from django.views.generic.edit import CreateView
from tweety.models import TweetyTimor
from django.core.urlresolvers import reverse_lazy


class AddTweet(CreateView):
    model = TweetyTimor
    fields = ['comment']
    template_name = "tweety/tweety_index.html"
    success_url = reverse_lazy('index')

    def get_context_data(self, *args, **kwargs):
        context = super(AddTweet, self).get_context_data(*args, **kwargs)
        context['tweets'] = TweetyTimor.objects.all()
        return context
