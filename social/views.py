from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q
from django.utils import timezone
from django.urls import reverse_lazy, reverse
from django.shortcuts import redirect
from django.contrib import messages
# from django.contrib.auth.models import User
# from members.models import User 

from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from django.views import View
from .models import Post, Comment, Notification, ThreadModel, MessageModel, Tag
# , Like
# Follow
from members.models import UserProfile, User
from .forms import PostForm, CommentForm, EditPostForm, ThreadForm, MessageForm, ExploreForm, ShareForm
from django.views.generic.edit import UpdateView, DeleteView
from django.views.generic.list import ListView
from django.views import generic 
from django import template     
from django.core.paginator import Paginator        
from django.template.loader import render_to_string




# # @login_required
# def follow(request, username, option, *args, **kwargs):
#     # profile = get_object_or_404(UserProfile, pk=pk)
#     following = get_object_or_404(User, username=username)
#     # following = UserProfile.objects.get(pk=pk)
#     try:
#         f, created = Follow.objects.get_or_create(follower=request.user, following=following)

#         if int(option) == 0:
#             f.delete()
#             # Stream.objects.filter(following=following, user=request.user).all().delete()
#         # else:
#         #     posts = Post.objects.all().filter(user=following)[:25]

#         #     with transaction.atomic():
#         #         for post in posts:
#         #             stream = Stream(post=post, user=request.user, date=post.posted, following=following)
#         #             stream.save()

#         return HttpResponseRedirect(reverse('show_profile_page_username', args=[username]))
#         # return HttpResponseRedirect(reverse('show_profile_page', user=user.id))
#         # return redirect('show_profile_page', pk=profile.pk)
#     except User.DoesNotExist:
#         return HttpResponseRedirect(reverse('show_profile_page_username', args=[username]))
#         # return HttpResponseRedirect(reverse('show_profile_page', user=user.id))
#         # return redirect('show_profile_page', pk=profile.pk)



class ListFollowers(View):
    def get(self, request, pk, *args, **kwargs):
        profile = UserProfile.objects.get(pk=pk)

        followers = profile.followers.all()

        if len(followers) == 0:
            is_following = False

        for follower in followers:
            if follower == request.user:
                is_following = True
                break
            else:
                is_following = False

        number_of_followers = len(followers)

        context = {
            'profile': profile,
            'followers': followers,
            'is_following': is_following,
            'number_of_followers': number_of_followers,
        }

        return render(request, 'social/followers_list.html', context)

class AddFollower(LoginRequiredMixin, View):
    def post(self, request, pk, *args, **kwargs):
        profile = UserProfile.objects.get(pk=pk)
        profile.followers.add(request.user)
        # followers = profile.followers.add(request.user)

        # if request.user in profile.followers:
        #     request.user.followings.add(profile)
        # session_user = request.session['user']
        
        # request.user.followings.add(profile)
        

        notification = Notification.objects.create(notification_type=3, from_user=request.user, to_user=profile.user)

        return redirect('show_profile_page', pk=profile.pk)

class RemoveFollower(LoginRequiredMixin, View):
    def post(self, request, pk, *args, **kwargs):
        profile = UserProfile.objects.get(pk=pk)
        profile.followers.remove(request.user)
        # request.user.followings.remove(profile.pk)
        # request.user.followings.remove(profile)

        return redirect('show_profile_page', pk=profile.pk)


# class DeleteFollower(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
#     model = UserProfile
#     template_name = 'social/delete-follower.html'
#     success_url = reverse_lazy('list-followers')

#     def test_func(self):
#         user = self.get_object()
#         return self.request.user

#     def get_success_url(self):
#         pk = self.kwargs['followers']
#         return reverse_lazy('list-followers', kwargs={'pk': pk})

# class DeleteFollower(LoginRequiredMixin, View):
#     def post(self, request, pk, *args, **kwargs):
#         profile = UserProfile.objects.get(pk=pk)
#         profile.followers.remove(request.user)
#         # request.user.followings.remove(profile.pk)
#         # request.user.followings.remove(profile)

#         return redirect('list-followers', pk=profile.pk)


class ListFollowings(View):
    def get(self, request, pk, *args, **kwargs):
        profile = UserProfile.objects.get(pk=pk)
        # session_user = request.session['user']
        # all_profiles = UserProfile.objects.all()
        # all_followers = all_profiles.followers.all()
        # if session_user in all_followers:
        #     request.user.followings.add(profile.pk)
        # followings = Follow.objects.filter(follower=user).get()
        followings = profile.followings.all()

        

        context = {
            'profile': profile,
            'followings': followings,
        }

        return render(request, 'social/followings_list.html', context)

# class ListFollowings(View):
#     def get(self, request, pk, followers, followings, *args, **kwargs):
#         # profile = UserProfile.objects.get(pk=pk)
#         # session_user = request.session['user']
#         # all_profiles = UserProfile.objects.all()
#         all_followers = UserProfile.objects.filter(followers=followers)
#         if request.user in all_followers:
#             request.user.followings.add(profile.pk)
#         # followings = Follow.objects.filter(follower=user).get()
#         followings = request.user.followings.filter(followings=followings)

        

#         context = {
#             'profile': profile,
#             'followings': followings,
#         }

#         return render(request, 'social/followings_list.html', context)





# # class RemoveFollowerFromList(LoginRequiredMixin, View):
# #     def post(self, request, pk, *args, **kwargs):
# #         profile = UserProfile.objects.get(pk=pk)
# #         profile.followers.remove(request.user)

# #         return redirect('list-followers', pk=profile.pk)

# class AddFollowing(LoginRequiredMixin, View):
#     def get(self, request, followers, *args, **kwargs):
#         # profile = UserProfile.objects.all()
#         profile = UserProfile.objects.get(followers=followers)
#         if request.user in profile:
#             request.user.profile.followings.add(profile)

#         # notification = Notification.objects.create(notification_type=3, from_user=request.user, to_user=profile.user)

#         return redirect('show_profile_page', pk=profile.pk)

# # class RemoveFollowing(LoginRequiredMixin, View):
# #     def post(self, request, pk, *args, **kwargs):
# #         profile = UserProfile.objects.get(pk=pk)
# #         profile.followings.remove(request.user)

# #         return redirect('show_profile_page', pk=profile.pk)













































































class PostListView(View):
    def get(self, request, *args, **kwargs):
        form = PostForm()
        share_form = ShareForm()
        post = Post.objects.all()
        post_count = post.count()




        # post_data = Post.objects.get(pk=pk)
        comment = Comment.objects.filter(post=post)
        



      
        p = Paginator(Post.objects.all(), 10)
        page = request.GET.get('page')
        posts = p.get_page(page)
        context = {
          'posts': posts,
          # 'share_post': share_post,
          'shareform': share_form,
          'form': form,
          'post_count': post_count,
          # 'comment_count': comment_count,
          # 'paginator': paginator,
          # 'profile': profile,
          # 'user': user,
        }
    
        return render(request, 'social/post_list.html', context)

    def post(self, request, *args, **kwargs):
        post = Post.objects.all()
        post_count = post.count()
        form = PostForm(request.POST, request.FILES)
        # files = request.FILES.getlist('image')
        share_form = ShareForm()
        p = Paginator(Post.objects.all(), 10)
        page = request.GET.get('page')
        posts = p.get_page(page)
       

        if form.is_valid():
            new_post = form.save(commit=False)
            new_post.author = request.user
            new_post.save()
            form = PostForm()
            


        ## code for multiple images took it out .. 
        # if form.is_valid():
        #     new_post = form.save(commit=False)
        #     new_post.author = request.user
        #     new_post.save()

        #     for f in files:
        #         img = Image(image=f)
        #         img.save()
        #         new_post.image.add()

        #     new_post.save()

        new_post.create_tags()

        context = {
            'posts': posts,
            'shareform': share_form,
            'form': form,
            'post_count': post_count,
        }
        # if request.is_ajax():
        #     html = render_to_string('social/posts.html', context, request=request)
        #     return JsonResponse({'form':html})

        return render(request, 'social/post_list.html', context)




# code for sharing post 
class SharedPostView(View):
    def post(self, request, pk, *args, **kwargs):
        original_post = Post.objects.get(pk=pk)
        # post = Post.objects.all()
        form = ShareForm(request.POST, request.FILES)
        # imageform = ImageForm(request.POST)
        # share_form = ShareForm(request.POST, request.FILES)

        if form.is_valid():
            new_post = Post(
                shared_body=self.request.POST.get('body'),
                # shared_image=post.image,
                image=original_post.image,
                video=original_post.video,
                body=original_post.body,
                author=original_post.author,
                # shared_likes=original_post.likes,
                # shared_dislikes=original_post.dislikes,
                # shared_likes=self.request.POST.get('likes'),
                # shared_dislikes=self.request.POST.get('dislikes'),
                shared_on=original_post.created_on,
                shared_user=request.user,
                created_on=timezone.now(),

            )
            
            new_post.save()
            # form = ShareForm()

        # if imageform.is_valid():
        #     new_image = (
        #         image=post.image,
        #     )

            new_post.create_tags()

        return redirect('post-list')

 
class PostDetailView(LoginRequiredMixin, ListView):
    def get(self, request, pk, *args, **kwargs):
        post = Post.objects.get(pk=pk)
        form = CommentForm()
        # form = ReplyForm()
        comment = Comment.objects.filter(post=post)
        # childrenn = children.count()

        # all_comments = Comment.all()
        # children = comment.children()

        # parent_comment = Comment.objects.get(pk=pk)
        # parent_comment_count = parent_comment.count()

        # comment_count = (int(comment.count()) - int(children.count())) 
        comment_count = comment.count()  


        # replies = Comment.children.get()[0:5]

        # paginate_by = 5
        p = Paginator(Comment.objects.filter(post=post), 10)
        # p = Paginator(Comment.objects.filter(parent=parent), 10)

        page = request.GET.get('page')
        comments = p.get_page(page)

        context = {
            'post': post,
            # 'children': children,
            # 'all_comments': all_comments,
            'form': form,
            'comment_count': comment_count,
            # 'child_comment': children_comment,
            # 'parent_comment_count': parent_comment_count,
            'comments': comments,
            # 'data': replies, 
            # 'max':max_size,
            # 'replies': replies,
            # 'total_comments': total_comments,
        }

        return render(request, 'social/post_detail.html', context)


    # def load_more(request):
    #     total_replies = int(request.GET.get('total_replies'))
    #     limit = 2
    #     comment_obj = list(Comment.objects.values()[offset_int:offset_int+limit])
    #     data = {
    #         'comments': comment_obj
    #     }
    #     return JsonResponse(data=data)



    def post(self, request, pk, *args, **kwargs):
        post = Post.objects.get(pk=pk)
        form = CommentForm(request.POST)

        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.author = request.user
            new_comment.post = post
            new_comment.save()
            new_comment.create_tags()
            form = CommentForm()

        # comments = Comment.objects.filter(post=post)

        p = Paginator(Comment.objects.filter(post=post), 10)
        page = request.GET.get('page')
        comments = p.get_page(page)

        notification = Notification.objects.create(notification_type=2, from_user=request.user, to_user=post.author, post=post)
        context = {
            'post': post,
            'form': form,
            # 'comments': comments,
            'comments': comments,
        }
        ## KEEP AJAX .. when user makes a comment .. page doesnt refresh .. if user clicks like.dislike data returned instead of html page ... user has to refesh page to like.dislike
        # if request.is_ajax():
        #     html = render_to_string('social/comments.html', context, request=request)
        #     return JsonResponse({'form':html})

        return render(request, 'social/post_detail.html', context)
        # return redirect('/post-detail', context)




class CommentReplyView(LoginRequiredMixin, ListView):
    def get(self, request, pk, *args, **kwargs):
        # post = Post.objects.get(pk=pk)

        form = CommentForm()
        # form = ReplyForm()
        comment = Comment.objects.get(pk=pk)
        # all_comments = Comment.all()
        # children = comment.children()

        # parent_comment = Comment.objects.get(pk=pk)
        # parent_comment_count = parent_comment.count()

        # comment_count = (int(comment.count()) - int(children_comment.count())) 
        # comment_count = comment.count()  


        # replies = Comment.children.get()[0:5]

        # paginate_by = 5
        # p = Paginator(Comment.objects.get(children=children), 5)
        # page = request.GET.get('page')
        # comment = p.get_page(page)
        context = {
            # 'post': post,
            # 'children': children,
            # 'all_comments': all_comments,
            'form': form,
            # 'comment_count': comment_count,
            # 'child_comment': children_comment,
            # 'parent_comment_count': parent_comment_count,
            'comment': comment,
            # 'data': replies, 
            # 'max':max_size,
            # 'replies': replies,
            # 'total_comments': total_comments,
        }
        return render(request, 'social/post_comment_replies.html', context)
    def post(self, request, pk, post_pk, *args, **kwargs):
        post = Post.objects.get(pk=post_pk)
        parent_comment = Comment.objects.get(pk=pk)
        form = CommentForm(request.POST)

        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.author = request.user
            new_comment.post = post
            new_comment.parent = parent_comment
            new_comment.save()

        notification = Notification.objects.create(notification_type=2, from_user=request.user, to_user=parent_comment.author, comment=new_comment)
        # context = {
        #     # 'post': post,
        #     'parent_comment': parent_comment,
        #     'form': form,
        #     # 'comments': comments,
        #     # 'comments': comments,
        # }
        # if request.is_ajax():
        #     html = render_to_string('social/comments.html', context, request=request)
        #     return JsonResponse({'form':html})
        return redirect('post-detail', pk=post_pk)
        # return redirect('comment-reply', pk=post_pk)
        # return render(request, 'social/post_comment_replies.html', context)
        # return render(request, 'social/get_comments_for_post_detail.html', pk=post_pk)




    # def post(self, request, post_pk, pk, *args, **kwargs):
    #     post = Post.objects.get(pk=post_pk)
    #     parent_comment = Comment.objects.get(pk=pk)
    #     form = CommentForm(request.POST)

    #     if form.is_valid():
    #         new_comment = form.save(commit=False)
    #         new_comment.author = request.user
    #         new_comment.post = post
    #         new_comment.parent = parent_comment
    #         new_comment.save()

    #     notification = Notification.objects.create(notification_type=2, from_user=request.user, to_user=parent_comment.author, comment=new_comment)

    #     return redirect('post-detail', pk=post_pk)
    #     # return render(request, 'social/get_comments_for_post_detail.html', pk=post_pk)



    ## tired to get replies and return them into ajax function with load more button 
    # def get(self, *args, **kwargs):
    #     upper = kwargs.get('num_replies')
    #     lower = upper - 3
    #     replies = list(Comment.objects.get(children).values()[lower:upper])
    #     replies_size = len(Comment.objects.get(children).all())
    #     max_size = True if upper >= replies_size else False
    #     # return JsonResponse({'data': replies, 'max':max_size}, safe=False)
    #     return redirect('post-detail', context={'data': replies, 'max':max_size})



  















class PostEditView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['body', 'image']
    template_name = 'social/post_edit.html'
   
    def get_success_url(self):
        pk = self.kwargs['pk']
        return reverse_lazy('post-detail', kwargs={'pk': pk})

    # def test_func(self):
    #     post = self.get_object()
    #     return self.request.user == post.author

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return self.request.user == post.author
        elif self.request.user == post.shared_user:
            return self.request.user == post.shared_user



class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    template_name = 'social/post_delete.html'
    success_url = reverse_lazy('post-list')
    

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author
        
    ## code to allow user who shared a post to delete that there post ... ran into problems
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return self.request.user == post.author
        elif self.request.user == post.shared_user:
            return self.request.user == post.shared_user
   

class CommentDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Comment
    template_name = 'social/comment_delete.html'

    def get_success_url(self):
        pk = self.kwargs['post_pk']
        return reverse_lazy('post-detail', kwargs={'pk': pk})

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author

class ReplyDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Comment
    template_name = 'social/reply_delete.html'

    def get_success_url(self):
        pk = self.kwargs['comment_pk']
        return reverse_lazy('view-comment-reply', kwargs={'pk': pk})

    def test_func(self):
        comment = self.get_object()
        return self.request.user == comment.author






















# class ProfileAddLike(LoginRequiredMixin, View):
#     def post(self, request, pk, *args, **kwargs):
#         post = Post.objects.get(pk=pk)

#         is_dislike = False

#         for dislike in post.dislikes.all():
#             if dislike == request.user:
#                 is_dislike = True
#                 break

#         if is_dislike:
#             post.dislikes.remove(request.user)

#         is_like = False

#         for like in post.likes.all():
#             if like == request.user:
#                 is_like = True
#                 break

#         if not is_like:
#             post.likes.add(request.user)
#             notification = Notification.objects.create(notification_type=1, from_user=request.user, to_user=post.author, post=post)

#         if is_like:
#             post.likes.remove(request.user)

#         next = request.POST.get('next', '/')
#         return HttpResponseRedirect(next)

# class ProfileAddDislike(LoginRequiredMixin, View):
#     def post(self, request, pk, *args, **kwargs):
#         post = Post.objects.get(pk=pk)

#         is_like = False

#         for like in post.likes.all():
#             if like == request.user:
#                 is_like = True
#                 break

#         if is_like:
#             post.likes.remove(request.user)

#         is_dislike = False

#         for dislike in post.dislikes.all():
#             if dislike == request.user:
#                 is_dislike = True
#                 break

#         if not is_dislike:
#             post.dislikes.add(request.user)

#         if is_dislike:
#             post.dislikes.remove(request.user)

#         next = request.POST.get('next', '/')
#         return HttpResponseRedirect(next)








class PostDetailAddLike(LoginRequiredMixin, View):
    def post(self, request, pk, *args, **kwargs):
        post = Post.objects.get(pk=pk)

        is_dislike = False

        for dislike in post.dislikes.all():
            if dislike == request.user:
                is_dislike = True
                break

        if is_dislike:
            post.dislikes.remove(request.user)

        is_like = False

        for like in post.likes.all():
            if like == request.user:
                is_like = True
                break

        if not is_like:
            post.likes.add(request.user)
            notification = Notification.objects.create(notification_type=1, from_user=request.user, to_user=post.author, post=post)

        if is_like:
            post.likes.remove(request.user)

        next = request.POST.get('next', '/')
        return HttpResponseRedirect(next)

class PostDetailAddDislike(LoginRequiredMixin, View):
    def post(self, request, pk, *args, **kwargs):
        post = Post.objects.get(pk=pk)

        is_like = False

        for like in post.likes.all():
            if like == request.user:
                is_like = True

                break

        if is_like:
            post.likes.remove(request.user)

        is_dislike = False

        for dislike in post.dislikes.all():
            if dislike == request.user:
                is_dislike = True
                break

        if not is_dislike:
            post.dislikes.add(request.user)

        if is_dislike:
            post.dislikes.remove(request.user)

        next = request.POST.get('next', '/')

        return HttpResponseRedirect(next)

class AddLike(LoginRequiredMixin, View):
    def post(self, request, id, *args, **kwargs):
        post = Post.objects.get(id=id)
        user=request.user
        # is_dislike = False
        Likes=False
        Dislikes=False
        if request.method=="POST":
            post_id=request.POST['post_id']
            get_post=get_object_or_404(Post, id=post_id)
            # profile = UserProfile.objects.get(user=user)

            if user in get_post.likes.all():
                get_post.likes.remove(user)
                Likes=False
                # get_video.save()
            elif user in get_post.dislikes.all():                                                      
                get_post.dislikes.remove(user) 
                Dislikes=False  
                # get_video.save()                                          
                get_post.likes.add(user)  
                Likes=True  
                # get_video.save()

            else:
                get_post.likes.add(user)
                Likes=True
                notification = Notification.objects.create(notification_type=1, from_user=user, to_user=post.author, post=post)
                # get_video.save()


            data={
                "post_id":post_id,
                "liked":Likes,
                "likes_count":get_post.likes.all().count(),
                "disliked":Dislikes,
                "dislikes_count":get_post.dislikes.all().count()
            }

            return JsonResponse(data, safe=False)
        return redirect(reverse("post-list"), args=[str(id)])


class AddDislike(LoginRequiredMixin, View):
    def post(self, request, id, *args, **kwargs):
        post = Post.objects.get(id=id)

        user=request.user
        Dislikes=False
        Likes=False
        if request.method == "POST":
            post_id=request.POST['post_id']
            # print("printing ajax id", video_id)
            post=get_object_or_404(Post, id=post_id)

            if user in post.dislikes.all():
              post.dislikes.remove(user)
              Dislikes = False
              # watch.save()

            elif user in post.likes.all():
              post.likes.remove(user)
              Likes=False
              # watch.save()
              post.dislikes.add(user)                       
              Dislikes=True  
              # watch.save()
                
            else:                                                                               
              post.dislikes.add(user)                                                            
              Dislikes=True  
              # watch.save()


            data={   
                # "post_id":post_id,        
                "liked":Likes,
                "likes_count":post.likes.all().count(),         
                "disliked":Dislikes,
                "dislikes_count":post.dislikes.all().count()
            }
          
            return JsonResponse(data, safe=False)
        return redirect(reverse("post-list"), args=[str(id)])



# class ProfileAddLike(LoginRequiredMixin, View):
#     def post(self, request, pk, *args, **kwargs):
#         post = Post.objects.get(pk=pk)

#         is_dislike = False

#         for dislike in post.dislikes.all():
#             if dislike == request.user:
#                 is_dislike = True
#                 break

#         if is_dislike:
#             post.dislikes.remove(request.user)

#         is_like = False

#         for like in post.likes.all():
#             if like == request.user:
#                 is_like = True
#                 break

#         if not is_like:
#             post.likes.add(request.user)
#             notification = Notification.objects.create(notification_type=1, from_user=request.user, to_user=post.author, post=post)

#         if is_like:
#             post.likes.remove(request.user)

#         next = request.POST.get('next', '/')
#         return HttpResponseRedirect(next)

# class ProfileAddDislike(LoginRequiredMixin, View):
#     def post(self, request, pk, *args, **kwargs):
#         post = Post.objects.get(pk=pk)

#         is_like = False

#         for like in post.likes.all():
#             if like == request.user:
#                 is_like = True

#                 break

#         if is_like:
#             post.likes.remove(request.user)

#         is_dislike = False

#         for dislike in post.dislikes.all():
#             if dislike == request.user:
#                 is_dislike = True
#                 break

#         if not is_dislike:
#             post.dislikes.add(request.user)

#         if is_dislike:
#             post.dislikes.remove(request.user)

#         next = request.POST.get('next', '/')

#         return HttpResponseRedirect(next)


class ProfileAddLike(LoginRequiredMixin, View):
    def post(self, request, id, pk, *args, **kwargs):
        post = Post.objects.get(id=id)
        user=request.user
        profile = UserProfile.objects.get(pk=pk)

        # user_profile = profile.user
        # is_dislike = False
        Likes=False
        Dislikes=False
        if request.method=="POST":
            post_id=request.POST['post_id']
            get_post=get_object_or_404(Post, id=post_id)
            # profile = UserProfile.objects.get(user=user)

            if user in get_post.likes.all():
                get_post.likes.remove(user)
                Likes=False
                # get_video.save()
            elif user in get_post.dislikes.all():                                                      
                get_post.dislikes.remove(user) 
                Dislikes=False  
                # get_video.save()                                          
                get_post.likes.add(user)  
                Likes=True  
                # get_video.save()

            else:
                get_post.likes.add(user)
                Likes=True
                notification = Notification.objects.create(notification_type=1, from_user=user, to_user=post.author, post=post)
                # get_video.save()


            data={
                # "profile": profile,
                "post_id":post_id,
                "liked":Likes,
                "likes_count":get_post.likes.all().count(),
                "disliked":Dislikes,
                "dislikes_count":get_post.dislikes.all().count()
            }

        
      


            return JsonResponse(data, safe=False)
        return redirect(reverse('registration/show_profile_page', pk=profile.pk, args=[str(id)]))
        # return redirect(reverse("show_profile_page"), args=[str(id)])
        # return redirect('show_profile_page', pk=profile_pk)

        # return render(request, 'registration/user_profile.html')


class ProfileAddDislike(LoginRequiredMixin, View):
    def post(self, request, id, pk, *args, **kwargs):
        post = Post.objects.get(id=id)
        user=request.user
        profile = UserProfile.objects.get(pk=pk)
        # profile = UserProfile.objects.get(pk=pk)
        # user_profile = profile.user
        Dislikes=False
        Likes=False
        if request.method == "POST":
            post_id=request.POST['post_id']
            # print("printing ajax id", video_id)
            post=get_object_or_404(Post, id=post_id)

            if user in post.dislikes.all():
              post.dislikes.remove(user)
              Dislikes = False
              # watch.save()

            elif user in post.likes.all():
              post.likes.remove(user)
              Likes=False
              # watch.save()
              post.dislikes.add(user)                       
              Dislikes=True  
              # watch.save()
                
            else:                                                                               
              post.dislikes.add(user)                                                            
              Dislikes=True  
              # watch.save()


            data={   
                "post_id":post_id, 
                # "profile": profile,       
                "liked":Likes,
                "likes_count":post.likes.all().count(),         
                "disliked":Dislikes,
                "dislikes_count":post.dislikes.all().count()
            }
          
            return JsonResponse(data, safe=False)
        return redirect(reverse('registration/show_profile_page', pk=profile.pk, args=[str(id)]))
        # return redirect(reverse("show_profile_page"), args=[str(id)])
        # return render(request, 'registration/user_profile.html')



class SharedProfileAddLike(LoginRequiredMixin, View):
    def post(self, request, id, pk, *args, **kwargs):
        post = Post.objects.get(id=id)
        user=request.user
        profile = UserProfile.objects.get(pk=pk)

        # user_profile = profile.user
        # is_dislike = False
        Likes=False
        Dislikes=False
        if request.method=="POST":
            post_id=request.POST['post_id']
            get_post=get_object_or_404(Post, id=post_id)
            # profile = UserProfile.objects.get(user=user)

            if user in get_post.likes.all():
                get_post.likes.remove(user)
                Likes=False
                # get_video.save()
            elif user in get_post.dislikes.all():                                                      
                get_post.dislikes.remove(user) 
                Dislikes=False  
                # get_video.save()                                          
                get_post.likes.add(user)  
                Likes=True  
                # get_video.save()

            else:
                get_post.likes.add(user)
                Likes=True
                notification = Notification.objects.create(notification_type=1, from_user=user, to_user=post.author, post=post)
                # get_video.save()


            data={
                # "profile": profile,
                "post_id":post_id,
                "liked":Likes,
                "likes_count":get_post.likes.all().count(),
                "disliked":Dislikes,
                "dislikes_count":get_post.dislikes.all().count()
            }

        
      


            return JsonResponse(data, safe=False)
        return redirect(reverse('registration/show_shared_profile_page', pk=profile.pk, args=[str(id)]))
        # return redirect(reverse("show_profile_page"), args=[str(id)])
        # return redirect('show_profile_page', pk=profile_pk)

        # return render(request, 'registration/user_profile.html')


class SharedProfileAddDislike(LoginRequiredMixin, View):
    def post(self, request, id, pk, *args, **kwargs):
        post = Post.objects.get(id=id)
        user=request.user
        profile = UserProfile.objects.get(pk=pk)
        # profile = UserProfile.objects.get(pk=pk)
        # user_profile = profile.user
        Dislikes=False
        Likes=False
        if request.method == "POST":
            post_id=request.POST['post_id']
            # print("printing ajax id", video_id)
            post=get_object_or_404(Post, id=post_id)

            if user in post.dislikes.all():
              post.dislikes.remove(user)
              Dislikes = False
              # watch.save()

            elif user in post.likes.all():
              post.likes.remove(user)
              Likes=False
              # watch.save()
              post.dislikes.add(user)                       
              Dislikes=True  
              # watch.save()
                
            else:                                                                               
              post.dislikes.add(user)                                                            
              Dislikes=True  
              # watch.save()


            data={   
                "post_id":post_id, 
                # "profile": profile,       
                "liked":Likes,
                "likes_count":post.likes.all().count(),         
                "disliked":Dislikes,
                "dislikes_count":post.dislikes.all().count()
            }
          
            return JsonResponse(data, safe=False)
        return redirect(reverse('registration/show_shared_profile_page', pk=profile.pk, args=[str(id)]))
        # return redirect(reverse("show_profile_page"), args=[str(id)])
        # return render(request, 'registration/user_profile.html')







# class PostDetailAddLike(LoginRequiredMixin, View):
#     def post(self, request, id, *args, **kwargs):
#         post = Post.objects.get(id=id)
#         user=request.user
#         # is_dislike = False
#         Likes=False
#         Dislikes=False
#         if request.method=="POST":
#             post_id=request.POST['post_id']
#             get_post=get_object_or_404(Post, id=post_id)
#             # profile = UserProfile.objects.get(user=user)

#             if user in get_post.likes.all():
#                 get_post.likes.remove(user)
#                 Likes=False
#                 # get_video.save()
#             elif user in get_post.dislikes.all():                                                      
#                 get_post.dislikes.remove(user) 
#                 Dislikes=False  
#                 # get_video.save()                                          
#                 get_post.likes.add(user)  
#                 Likes=True  
#                 # get_video.save()

#             else:
#                 get_post.likes.add(user)
#                 Likes=True
#                 # get_video.save()

#             data={
#                 # "post_id":post_id,
#                 "liked":Likes,
#                 "likes_count":get_post.likes.all().count(),
#                 "disliked":Dislikes,
#                 "dislikes_count":get_post.dislikes.all().count()
#             }

#             return JsonResponse(data, safe=False)
#         return redirect(reverse("post-detail"), args=[str(id)])


# class PostDetailAddDislike(LoginRequiredMixin, View):
#     def post(self, request, id, *args, **kwargs):
#         post = Post.objects.get(id=id)

#         user=request.user
#         Dislikes=False
#         Likes=False
#         if request.method == "POST":
#             post_id=request.POST['post_id']
#             # print("printing ajax id", video_id)
#             post=get_object_or_404(Post, id=post_id)

#             if user in post.dislikes.all():
#               post.dislikes.remove(user)
#               Dislikes = False
#               # watch.save()

#             elif user in post.likes.all():
#               post.likes.remove(user)
#               Likes=False
#               # watch.save()
#               post.dislikes.add(user)                       
#               Dislikes=True  
#               # watch.save()
                
#             else:                                                                               
#               post.dislikes.add(user)                                                            
#               Dislikes=True  
#               # watch.save()


#             data={   
#                 # "post_id":post_id,        
#                 "liked":Likes,
#                 "likes_count":post.likes.all().count(),         
#                 "disliked":Dislikes,
#                 "dislikes_count":post.dislikes.all().count()
#             }
          
#             return JsonResponse(data, safe=False)
#         return redirect(reverse("post-detail"), args=[str(id)])



# def like_unlike_post(request):
#     username = request.user
#     if request.method == 'POST':
#         post_id = request.POST.get('post_id')
#         post_obj = Post.objects.get(id=post_id)
#         profile = User.objects.get(username=username)

#         if profile in post_obj.liked.all():
#             post_obj.liked.remove(profile)
#         else:
#             post_obj.liked.add(profile)

#         like, created = Like.objects.get_or_create(user=profile, post_id=post_id)

#         if not created:
#             if like.value=='Like':
#                 like.value='Unlike'
#             else:
#                 like.value='Like'
#         else:
#             like.value='Like'

#             post_obj.save()
#             like.save()

#         data = {
#             'value': like.value,
#             'liked': post_obj.liked.all().count()
#         }

#         return JsonResponse(data, safe=False)
#     return redirect(reverse("post-list"))

  
















class AddCommentLike(LoginRequiredMixin, View):
    def post(self, request, pk, *args, **kwargs):
        # post = Post.objects.get(id=id)
        # post = Post.objects.get(pk=pk)
        comment = Comment.objects.get(pk=pk)
        user=request.user
        # is_dislike = False
        Likes=False
        Dislikes=False
        if request.method=="POST":
            comment_pk=request.POST['comment_pk']
            get_comment=get_object_or_404(Comment, pk=comment_pk)
            # profile = UserProfile.objects.get(user=user)

            if user in get_comment.likes.all():
                get_comment.likes.remove(user)
                Likes=False
                # get_video.save()
            elif user in get_comment.dislikes.all():                                                      
                get_comment.dislikes.remove(user) 
                Dislikes=False  
                # get_video.save()                                          
                get_comment.likes.add(user)  
                Likes=True  
                # get_video.save()

            else:
                get_comment.likes.add(user)
                Likes=True
                notification = Notification.objects.create(notification_type=1, from_user=user, to_user=comment.author, comment=comment)
                # get_video.save()


            data={
                # "post": post,
                "comment_pk":comment_pk,
                "liked":Likes,
                "likes_count":get_comment.likes.all().count(),
                "disliked":Dislikes,
                "dislikes_count":get_comment.dislikes.all().count()
            }

            return JsonResponse(data, safe=False)
        return redirect(reverse("post-detail"))


class AddCommentDislike(LoginRequiredMixin, View):
    def post(self, request, pk, *args, **kwargs):
        # post = Post.objects.get(id=id)
        comment = Comment.objects.get(pk=pk)

        user=request.user
        Dislikes=False
        Likes=False
        if request.method == "POST":
            comment_pk=request.POST['comment_pk']
            # print("printing ajax id", video_id)
            get_comment=get_object_or_404(Comment, pk=comment_pk)

            if user in  get_comment.dislikes.all():
              get_comment.dislikes.remove(user)
              Dislikes = False
              # watch.save()

            elif user in get_comment.likes.all():
              get_comment.likes.remove(user)
              Likes=False
              # watch.save()
              get_comment.dislikes.add(user)                       
              Dislikes=True  
              # watch.save()
                
            else:                                                                               
              get_comment.dislikes.add(user)                                                            
              Dislikes=True  
              # watch.save()


            data={   
                # "post_id":post_id,        
                "liked":Likes,
                "likes_count": get_comment.likes.all().count(),         
                "disliked":Dislikes,
                "dislikes_count": get_comment.dislikes.all().count()
            }
          
            return JsonResponse(data, safe=False)
        return redirect(reverse("post-detail"))









# class AddCommentLike(LoginRequiredMixin, View):
#     def post(self, request, pk, *args, **kwargs):
#         comment = Comment.objects.get(pk=pk)

#         is_dislike = False

#         for dislike in comment.dislikes.all():
#             if dislike == request.user:
#                 is_dislike = True
#                 break

#         if is_dislike:
#             comment.dislikes.remove(request.user)

#         is_like = False

#         for like in comment.likes.all():
#             if like == request.user:
#                 is_like = True
#                 break

#         if not is_like:
#             comment.likes.add(request.user)
#             notification = Notification.objects.create(notification_type=1, from_user=request.user, to_user=comment.author, comment=comment)

#         if is_like:
#             comment.likes.remove(request.user)

#         next = request.POST.get('next', '/')
#         return HttpResponseRedirect(next)

# class AddCommentDislike(LoginRequiredMixin, View):
#     def post(self, request, pk, *args, **kwargs):
#         comment = Comment.objects.get(pk=pk)

#         is_like = False

#         for like in comment.likes.all():
#             if like == request.user:
#                 is_like = True
#                 break

#         if is_like:
#             comment.likes.remove(request.user)

#         is_dislike = False

#         for dislike in comment.dislikes.all():
#             if dislike == request.user:
#                 is_dislike = True
#                 break

#         if not is_dislike:
#             comment.dislikes.add(request.user)

#         if is_dislike:
#             comment.dislikes.remove(request.user)

#         next = request.POST.get('next', '/')
#         return HttpResponseRedirect(next)

class UserSearch(View):
    def get(self, request, *args, **kwargs):
        query = self.request.GET.get('query')
        profile_list = UserProfile.objects.filter(
            Q(user__username__icontains=query)
        )

        context = {
            'profile_list': profile_list,
        }

        return render(request, 'social/search.html', context)








class NotificationView(View):
    # def show_notifications(takes_context=True):
    def get(self, request, *args, **kwargs):
    # def get(self, request, pk, *args, **kwargs):
        request_user = request.user
        # notification = Notification.objects.filter(to_user=request_user).exclude(user_has_seen=True).count()
        p = Paginator(Notification.objects.filter(to_user=request_user).exclude(user_has_seen=True).order_by('-date'), 10)
        # notification_count = notification.count()
        page = request.GET.get('page')
        notifications = p.get_page(page)
        notificationss = Notification.notification_type
        # context = {'notifications': notifications, 'notification_count':notification_count}
        context = {'notifications': notifications}

        
        if notificationss == 1:
            def get(self, request, notification_pk, post_pk, object_pk, *args, **kwargs):
                notification = Notification.objects.get(pk=notification_pk)
                post = Post.objects.get(pk=post_pk)

                notification.user_has_seen = True
                notification.save()

                return redirect('post-detail', pk=post_pk)

        if notificationss == 2:
            def get(self, request, notification_pk, profile_pk, *args, **kwargs):
                notification = Notification.objects.get(pk=notification_pk)
                profile = UserProfile.objects.get(pk=profile_pk)

                notification.user_has_seen = True
                notification.save()

                return redirect('show_profile_page', pk=profile_pk)

        if notificationss == 3:
            def get(self, request, notification_pk, object_pk, *args, **kwargs):
                notification = Notification.objects.get(pk=notification_pk)
                thread = ThreadModel.objects.get(pk=object_pk)

                notification.user_has_seen = True
                notification.save()

                return redirect('thread', pk=object_pk)

        if notificationss == 4:
            def delete(self, request, notification_pk, *args, **kwargs):
                notification = Notification.objects.get(pk=notification_pk)

                notification.user_has_seen = True
                notification.save()

                return HttpResponse('Success', content_type='text/plain')
        
        return render(request, 'social/all_notifications.html', context)
  

            
    

       
   

       
 

        
  

    
   
        

       



    # register = template.Library()

    # @register.inclusion_tag('social/show_notifications.html', takes_context=True)
    # def show_notifications(context):
    #     request_user = context['request'].user
    #     notifications = Notification.objects.filter(to_user=request_user).exclude(user_has_seen=True).order_by('-date')
    #     return {'notifications': notifications}





    # def get(self, request, notification_pk, post_pk, object_pk, *args, **kwargs):
    #     request_user = context['request'].user
    #     notification = Notification.objects.filter(to_user=request_user).exclude(user_has_seen=True).order_by('-date')
        
    #     if notification_type == 1:
    #         notification = Notification.objects.get(pk=notification_pk)
    #         post = Post.objects.get(pk=post_pk)

    #         notification.user_has_seen = True
    #         notification.save()

    #         return redirect('post-detail', pk=post_pk)

    #     elif notification_type == 2:
    #         notification = Notification.objects.get(pk=notification_pk)
    #         profile = UserProfile.objects.get(pk=profile_pk)

    #         notification.user_has_seen = True
    #         notification.save()

    #         return redirect('show_profile_page', pk=profile_pk)

    #     elif notification_type == 3:
    #         notification = Notification.objects.get(pk=notification_pk)
    #         thread = ThreadModel.objects.get(pk=object_pk)

    #         notification.user_has_seen = True
    #         notification.save()

    #         return redirect('thread', pk=object_pk)

    #     elif notification_type == 4:
    #         notification = Notification.objects.get(pk=notification_pk)

    #         notification.user_has_seen = True
    #         notification.save()

    #         return HttpResponse('Success', content_type='text/plain')

      

        





    





class PostNotification(View):
    def get(self, request, notification_pk, post_pk, *args, **kwargs):
        notification = Notification.objects.get(pk=notification_pk)
        post = Post.objects.get(pk=post_pk)

        notification.user_has_seen = True
        notification.save()

        return redirect('post-detail', pk=post_pk)

class FollowNotification(View):
    def get(self, request, notification_pk, profile_pk, *args, **kwargs):
        notification = Notification.objects.get(pk=notification_pk)
        profile = UserProfile.objects.get(pk=profile_pk)

        notification.user_has_seen = True
        notification.save()

        return redirect('show_profile_page', pk=profile_pk)

class ThreadNotification(View):
    def get(self, request, notification_pk, object_pk, *args, **kwargs):
        notification = Notification.objects.get(pk=notification_pk)
        thread = ThreadModel.objects.get(pk=object_pk)

        notification.user_has_seen = True
        notification.save()

        return redirect('thread', pk=object_pk)

class RemoveNotification(View):
    def delete(self, request, notification_pk, *args, **kwargs):
        notification = Notification.objects.get(pk=notification_pk)

        notification.user_has_seen = True
        notification.save()

        return HttpResponse('Success', content_type='text/plain')

class ListThreads(View):
    def get(self, request, *args, **kwargs):
        threads = ThreadModel.objects.filter(Q(user=request.user) | Q(receiver=request.user))

        context = {
            'threads': threads, 
        }

        return render(request, 'social/inbox.html', context)

class CreateThread(View):
    def get(self, request, *args, **kwargs):
        form = ThreadForm()

        context = {
            'form': form
        }

        return render(request, 'social/create_thread.html', context)

    def post(self, request, *args, **kwargs):
        form = ThreadForm(request.POST)

        username = request.POST.get('username')

        try:
            receiver = User.objects.get(username=username)
            if ThreadModel.objects.filter(user=request.user, receiver=receiver).exists():
                thread = ThreadModel.objects.filter(user=request.user, receiver=receiver)[0]
                return redirect('thread', pk=thread.pk)
            elif ThreadModel.objects.filter(user=receiver, receiver=request.user).exists():
                thread = ThreadModel.objects.filter(user=receiver, receiver=request.user)[0]
                return redirect('thread', pk=thread.pk)

            if form.is_valid():
                thread = ThreadModel(
                    user=request.user,
                    receiver=receiver
                )
                thread.save()

                return redirect('thread', pk=thread.pk)
        except:
            messages.error(request, 'Invalid username')
            return redirect('create-thread')

class ThreadView(View):
    def get(self, request, pk, *args, **kwargs):
        form = MessageForm()
        thread = ThreadModel.objects.get(pk=pk)
        # message_list = MessageModel.objects.filter(thread__pk__contains=pk)
        p = Paginator( MessageModel.objects.filter(thread__pk__contains=pk), 10)
        page = request.GET.get('page')
        message_list = p.get_page(page)
        context = {
            'thread': thread,
            'form': form,
            'message_list': message_list
        }

        return render(request, 'social/thread.html', context)

class CreateMessage(View):
    def post(self, request, pk, *args, **kwargs):
        form = MessageForm(request.POST, request.FILES)
        thread = ThreadModel.objects.get(pk=pk)
        if thread.receiver == request.user:
            receiver = thread.user
        else:
            receiver = thread.receiver

        if form.is_valid():
            message = form.save(commit=False)
            message.thread = thread
            message.sender_user = request.user
            message.receiver_user = receiver
            message.save()

        notification = Notification.objects.create(
            notification_type=4,
            from_user=request.user,
            to_user=receiver,
            thread=thread
        )
        return redirect('thread', pk=pk)


class Explore(View):
    def get(self, request, *args, **kwargs):
        explore_form = ExploreForm()
        query = self.request.GET.get('query')
        tag = Tag.objects.filter(name=query).first()

        if tag:
            # posts = Post.objects.filter(tags__in=[tag])
            p = Paginator(Post.objects.filter(tags__in=[tag]), 5)
            page = request.GET.get('page')
            posts = p.get_page(page)

        else:
            # posts = Post.objects.all()
            p = Paginator(Post.objects.all(), 5)
            page = request.GET.get('page')
            posts = p.get_page(page)

        context = {
            'tag': tag,
            'posts': posts,
            'explore_form': explore_form,
        }

        return render(request, 'social/explore.html', context)

    def post(self, request, *args, **kwargs):
        explore_form = ExploreForm(request.POST)
        if explore_form.is_valid():
            query = explore_form.cleaned_data['query']
            tag = Tag.objects.filter(name=query).first()

            posts = None
            if tag:
                posts = Post.objects.filter(tags__in=[tag])

            if posts:
                context = {
                    'tag': tag,
                    'posts': posts,
                }
            else:
                context = {
                    'tag': tag,
                }

            return HttpResponseRedirect(f'/social/explore?query={query}')
        return HttpResponseRedirect('/social/explore')
    # def get(self, request, *args, **kwargs):
    #     explore_form = ExploreForm()
    #     query = self.request.GET.get('query')
    #     tag = Tag.objects.filter(name=query).first()

    #     if tag:
    #         posts = Post.objects.filter(tags__in=[tag])
    #     else:
    #         posts = Post.objects.all()

    #     context = {
    #         'tag': tag,
    #         'posts': posts,
    #         'explore_form': explore_form,
    #     }

    #     return render(request, 'social/explore.html', context)

    # def post(self, request, *args, **kwargs):
    #     explore_form = ExploreForm(request.POST)
    #     if explore_form.is_valid():
    #         query = explore_form.cleaned_data['query']
    #         tag = Tag.objects.filter(name=query).first()

    #         posts = None
    #         if tag:
    #             posts = Post.objects.filter(tags__in=[tag])

    #         if posts:
    #             context = {
    #                 'tag': tag,
    #                 'posts': posts,
    #             }
    #         else:
    #             context = {
    #                 'tag': tag,
    #             }

    #         return HttpResponseRedirect(f'/social/explore?query={query}')
    #     return HttpResponseRedirect('/social/explore')

