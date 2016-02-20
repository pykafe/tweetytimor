from django.views.generic.edit import CreateView
from tweety.models import TweetyTimor
from django.core.urlresolvers import reverse_lazy


class Index(CreateView):
    model = TweetyTimor
    fields = ['comment', 'nation']
    template_name = "tweety/index.html"
    success_url = reverse_lazy('index')

    def get_context_data(self, *args, **kwargs):
        context = super(Index, self).get_context_data(*args, **kwargs)
        context['tweets'] = TweetyTimor.objects.order_by('-created_on')[:5]
        context['tweets_histories'] = TweetyTimor.objects.order_by('-created_on')
        context['total_tweets'] = TweetyTimor.objects.count()
        return context
