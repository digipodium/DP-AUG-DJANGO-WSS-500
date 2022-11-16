from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.contrib.auth import logout
from .models import Slider


# def home_view(request):
#     ctx = {}
#     ctx['sliders'] = Slider.objects.all()
#     ctx['title'] = 'Home'
#     return render(request, 'home/index.html', ctx)

# Create your views here.
class HomeView(TemplateView):
    template_name = 'home/index.html'    

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Home'
        context['slider'] = Slider.objects.all()
        return context

class ProfileView(TemplateView):
    template_name = 'home/profile.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Profile'
        return context

# logout
def logout_view(request):
    logout(request)
    return redirect('home')

class ContactView(TemplateView):
    template_name = 'home/contact.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Contact'
        return context
