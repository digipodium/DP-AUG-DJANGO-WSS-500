from django.shortcuts import render, redirect
from django.views.generic import  View
from django.contrib import messages
from products.models import Product
from .models import OrderItem, Order
from django.utils import timezone




from .models import OrderItem, Order
from django.shortcuts import render, get_object_or_404

class OrderSummaryView(View):
    def get(self, *args, **kwargs):
        try:
            order = Order.objects.get(user=self.request.user, ordered=False)
            context = {
                'object': order
            }
            return render(self.request, 'order_summary.html', context)
        except:
            messages.error(self.request, "You do not have an active order")
            return redirect("home")

class OrderItemDeleteView(View):
    def get(self, *args, **kwargs):
        order_qs = Order.objects.filter(
            user=self.request.user,
            ordered=False
        )
        if order_qs.exists():
            order = order_qs[0]
            # check if the order item is in the order
            item = get_object_or_404(OrderItem, slug=self.kwargs.get('slug'))
            order.items.remove(item)
            messages.info(self.request, "This item was removed from your cart.")
            return redirect("core:order-summary")
        else:
            # add a message saying the user doesnt have an order
            messages.info(self.request, "You do not have an active order")
            return redirect("product", slug=self.kwargs.get('slug'))

class OrderItemAddView(View):
    def get(self, *args, **kwargs):
        product = get_object_or_404(Product, slug=self.kwargs.get('slug'))
        order_item, created = OrderItem.objects.get_or_create(
            product=product,
            user=self.request.user,
            ordered=False
        )
        order_qs = Order.objects.filter(user=self.request.user, ordered=False)
        if order_qs.exists():
            order = order_qs[0]
            # check if the order item is in the order
            if order.items.filter(product__slug=product.slug).exists():
                order_item.quantity += 1
                order_item.save()
                messages.info(self.request, "This item quantity was updated.")
                return redirect("order-summary")
            else:
                order.items.add(order_item)
                messages.info(self.request, "This item was added to your cart.")
                return redirect("order-summary")
        else:
            ordered_date = timezone.now()
            order = Order.objects.create(user=self.request.user, ordered_date=ordered_date)
            order.items.add(order_item)
            messages.info(self.request, "This item was added to your cart.")
            return redirect("order-summary")

     
