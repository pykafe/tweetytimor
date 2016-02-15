from django.shortcuts import TemplateView

# Create your views here.


class Home(TemplateView):
    template_name: 'home.html'
