from django.shortcuts import render
from django.views.generic.base import TemplateView
from tweety.models import Tweety
from django.core.urlresolvers import reverse_lazy
# Create your views here.


class Index(TemplateView):
    model = Tweety
    fields = ['description']
    template_name = 'tweety/index.html'
    success_url = reverse_lazy('index')
