from django.views.generic.edit import CreateView
from tweety import models
from tweety.forms import TweetyCommentForm
from django.core.urlresolvers import reverse_lazy


class Index(CreateView):
    model = models.TweetyTimor
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
        context['tweets'] = models.TweetyTimor.objects.order_by('-created_on')[:5]
        context['total_tweets'] = models.TweetyTimor.objects.count()
        context['page_template'] = self.page_template_name
        return context


class Like(CreateView):
    model = models.Like
    fields = ['tweety']
    template_name = 'tweety/tweety_like.html'
    page_template_name = 'tweety/tweety_like_tweetpage.html'
    success_url = reverse_lazy('like')


class TweetyComment(CreateView):
    model = models.TweetyComment
    fields = ['tweet', 'tweetycomment']
    template_name = 'tweety/tweety_tweetycomment.html'
    page_template_name = 'tweety/tweety_tweetycomment_tweetpage.html'
    success_url = reverse_lazy('index')
    #form_class = TweetyCommentForm

    def get_template_names(self):
        if self.request.is_ajax():
            return [self.page_template_name]
        return super(TweetyComment, self).get_template_names()

    def get_context_data(self, **kwargs):
        context = super(TweetyComment, self).get_context_data(**kwargs)
        context['page_template'] = self.page_template_name
        context['tweet'] = models.TweetyTimor.objects.get(id=self.kwargs.get('tweet'))
        context['comments'] = models.TweetyComment.objects.filter(tweet=self.kwargs.get('tweet'))
        return context
