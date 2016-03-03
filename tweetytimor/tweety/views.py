from django.views.generic.edit import CreateView
from tweety.models import TweetyTimor, LikeTweet, TweetComment
from django.core.urlresolvers import reverse_lazy
from django.db.models import Count
from django.http import HttpResponse


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
        context['tweets'] = TweetyTimor.objects.all().annotate(like_count=Count('liketweet'))
        context['total_tweets'] = TweetyTimor.objects.count()
        context['page_template'] = self.page_template_name
        return context


class LikeTweetView(CreateView):
    model = LikeTweet
    fields = ['tweet']
    template_name = 'tweety/like_tweet.html'
    success_url = reverse_lazy('tweety')

    def form_valid(self, form):
        if self.request.is_ajax():
            form.save()
            # find out how many likes htere are and return to the user
            count = LikeTweet.objects.filter(tweet=form.instance.tweet_id).count()
            return HttpResponse(str(count), status=201)
        else:
            return super(LikeTweetView, self).form_valid(form)


class TweetCommentView(CreateView):
    model = TweetComment
    fields = ['tweet', 'comment']
    template_name = 'tweety/comment_tweet.html'
    success_url = reverse_lazy('tweety')
