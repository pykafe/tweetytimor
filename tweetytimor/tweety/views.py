from django.views.generic.edit import CreateView
from tweety.models import TweetyTimor, TweetyLike
from django.core.urlresolvers import reverse_lazy


class Index(CreateView):
    model = TweetyTimor
    fields = ['comment', 'nation', 'photo']
    template_name = "tweety/index.html"
    success_url = reverse_lazy('index')

    def get_context_data(self, *args, **kwargs):
        context = super(Index, self).get_context_data(*args, **kwargs)
        context['tweets'] = TweetyTimor.objects.order_by('-created_on')[:5]
        context['tweets_histories'] = TweetyTimor.objects.order_by('-created_on')
        context['total_tweets'] = TweetyTimor.objects.count()
        context['like_tweets'] = TweetyLike.objects.count()
        return context


class Like(CreateView):
    model = TweetyLike
    fields = ['like']
    template_name = "tweety/like.html"
    success_url = reverse_lazy('index')
