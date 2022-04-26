from django.shortcuts import render, get_object_or_404, redirect													
from django.views import generic 							
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm, PasswordResetForm                      
from django.contrib.auth.views import PasswordChangeView                                                                      
from django.urls import reverse_lazy                       
from .forms import SignUpForm, EditProfileForm, PasswordChangingForm, ProfilePageForm
# get_state_strings, get_city_strings         
from django.views.generic import DetailView, CreateView, DeleteView        															 
from .models import UserProfile, User, State, City
# , Branch
from social.models import Post 
# Follow                                                                                                                                                                         
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.http import HttpResponse
from django.utils.encoding import force_bytes, force_str
from members.tokens import account_activation_token
from django.core import mail
from django.views.generic.list import ListView
# from django.contrib.auth.models import User
# from members.models import User 

from django.utils.encoding import force_text
from django.contrib.auth import login
from django.core.mail import send_mail, BadHeaderError
from django.template.loader import render_to_string
from django.db.models.query_utils import Q
from django.contrib.auth.tokens import default_token_generator
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from django.core.paginator import Paginator   
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy, reverse
import json

def password_success(request):                                                  
	return render(request, 'registration/password_success.html', {})  

class PasswordsChangeView(PasswordChangeView):                                                                           
	form_class = PasswordChangingForm 										    
	success_url = reverse_lazy('password_success')     

class UserDeleteView(DeleteView):
	model = User
	success_url = reverse_lazy('login')

def register(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()
            current_site = get_current_site(request)
            mail_subject = 'Activate your blog account.'
            message = render_to_string(
                'registration/email_template.html',
                {
                    'user': user,
                    'domain': current_site.domain,
                    'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                    'token': account_activation_token.make_token(user),
                }
            )
            to_email = form.cleaned_data.get('email')
            email = mail.EmailMessage(mail_subject, message, to=[to_email])
            email.send()
            return render(request, 'registration/confirm_email.html')  
            # return HttpResponse('Please confirm your email address to complete the registration')
    else:
        form = SignUpForm()
    return render(request, 'registration/register.html', {'form': form})

def load_citys(request):
    state_id = request.GET.get('state')
    citys = City.objects.filter(state_id=state_id).order_by('name')
    return render(request, 'registration/city_dropdown_list_options.html', {'citys': citys})

# def load_branches(request):
#     college_id = request.GET.get('college')
#     branches = Branch.objects.filter(college_id=college_id).order_by('name')
#     return render(request, 'registration/branch_dropdown_list_options.html', {'branches': branches})

# def register(request):
#     if request.method == 'POST':
#         form = SignUpForm(request.POST)
#         if form.is_valid():
#             user = form.save(commit=False)
#             user.is_active = False
#             user.save()
#             current_site = get_current_site(request)
#             mail_subject = 'Activate your blog account.'
#             message = render_to_string(
#                 'registration/email_template.html',
#                 {
#                     'user': user,
#                     'domain': current_site.domain,
#                     'uid': urlsafe_base64_encode(force_bytes(user.pk)),
#                     'token': account_activation_token.make_token(user),
#                 }
#             )
#             to_email = form.cleaned_data.get('email')
#             email = mail.EmailMessage(mail_subject, message, to=[to_email])
#             email.send()
#             return render(request, 'registration/confirm_email.html')  
#             # return HttpResponse('Please confirm your email address to complete the registration')
#     else:
#         form = SignUpForm()
#         country_id = request.GET.get('country_id')
#         cities = City.objects.filter(country_id=country_id).all()
#         context = {
#             'form': form,
#             'cities': cities,
#         }
#     return render(request, 'registration/register.html', context)
#     # return JsonResponse(list(cities.values('id', 'name')), safe=False)

# # AJAX
# def load_cities(request):
#     country_id = request.GET.get('country_id')
#     cities = City.objects.filter(country_id=country_id).all()
#     return render(request, 'persons/city_dropdown_list_options.html', {'cities': cities})
#     # return JsonResponse(list(cities.values('id', 'name')), safe=False)


# def register(request):
#     if request.method == 'POST':
#         form = SignUpForm(request.POST)
       
#         if form.is_valid():
#             user = form.save(commit=False)
#             user.is_active = False
#             user.save()
#             current_site = get_current_site(request)
#             mail_subject = 'Activate your blog account.'
#             message = render_to_string(
#                 'registration/email_template.html',
#                 {
#                     'user': user,
#                     'domain': current_site.domain,
#                     'uid': urlsafe_base64_encode(force_bytes(user.pk)),
#                     'token': account_activation_token.make_token(user),
#                 }
#             )
#             to_email = form.cleaned_data.get('email')
#             email = mail.EmailMessage(mail_subject, message, to=[to_email])
#             email.send()
#             return render(request, 'registration/confirm_email.html')  
#             # return HttpResponse('Please confirm your email address to complete the registration')
#     else:
#         form = SignUpForm()
#         state_strings = get_state_strings()
#         city_strings = get_city_strings()
#         json_state_strings = json.dumps(state_strings)
#         json_city_strings = json.dumps(city_strings)
#         # context['json_state_strings'] = json_state_strings
#         context = {
#         	'json_state_strings': json_state_strings,
#         	'json_city_strings': json_city_strings,
#         	'form': form,
#         }
#     return render(request, 'registration/register.html', context)
 

# class RegisterView(generic.CreateView):
# 	def register(request):
# 	    if request.method == 'POST':
# 	        form = SignUpForm(request.POST)
# 	        if form.is_valid():
# 	            user = form.save(commit=False)
# 	            user.is_active = False
# 	            user.save()
# 	            current_site = get_current_site(request)
# 	            mail_subject = 'Activate your blog account.'
# 	            message = render_to_string(
# 	                'registration/email_template.html',
# 	                {
# 	                    'user': user,
# 	                    'domain': current_site.domain,
# 	                    'uid': urlsafe_base64_encode(force_bytes(user.pk)),
# 	                    'token': account_activation_token.make_token(user),
# 	                }
# 	            )
# 	            to_email = form.cleaned_data.get('email')
# 	            email = mail.EmailMessage(mail_subject, message, to=[to_email])
# 	            email.send()
# 	            return render(request, 'registration/confirm_email.html')  
# 	            # return HttpResponse('Please confirm your email address to complete the registration')
# 	    else:
# 	        form = SignUpForm()
# 	    return render(request, 'registration/register.html', {'form': form})


	# def load_states(request):
	#     country_id = request.GET.get('country')
	#     states = State.objects.filter(country_id=country_id).order_by('name')
	#     return render(request, 'registration/state_dropdown_list_options.html', {'states': states})
 




def activate(request, uidb64, token):
	try:
		uid = force_text(urlsafe_base64_decode(uidb64))
		user = User.objects.get(pk=uid)
	except(TypeError, ValueError, OverflowError, User.DoesNotExist):
		user = None
	if user is not None and account_activation_token.check_token(user, token):
		user.is_active = True
		user.save()
		login(request, user)
		# return HttpResponse('Thank you for your email confirmation. Now you can login account.')
		return render(request, 'registration/successful_registration.html') 
	else:
		return HttpResponse('Activation link is invalid!')    

class UserEditView(generic.UpdateView):                  							
	model = UserProfile
	# date_joined = User.date_joined
	form_class = EditProfileForm	
	# fields = ['username', 'email', 'password1', 'password2']												    
	template_name = 'registration/edit_profile.html'                                          
	# success_url = reverse_lazy('home')        
	# date_joined = User.objects.all()                                      

	def get_object(self):															
		return self.request.user     

	def get_success_url(self):
		pk = self.kwargs['pk']
		return reverse_lazy('show_profile_page', kwargs={'pk': pk})

	def test_func(self):
		profile = self.get_object()
		return self.request.user == profile.user


class ShowProfilePageView(DetailView, ListView):    
	def get(self, request, pk, *args, **kwargs):
		# date_joined = User.objects.filter(date_joined=date_joined)
		profile = UserProfile.objects.get(pk=pk)
		# date_join = User.objects.get_field(date_joined)
		user = profile.user
		# following_count = Follow.objects.filter(follower=user).count()
		# followers_count = Follow.objects.filter(following=user).count()
		# follow_status = Follow.objects.filter(following=user, follower=request.user).exists()
		# userProfile = UserProfile.objects.get(user=user)
		# posts = Post.objects.filter(author=user)
		# sharedposts = Post.objects.filter(shared_user=user)
		followers = profile.followers.all()
		followings = profile.followings.all()
		p = Paginator(Post.objects.filter(author=user), 10)
		page = request.GET.get('page')
		posts = p.get_page(page)

		# p = Paginator(Post.objects.filter(author=user), 3)
		# page = request.GET.get('page')
		# posts = p.get_page(page)

		
		if len(followers) == 0:
			is_following = False

		for follower in followers:
			if follower == request.user:
				is_following = True
				break
			else:
				is_following = False

		number_of_followers = len(followers)



		# if len(followings) == 0:
		# 	is_follower = False

		# for following in followings:
		# 	if following == request.user:
		# 		is_follower = True
		# 		break
		# 	else:
		# 		is_follower = False

		number_of_followings = len(followings)

			
		context = {
			'user': user,
			# 'author': userProfile,
			'profile': profile,
			# 'date_join': date_join,
			# 'picture': picture,
			'posts': posts,
			# 'following_count':following_count,
			# 'followers_count':followers_count,
			# 'follow_status':follow_status,
			# 'sharedposts': sharedposts,
			'number_of_followers': number_of_followers,
			'is_following': is_following,
			'number_of_followings': number_of_followings,
			# 'is_follower': is_follower,
		}

		return render(request, 'registration/user_profile.html', context)


# class ShowProfilePageViewUsername(DetailView, ListView):    
# 	def get(self, request, pk, *args, **kwargs):
# 		profile = UserProfile.objects.get(pk=pk)
# 		user = profile.user
# 		# following_count = Follow.objects.filter(follower=user).count()
# 		# followers_count = Follow.objects.filter(following=user).count()
# 		# follow_status = Follow.objects.filter(following=user, follower=request.user).exists()
# 		# userProfile = UserProfile.objects.get(user=user)
# 		# posts = Post.objects.filter(author=user)
# 		# sharedposts = Post.objects.filter(shared_user=user)
# 		# followers = profile.followers.all()
# 		# followings = profile.followings.all()
# 		p = Paginator(Post.objects.filter(author=user), 5)
# 		page = request.GET.get('page')
# 		posts = p.get_page(page)
		
# 		# if len(followers) == 0:
# 		# 	is_following = False

# 		# for follower in followers:
# 		# 	if follower == request.user:
# 		# 		is_following = True
# 		# 		break
# 		# 	else:
# 		# 		is_following = False

# 		# number_of_followers = len(followers)



# 		# if len(followings) == 0:
# 		# 	is_follower = False

# 		# for following in followings:
# 		# 	if following == request.user:
# 		# 		is_follower = True
# 		# 		break
# 		# 	else:
# 		# 		is_follower = False

# 		# number_of_followings = len(followings)

			
# 		context = {
# 			'user': user,
# 			# 'author': userProfile,
# 			'profile': profile,
# 			# 'picture': picture,
# 			'posts': posts,
# 			# 'following_count':following_count,
# 			# 'followers_count':followers_count,
# 			# 'follow_status':follow_status,
# 			# 'sharedposts': sharedposts,
# 			# 'number_of_followers': number_of_followers,
# 			# 'is_following': is_following,
# 			# 'number_of_followings': number_of_followings,
# 			# 'is_follower': is_follower,
# 		}

# 		return render(request, 'registration/user_profile_username.html', context)



# def followToggle(request, author):
#     authorObj = UserProfile.objects.get(user=author)
#     currentUserObj = UserProfile.objects.get(user=request.user)
#     following = authorObj.following.all()

#     if author != currentUserObj.user:
#         if currentUserObj in following:
#             authorObj.following.remove(currentUserObj)
#         else:
#             authorObj.following.add(currentUserObj)

#     return HttpResponseRedirect(reverse('show_profile_page', args=[authorObj.user]))


# class ShowProfilePageView(DetailView):    
# 	def get(self, request, pk, *args, **kwargs):
# 		profile = UserProfile.objects.get(pk=pk)
# 		user = profile.user
# 		# posts = Post.objects.filter(author=user)
# 		# sharedposts = Post.objects.filter(shared_user=user)
# 		followers = profile.followers.all()
		
# 		if len(followers) == 0:
# 			is_following = False

# 		for follower in followers:
# 			if follower == request.user:
# 				is_following = True
# 				break
# 			else:
# 				is_following = False

# 		number_of_followers = len(followers)
			
# 		context = {
# 			'user': user,
# 			'profile': profile,
# 			# 'picture': picture,
# 			# 'posts': posts,
# 			# 'sharedposts': sharedposts,
# 			'number_of_followers': number_of_followers,
# 			'is_following': is_following,
# 		}

# 		return render(request, 'registration/user_profile.html', context)


# def ShowProfilePageWithPosts(request, pk):
# 	limit = request.GET.get('limit')
# 	start = request.GET.get('start')
# 	print(f"printing limit", limit)
# 	print(f"printing limit", start)
# 	profile = UserProfile.objects.get(pk=pk)
# 	user = profile.user
# 	# posts = Post.objects.filter(author=user)
# 	posts = Post.objects.filter(author=user)[int(start):int(limit) + int(start)]
# 	# sharedposts = Post.objects.filter(shared_user=user)[int(start):int(limit) + int(start)]
 
# 	context = {
# 		'user': user,
# 		'profile': profile,
# 		'post_list': posts,
# 		# 'sharedposts': sharedposts,
# 	}
   
# 	return render(request, 'registration/get_posts_for_profilepage.html', context)


class ShowSharedProfilePageView(DetailView):    
	def get(self, request, pk, *args, **kwargs):
		profile = UserProfile.objects.get(pk=pk)
		user = profile.user
		posts = Post.objects.filter(author=user)
		sharedposts = Post.objects.filter(shared_user=user)
		followers = profile.followers.all()
		followings = profile.followings.all()

		p = Paginator(Post.objects.filter(shared_user=user), 10)
		page = request.GET.get('page')
		sharedposts = p.get_page(page)

		if len(followers) == 0:
			is_following = False

		for follower in followers:
			if follower == request.user:
				is_following = True
				break
			else:
				is_following = False

		number_of_followers = len(followers)


		if len(followings) == 0:
			is_follower = False

		for following in followings:
			if following == request.user:
				is_follower = True
				break
			else:
				is_follower = False

		number_of_followings = len(followings)

		context = {
			'user': user,
			'profile': profile,
			# 'picture': picture,
			'posts': posts,
			'sharedposts': sharedposts,
			'number_of_followers': number_of_followers,
			'is_following': is_following,
			'number_of_followings': number_of_followings,
			'is_follower': is_follower,
		}

		return render(request, 'registration/get_sharedposts_for_profilepage.html', context)

class EditProfilePageView(generic.UpdateView):
	model = UserProfile
	fields = ['first_name', 'last_name', 'birth_date', 'location', 'bio', 'picture', 'website_url', 'facebook_url', 'twitter_url', 'instagram_url', 'pinterest_url']
	template_name = 'registration/edit_profile_page.html'

	def get_success_url(self):
		pk = self.kwargs['pk']
		return reverse_lazy('show_profile_page', kwargs={'pk': pk})

	def test_func(self):
		profile = self.get_object()
		return self.request.user == profile.user

	

	# model = UserProfile                                                                                                             
	# template_name = 'registration/edit_profile_page.html'
	# fields = ['first_name', 'last_name', 'bio', 'picture', 'website_url', 'facebook_url', 'twitter_url', 'instagram_url', 'pinterest_url']    
	# success_url = reverse_lazy('home')

# class CreateProfilePageView(CreateView):											
# 	model = UserProfile 
# 	form_class = ProfilePageForm                                                    
# 	template_name = 'registration/create_user_profile_page.html'
# 	# fields = '__all__'																 

# 	def form_valid(self, form):                                                    
# 		form.instance.user = self.request.user 
# 		return super().form_valid(form)





