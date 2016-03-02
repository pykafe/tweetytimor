from django.views.generic.edit import CreateView, ModelFormMixin
from tweety.models import TweetyTimor, TweetyLike, TweetyCreated
from .forms import LikeForm
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
        context['like_form'] = LikeForm()
        return context


class Like(CreateView):
    model = TweetyLike
    fields = ['like']
    template_name = "tweety/like.html"
    success_url = reverse_lazy('index')


class CreateTweetyUser(CreateView):
    model = TweetyCreated
    fields = ['first_name', 'last_name', 'username', 'password', 'email', 'confirme_email']
    template_name = "tweety/create.html"
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        self.object = form.save()
        self.object.set_password(self.object.password)
        self.object.save()
        return super(ModelFormMixin, self).form_valid(form)

    def get_context_data(self, *args, **kwargs):
        context = super(CreateTweetyUser, self).get_context_data(*args, **kwargs)
        context['total_users'] = TweetyCreated.objects.count()
        return context
