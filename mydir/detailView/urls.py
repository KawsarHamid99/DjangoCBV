from django.urls import path
from . import views
app_name='book'
urlpatterns=[ 
    path("",views.IndexView.as_view(),name="home"),
    path('<slug:slug>/',views.bookDetailView.as_view(),name="details"),
    path("bookl",views.Booklist.as_view(),name="booklist"),
    path('isbn/<str:isbn>/',views.IsbnView.as_view(),name="isbn")


]