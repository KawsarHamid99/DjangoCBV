from itertools import count
from multiprocessing import context
from django.shortcuts import render,HttpResponse
from django.views.generic import TemplateView,DetailView,ListView
from .models import Book
from django.db.models import F 
from django.utils import timezone
# Create your views here.


class Booklist(ListView):
    model = Book
    template_name = 'listview2.html'
    context_object_name = 'book'
    paginate_by=1
    #queryset=Book.objects.all()[:2]
    def get_queryset(self):
        return Book.objects.all()[:3]


class IsbnView(ListView):
    model=Book
    template_name="listview2.html"
    context_object_name='book'
    paginate_by=2




class IndexView(TemplateView):
    template_name='booklist.html'
    def get_context_data(self,**kwargs):
        context=super().get_context_data(**kwargs)
        context['book']=Book.objects.all()
        print("--------------------------------------")
        print(context['book'])
        return context





class bookDetailView(DetailView):
    model=Book
    template_name='bookdetails.html'
    context_object_name='book'

    def get_context_data(self,**kwargs):
        context=super().get_context_data(**kwargs)

        post=Book.objects.filter(slug=self.kwargs.get('slug'))
        post.update(count=F('count')+1)

        context['time']=timezone.now()

        return context