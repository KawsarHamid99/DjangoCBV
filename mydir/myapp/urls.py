from django.urls import path
from . import views


app_name="cbv"
urlpatterns=[ 
    path("",views.Tview.as_view()),
    path("singleobject/<int:pk>/",views.SinglePostView.as_view(),name='singleobject'),
    path("postpreloaded/<int:pk>",views.PostPreloadedtaskView.as_view(),name="postpreloaded")

]