from django.urls import path
from django.conf.urls import url 
from .views import HomeView, AboutView, PromotePetitionsView, SurveyView, the_plan, like, dislike, executive_orders, vaccine_percentages

from . import views
# SurveyCommentView


urlpatterns = [
   path('', HomeView, name='home'),                                                                      
   path('promote_the_petitions/', PromotePetitionsView, name='promote_the_petitions'),
   path('about/', AboutView, name='about'),
   path('surveys/', SurveyView, name='surveys'),


   # path('survey_comment/<int:id>/', SurveyCommentView.as_view(), name='survey_comment'),
   # path('survey_comment/<int:pk>/', SurveyCommentView.as_view(), name='survey_comment'),

   path('the_plan/', the_plan, name='the_plan'),
   path("like/<int:id>/", like, name="likes"),
   path("dislike/<int:id>/", dislike, name="dislikes"),
   path('executive_orders/', executive_orders, name='executive_orders'),
   path('vaccine_percentages/', vaccine_percentages, name='vaccine_percentages'),

  


   # path('post', PostListView.as_view(), name='post-list'),
   # path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
   # path('post/edit/<int:pk>/', PostEditView.as_view(), name='post-edit'),
   # path('post/delete/<int:pk>/', PostDeleteView.as_view(), name='post-delete'),
   # path('post/<int:post_pk>/comment/delete/<int:pk>/', CommentDeleteView.as_view(), name='comment-delete')
]