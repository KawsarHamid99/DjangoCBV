
from itertools import count
from multiprocessing import context
from django.shortcuts import get_object_or_404, render
from django.db.models import F
# Create your views here.
from django.views.generic import TemplateView,ListView,RedirectView
from .models import Post

class Dog:
    def hello(self):
        
        print("any qstn...???")
        return "baksi from self class"

class Tview(TemplateView,Dog):

    template_name="base.html"
    def __init__(self):
        new=super().hello()
        self.new=new
        print(new)
    def get_context_data(self,**kwargs):
        context=super().get_context_data(**kwargs)
        context['posts']=Post.objects.get(id=2)
        context['data']="context data from template view"
        context['new']=self.new 

        return context


class PostPreloadedtaskView(RedirectView):
    pattern_name='cbv:singleobject'
    def get_redirect_url(self,*args,**kwargs):
        post=Post.objects.filter(id=kwargs['pk'])
        post.update(roll=F('roll')+11)

        return super().get_redirect_url(*args,**kwargs)





class SinglePostView(TemplateView):
    template_name="base.html"

    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        print("----------------------------------------------------------------")
        #context['posts']=get_object_or_404(Post,pk=self.kwargs.get('pk'))
        context['posts']=Post.objects.get(id=kwargs['pk'])
        

       
        print(context['posts'])
        return context
