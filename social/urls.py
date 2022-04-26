# from django.urls import path
# from django.conf.urls import url 
# from .views import PostListView, PostDetailView, PostEditView, PostDeleteView, CommentDeleteView
# from . import views

# urlpatterns = [

# 	path('post-list', PostListView.as_view(), name='post-list'),
# 	path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
# 	path('post/edit/<int:pk>/', PostEditView.as_view(), name='post-edit'),
# 	path('post/delete/<int:pk>/', PostDeleteView.as_view(), name='post-delete'),
# 	path('post/<int:post_pk>/comment/delete/<int:pk>/', CommentDeleteView.as_view(), name='comment-delete')

# ]



from django.urls import path
from .views import PostListView, PostDetailView, PostEditView, PostDeleteView, NotificationView, CommentDeleteView, SharedPostView,  AddLike, AddDislike, UserSearch, AddCommentLike, AddCommentDislike, CommentReplyView, CreateThread, ListThreads, ThreadView, CreateMessage, Explore
from .views import PostNotification, PostDetailAddLike, PostDetailAddDislike, SharedProfileAddLike, SharedProfileAddDislike, ProfileAddLike, ProfileAddDislike, ThreadNotification, RemoveNotification, ReplyDeleteView, AddFollower, RemoveFollower, ListFollowers, FollowNotification, ListFollowings
# , DeleteFollower
# , follow, ListFollowings
# AddFollower, RemoveFollower, ListFollowings, ListFollowers, FollowNotification, like_unlike_post,
# ListFollowings, RemoveFollowing, 
# RemoveFollowerFromList



urlpatterns = [
    # path('', PublicPostListView.as_view(), name='public-post-list'),
    path('post-list/', PostListView.as_view(), name='post-list'),
    
    path('explore/', Explore.as_view(), name='explore'),

    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    

    path('post/edit/<int:pk>/', PostEditView.as_view(), name='post-edit'),
    path('post/delete/<int:pk>/', PostDeleteView.as_view(), name='post-delete'),

    path('post/<int:post_pk>/comment/delete/<int:pk>/', CommentDeleteView.as_view(), name='comment-delete'),
    path('post/<int:post_pk>/comment/<int:pk>/like', AddCommentLike.as_view(), name='comment-like'),
    path('post/<int:post_pk>/comment/<int:pk>/dislike', AddCommentDislike.as_view(), name='comment-dislike'),



    path('comment/<int:pk>/reply', CommentReplyView.as_view(), name='view-comment-reply'),
    path('post/<int:post_pk>/comment/<int:pk>/reply', CommentReplyView.as_view(), name='comment-reply'),
    path('comment/<int:comment_pk>/reply/delete/<int:pk>/', ReplyDeleteView.as_view(), name='reply-delete'),

    

    # path('post/<int:post_pk>/comment/<int:pk>/reply', CommentReplyView.as_view(), name='comment-reply'),
    # path('post/<int:post_pk>/comment/<int:pk>/reply/<int:num_replies>/', CommentReplyView.as_view(), name='comment-reply'), ## tried to create load button url for loading replies



    path('post/<int:id>/like', AddLike.as_view(), name='like'),
    path('post/<int:id>/dislike', AddDislike.as_view(), name='dislike'),
    path('post/<int:pk>/post-detail-like', PostDetailAddLike.as_view(), name='post-detail-like'),
    path('post/<int:pk>/post-detail-dislike', PostDetailAddDislike.as_view(), name='post-detail-dislike'),
    # path('post/<int:id>/profile-like', ProfileAddLike.as_view(), name='profile-like'),
    # path('post/<int:id>/profile-dislike', ProfileAddDislike.as_view(), name='profile-dislike'),
    path('profile/<int:pk>/post/<int:id>/profile-like', ProfileAddLike.as_view(), name='profile-like'),
    path('profile/<int:pk>/post/<int:id>/profile-dislike', ProfileAddDislike.as_view(), name='profile-dislike'),
    path('profile/<int:pk>/post/<int:id>/shared-profile-like', SharedProfileAddLike.as_view(), name='shared-profile-like'),
    path('profile/<int:pk>/post/<int:id>/shared-profile-dislike', SharedProfileAddDislike.as_view(), name='shared-profile-dislike'),
    # path('post/<int:id>/liked', like_unlike_post, name='like-post-view'),
    # path('liked/', like_unlike_post, name='like-post-view'),

    # path('post/<int:pk>/like', AddLike, name='like'),
    # path('post/<int:pk>/dislike', AddDislike, name='dislike'),
    path('post/<int:pk>/share', SharedPostView.as_view(), name='share-post'),
    # path('profile/<int:pk>/', ProfileView.as_view(), name='profile'),
    # path('profile/edit/<int:pk>/', ProfileEditView.as_view(), name='profile-edit'),

    # path("followToggle/<str:author>/", followToggle, name="followToggle"),
    # path('<username>/follow/<option>', follow, name='follow'),
    path('profile/<int:pk>/followers/', ListFollowers.as_view(), name='list-followers'),
    # # path('profile/<int:pk>/followers-list/remove', RemoveFollowerFromList.as_view(), name='remove-list-followers'),
    path('profile/<int:pk>/followers/add', AddFollower.as_view(), name='add-follower'),
    path('profile/<int:pk>/followers/remove', RemoveFollower.as_view(), name='remove-follower'),
    # path('profile/<int:pk>/followers/delete', DeleteFollower.as_view(), name='delete-follower'),



    path('profile/<int:pk>/followings/', ListFollowings.as_view(), name='list-followings'),
    # # path('profile/<int:pk>/followings/add', AddFollower.as_view(), name='add-following'),
    # # path('profile/<int:pk>/followings/remove', RemoveFollowing.as_view(), name='remove-following'),

    
    path('search/', UserSearch.as_view(), name='profile-search'),

    path('notifications/', NotificationView.as_view(), name='notifications'),
    # path('notification/<int:notification_pk>/post/<int:post_pk>', NotificationView.as_view(), name='post-notification'),
    # path('notification/<int:notification_pk>/profile/<int:profile_pk>', NotificationView.as_view(), name='follow-notification'),
    # path('notification/<int:notification_pk>/thread/<int:object_pk>', NotificationView.as_view(), name='thread-notification'),
    # path('notification/delete/<int:notification_pk>', NotificationView.as_view(), name='notification-delete'),

    path('notification/<int:notification_pk>/post/<int:post_pk>', PostNotification.as_view(), name='post-notification'),
    path('notification/<int:notification_pk>/profile/<int:profile_pk>', FollowNotification.as_view(), name='follow-notification'),
    path('notification/<int:notification_pk>/thread/<int:object_pk>', ThreadNotification.as_view(), name='thread-notification'),
    path('notification/delete/<int:notification_pk>', RemoveNotification.as_view(), name='notification-delete'),

    path('inbox/', ListThreads.as_view(), name='inbox'),
    path('inbox/create-thread/', CreateThread.as_view(), name='create-thread'),
    path('inbox/<int:pk>/', ThreadView.as_view(), name='thread'),
    path('inbox/<int:pk>/create-message/', CreateMessage.as_view(), name='create-message'),
]