from django.views.generic.edit import CreateView
from tweety.models import TweetyTimor
from django.core.urlresolvers import reverse_lazy


class AddTweet(CreateView):
    model = TweetyTimor
    fields = ['comment']
    template_name = "tweety/tweety_index.html"
    page_template_name = 'tweety/tweety_index_tweetpage.html'
    success_url = reverse_lazy('tweety')

    def get_template_names(self):
        if self.request.is_ajax():
            return [self.page_template_name]
        return super(CreateView, self).get_template_names()

    def get_context_data(self, *args, **kwargs):
        context = super(AddTweet, self).get_context_data(*args, **kwargs)
        context['tweets'] = TweetyTimor.objects.all()
        context['total_tweets'] = TweetyTimor.objects.count()
        context['page_template'] = self.page_template_name
        return context
