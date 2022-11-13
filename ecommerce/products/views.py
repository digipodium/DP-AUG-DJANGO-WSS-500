from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from .forms import ProductForm
from .models import Product
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Create your views here.
class ProductListView(ListView):
    model = Product
    template_name = 'products/list.html'
    context_object_name = 'products'
    paginate_by = 10

class ProductDetailView(DetailView):
    model = Product
    template_name = 'products/detail.html'
    context_object_name = 'product'


@login_required
def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            object = form.save(commit=False)
            slug = form.cleaned_data.get('title').replace(' ', '-')
            object.slug = slug
            object.save()
            messages.success(request, 'Product added successfully')
            return redirect('product_list')
        else:
            messages.error(request, 'Error adding product')
    else:
        form = ProductForm()
    return render(request, 'products/add.html', {'form': form})