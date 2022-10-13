from django import forms
from django import forms
from detailView.models import Book

class Addform(forms.ModelForm):
    class Meta:
        model=Book
        fields=('title','author','isbn')
        widgets={
        'title':forms.TextInput(attrs={'class':'form-control'}),
        'author':forms.TextInput(attrs={'class':'form-control'}),
        'isbn':forms.TextInput(attrs={'class':'form-control'}),
        
        }

    
    

