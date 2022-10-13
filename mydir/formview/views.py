from django.shortcuts import render
from django.views.generic import TemplateView,FormView
from django.views.generic.edit import FormView,CreateView,UpdateView
from .forms import Addform
from detailView.models import Book
# Create your views here.
class TemView(TemplateView):
    template_name="formview/base.html"



class addView(FormView):
    template_name="formview/add.html"
    form_class=Addform
    success_url='/detailView'


    def form_valid(self,form):
        form.save()
        return super().form_valid(form)

class AddeditView(UpdateView):
    model=Book
    form_class=Addform
    template_name='formview/add.html'
    success_url= '/detailView'



# By using CreateView
class AddView(CreateView):
    model= Book
    form_class=Addform
    template_name='formview/add.html'
    success_url = '/detailView'

    # we can add aditional information to the form
    #fields=['title']
    def get_initial(self,*args,**kwargs):
        initial=super().get_initial(**kwargs)
        initial['title']='Enter Title'
        return initial

