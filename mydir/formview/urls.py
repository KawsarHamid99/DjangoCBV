from django.urls import path
from . import views
urlpatterns = [ 
    path('',views.addView.as_view(),name="formview"),
    path('createview/',views.AddView.as_view(),name='createview'),
    path('<slug:slug>/edit',views.AddeditView.as_view(),name="edit-detail")
]