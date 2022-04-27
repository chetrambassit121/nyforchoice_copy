from django.urls import path
from django.conf.urls import url 
from .views import HomeView, AboutView, SurveyView, like, dislike 

from . import views
# SurveyCommentView


urlpatterns = [
   path('', HomeView, name='home'),                                                                      
   path('about/', AboutView, name='about'),
   path('surveys/', SurveyView, name='surveys'),
   path("like/<int:id>/", like, name="likes"),
   path("dislike/<int:id>/", dislike, name="dislikes"),
  
]