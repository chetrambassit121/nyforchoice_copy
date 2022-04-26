from django.urls import path         
from .views import register, UserEditView, PasswordsChangeView, load_citys, ShowProfilePageView, EditProfilePageView, UserDeleteView, ShowSharedProfilePageView #followToggle # ShowProfilePageWithPosts
from django.contrib.auth import views as auth_views
from . import views 
# from social.views import follow      
# load_branches,                                                                            

urlpatterns = [
   # path('register/', RegisterView.as_view(), name='register'), 
   path('register/', views.register, name='register'), 
   path('ajax/load-citys/', views.load_citys, name='ajax_load_citys'),
   # path('ajax/load-branches/', views.load_branches, name='ajax_load_branches'),

   # path('ajax/load-branches/', RegisterView.as_view(), name='ajax_load_branches'),
   path('<int:pk>/delete/', UserDeleteView.as_view(template_name='registration/delete.html'), name="account_delete"),
   path('<int:pk>/edit_profile/', UserEditView.as_view(), name='edit_profile'),                  
   path('<int:pk>/password/', PasswordsChangeView.as_view(template_name='registration/change_password.html')), 
   path('password_success/', views.password_success, name='password_success'),   
   # path('<int:pk>/profile/', ShowProfilePageView.as_view(), name='show_profile_page'),
   path('<int:pk>/profile/', ShowProfilePageView.as_view(), name='show_profile_page'),
   # path('<username>/profile/', ShowProfilePageViewUsername.as_view(), name='show_profile_page'),


   # path('<username>/profile/<option>', follow, name='show_profile_pagee'),
   # path('<int:pk>/profile/with-posts/', ShowProfilePageWithPosts, name='with-posts'),
   path('<int:pk>/profile/shared/', ShowSharedProfilePageView.as_view(), name='show_shared_profile_page'),  
   # path('<int:pk>/profile/shared/with-sharedposts', ShowProfilePageWithSharedPosts, name='with-sharedposts'),                                                                                      
   path('<int:pk>/edit_profile_page/', EditProfilePageView.as_view(), name='edit_profile_page'),            
   # path('create_profile_page/', CreateProfilePageView.as_view(), name='create_profile_page'), 
   path('activate/<uidb64>/<token>/', views.activate, name='activate'),
   path('reset_password/',
      auth_views.PasswordResetView.as_view(template_name="accounts/password_reset_form.html"),
      name="password_reset"),
   path('reset_password_sent/', 
      auth_views.PasswordResetDoneView.as_view(template_name="accounts/password_reset_done.html"), 
      name="password_reset_done"),
   path('reset/<uidb64>/<token>/',
      auth_views.PasswordResetConfirmView.as_view(template_name="accounts/password_reset_confirm.html"), 
      name="password_reset_confirm"),
   path('reset_password_complete/', 
      auth_views.PasswordResetCompleteView.as_view(template_name="accounts/password_reset_complete.html"), 
      name="password_reset_complete"),


   #path("followToggle/<str:author>/", views.followToggle, name="followToggle"),
]
