from django.views.generic.edit import CreateView, ModelFormMixin, UpdateView
from django.views.generic.base import TemplateView
from django.contrib.messages.views import SuccessMessageMixin
from tweety.models import TweetyTimor, TweetyLike, TweetyUser, PersonTweety
from .forms import LikeForm, RegisterUser, PersonForm
from django.core.urlresolvers import reverse_lazy
#from tinymce.widgets import TinyMCE
#from django import forms
from django_markdown.widgets import MarkdownWidget
from django.forms.widgets import Widget
from django.shortcuts import render
from django.http import HttpResponseRedirect
from webcam.fields import CameraField



class Index(CreateView):
    model = TweetyTimor
    fields = ['comment', 'nation', 'photo']
    template_name = "tweety/index.html"
    success_url = reverse_lazy('index')

    def get_context_data(self, *args, **kwargs):
        context = super(Index, self).get_context_data(*args, **kwargs)
        context['tweets'] = TweetyTimor.objects.order_by('-created_on')
        context['tweets_histories'] = TweetyTimor.objects.order_by('-created_on')
        context['total_tweets'] = TweetyTimor.objects.count()
        context['like_tweets'] = TweetyLike.objects.count()
        context['cameras'] = PersonTweety.objects.all()
        context['like_form'] = LikeForm()
        return context

   # def get_form(self):
    #    form = super(Index, self).get_form()
     #   form.fields['comment'].widget =TinyMCE()
      #  return form

    def get_form(self):
        form = super(Index, self).get_form()
        form.fields['comment'].widget = MarkdownWidget(attrs={'cols': 20, 'rows': 20})
        return form


class Like(CreateView):
    model = TweetyLike
    fields = ['like']
    template_name = "tweety/like.html"
    success_url = reverse_lazy('index')



class Person(CreateView):
    form_class = PersonForm
    template_name = "webcam/templates/webcam/dbwidget.html"
    success_url = reverse_lazy('index')

    #def dispatch(self, request, *args, **kwargs):
     #   import pudb; pudb.set_trace()
       # return super(Person, self).dispatch(request, *args, **kwargs)
   # def save(self):
    #    picture = super(Person, self).save()
     #   picture = self.cleaned_data["picture"]
      #  picture.save()
       # return picture

   # def form_valid(self, form):
    #    self.object = form.save()
     #   self.object.picture()
      #  self.object.save()
       # return super(ModelFormMixin, self).form_valid(form)

    #def get_person(self, form, request):

      #  if request.method == 'POST':
       #     form = Person(request.POST)
        #    if form.is_valid():
         #       picture = form.cleaned_data['picture']
          #      return HttpResponseRedirect('/')
        #else:
         #   form = PersonForm()
        #return render(request, )


class CreateTweetyUser(SuccessMessageMixin, CreateView):
    form_class = RegisterUser
    template_name = "tweety/create.html"
    success_url = reverse_lazy('index')
    success_message = "welcome to your comment"

    def form_valid(self, form):
        self.object = form.save()
        self.object.set_password(self.object.password)
        self.object.save()
        return super(ModelFormMixin, self).form_valid(form)

    def get_context_data(self, *args, **kwargs):
        context = super(CreateTweetyUser, self).get_context_data(*args, **kwargs)
        context['total_users'] = TweetyUser.objects.count()
        return context

    #def get_form(self):
     #   form = super(CreateTweetyUser, self).get_form()
      #  form.fields['password'].widget = forms.PasswordInput()
       # return form


class UpdateTweety(UpdateView):
    model = TweetyTimor
    fields = ['comment', 'nation', 'photo']
    template_name = "tweety/index.html"
    success_url = reverse_lazy('index')

    def get_form(self):
        form = super(UpdateTweety, self).get_form()
        form.fields['comment'].widget = MarkdownWidget(attrs={'cols': 20, 'rows': 20})
        return form


class TodoView(TemplateView):
    template_name = 'tweety/comment.html'
