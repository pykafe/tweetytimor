from django.views.generic.edit import CreateView, ModelFormMixin
from tweety.models import TweetyTimor, Like, TweetComment, Member
from django.core.urlresolvers import reverse_lazy
from django.db.models import Count
from django.http import HttpResponse


class TweetyCreate(CreateView):
    model = TweetyTimor
    fields = ['comment']
    template_name = 'tweety/tweety_index.html'
    page_template_name = 'tweety/tweety_index_tweetpage.html'
    success_url = reverse_lazy('tweety')

    def get_template_names(self):
        if self.request.is_ajax():
            return [self.page_template_name]
        return super(CreateView, self).get_template_names()

    def get_context_data(self, **kwargs):
        context = super(TweetyCreate, self).get_context_data(**kwargs)
        context['tweets'] = TweetyTimor.objects.all().annotate(like_count=Count('like'))
        context['count_tweets'] = TweetyTimor.objects.count()
        context['page_template'] = self.page_template_name
        return context


class CreateMember(CreateView):
    model = Member
    fields = ['user', 'first_name', 'last_name', 'username', 'password']
    template_name = 'tweety/create_members.html'
    success_url = reverse_lazy('create')

    def form_valid(self, form):
        ''' Overriding the form valid method to set the user password correctly '''
        self.object = form.save()
        self.object.set_password(self.object.password)
        self.object.save()
        return super(ModelFormMixin, self).form_valid(form)


class LikeTweet(CreateView):
    model = Like
    fields = ['tweet']
    template_name = 'tweety/like_tweet.html'
    success_url = reverse_lazy('like')

    def form_valid(self, form):
        if self.request.is_ajax():
            form.save()
            # find out how many likes htere are and return to the user
            count = LikeTweet.objects.filter(tweet=form.instance.tweet_id).count()
            return HttpResponse(str(count), status=201)
        else:
            return super(LikeTweet, self).form_valid(form)


class TweetComment(CreateView):
    model = TweetComment
    fields = ['tweet', 'tweetcomment']
    template_name = 'tweety/comment_tweet.html'
    success_url = reverse_lazy('comment')

    def form_valid(self, form):
        if self.request.is_ajax():
            form.save()
            # find out how many comments htere are and return to the user
            count = TweetComment.objects.filter(tweet=form.instance.tweetcomment_id).count()
            return HttpResponse(str(count), status=201)
        else:
            return super(TweetComment, self).form_valid(form)
