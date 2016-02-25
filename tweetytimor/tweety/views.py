from django.views.generic.edit import CreateView
from tweety.models import TweetyTimor
from django.core.urlresolvers import reverse_lazy


class Index(CreateView):
    model = TweetyTimor
    fields = ['comment']
    template_name = 'tweety/tweety_index.html'
    page_template_name = 'tweety/tweety_index_tweetpage.html'
    success_url = reverse_lazy('index')

    def get_template_names(self):
        if self.request.is_ajax():
            return [self.page_template_name]
        return super(CreateView, self).get_template_names()

    def get_context_data(self, **kwargs):
        context = super(Index, self).get_context_data(**kwargs)
        context['tweets'] = TweetyTimor.objects.all()
        context['count_tweets'] = TweetyTimor.objects.count()
        context['page_template'] = self.page_template_name
        return context
