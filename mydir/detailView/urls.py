from django.urls import path
from . import views
app_name='book'
urlpatterns=[ 
    path("",views.IndexView.as_view(),name="home"),
    path('<slug:slug>/',views.bookDetailView.as_view(),name="details")
]