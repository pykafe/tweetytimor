from django.views.generic.edit import CreateView
from tweety.models import TweetyTimor
from django.core.urlresolvers import reverse_lazy
# Create your views here.


class Index(CreateView):
    model = TweetyTimor
    fields = ['comment']
    template_name = 'tweety/index.html'
    success_url = reverse_lazy('index')

    def get_context_data(self, **kwargs):
        context = super(Index, self).get_context_data(**kwargs)
        context['tweets'] = TweetyTimor.objects.all()
        return context
