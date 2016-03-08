from django.views.generic.edit import CreateView
from tweety.models import TweetyTimor, Like, TweetyComment
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
        context['tweets'] = TweetyTimor.objects.order_by('-created_on')[:5]
        context['total_tweets'] = TweetyTimor.objects.count()
        context['page_template'] = self.page_template_name
        return context


class Like(CreateView):
    model = Like
    fields = ['tweety']
    template_name = 'tweety/tweety_like.html'
    page_template_name = 'tweety/tweety_like_tweetpage.html'
    success_url = reverse_lazy('like')


class TweetyComment(CreateView):
    model = TweetyComment
    fields = ['tweety', 'tweetycomment']
    template_name = 'tweety/tweety_tweetycomment.html'
    page_template_name = 'tweety/tweety_tweetycomment_tweetpage.html'
    success_url = reverse_lazy('tweetycomment')

    def get_template_names(self):
        if self.request.is_ajax():
            return [self.page_template_name]
        return super(CreateView, self).get_template_names()

    def get_context_data(self, **kwargs):
        context = super(Index, self).get_context_data(**kwargs)
        context['page_template'] = self.page_template_name
        return context
