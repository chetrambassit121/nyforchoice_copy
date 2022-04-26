from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm                                                                
# from django.contrib.auth.models import User                             
from django import forms 
from .models import UserProfile, User, State, City
# , Branch
from django.utils.safestring import mark_safe


# NY_STATE = 'Resident of the State of New York'
# OTHER = 'Outside the State of New York'

# NY_STATE_1 = 'Resident of New York City'
# NY_STATE_2 = 'Outside of New York City'
# OTHER_1 = 'Outside the State of New York'
# # B_2 = 'Outside New York City'

# STATE_CHOICES = [
#   (NY_STATE, NY_STATE),
#   (OTHER, OTHER),
# ]

# CITY_CHOICES = [
#   (NY_STATE_1, NY_STATE_1),
#   (NY_STATE_2, NY_STATE_2),
#   (OTHER_1, OTHER_1),
# ]             

# def get_state_strings():
#     state_strings = [
#         NY_STATE_1,
#         NY_STATE_2,
#     ]

#     return state_strings   

# def get_city_strings():
#     city_strings = [
#         OTHER_1,
#     ]

#     return city_strings

class SignUpForm(UserCreationForm):              
	                              

	email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))                              																						
	first_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))                                                                    
	last_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))  
	
	# country = forms.ChoiceField(choices=Country)
	# city = forms.ChoiceField(choices=City)

	# state = forms.CharField(max_length=100, widget=forms.TextInput(choices=STATE_CHOICES))
	# city = forms.CharField(max_length=100, widget=forms.TextInput(choices=CITY_CHOICES))

	# state = forms.ChoiceField(choices=STATE_CHOICES) # id_state
	# city = forms.ChoiceField(choices=CITY_CHOICES) # id_city

	class Meta:                                                                                         
		model = User                                                                                    
		# fields = ('username', 'first_name', 'last_name', 'email', 'state', 'city', 'college', 'branch', 'password1', 'password2')  
		fields = ('username', 'email', 'first_name', 'last_name', 'state', 'city', 'password1', 'password2')  


	

	def clean_email(self):
		email = self.cleaned_data['email']
		if User.objects.filter(email=email).exists():
		    raise forms.ValidationError('Email already used')
		return email

	def __init__(self, *args, **kwargs):                                    
		super(SignUpForm, self).__init__(*args, **kwargs)                    
		self.fields['username'].widget.attrs['class'] = 'form-control'
		# self.fields['email'].widget.attrs['class'] = 'form-control'              
		self.fields['password1'].widget.attrs['class'] = 'form-control'      
		self.fields['password2'].widget.attrs['class'] = 'form-control'   
		self.fields['city'].queryset = City.objects.none()
		# self.fields['branch'].queryset = Branch.objects.none()

		if 'state' in self.data:
			try:
				state_id = int(self.data.get('state'))
				self.fields['city'].queryset = City.objects.filter(state_id=state_id).order_by('name')
			except (ValueError, TypeError):
				pass  # invalid input from the client; ignore and fallback to empty City queryset
		elif self.instance.pk:
			self.fields['city'].queryset = self.instance.state.city_set.order_by('name')


		# if 'college' in self.data:
		# 	try:
		# 		college_id = int(self.data.get('college'))
		# 		self.fields['branch'].queryset = Branch.objects.filter(college_id=college_id).order_by('name')
		# 	except (ValueError, TypeError):
		# 		pass  # invalid input from the client; ignore and fallback to empty City queryset
		# elif self.instance.pk:
		# 	self.fields['branch'].queryset = self.instance.college.branch_set.order_by('name')






# class SignUpForm(UserCreationForm):                                                                                 
# 	email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))                              																						
# 	first_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))                                                                    
# 	last_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))  
# 	country = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))                                                                    
# 	state = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))                                                                    


# 	class Meta:                                                                                         
# 		model = User                                                                                    
# 		fields = ('username', 'first_name', 'last_name', 'country', 'state', 'email', 'password1', 'password2')  

# 	def clean_email(self):
# 		email = self.cleaned_data['email']
# 		if User.objects.filter(email=email).exists():
# 		    raise forms.ValidationError('Email already used')
# 		return email

# 	def __init__(self, *args, **kwargs):                                    
# 		super(SignUpForm, self).__init__(*args, **kwargs)                    
# 		self.fields['username'].widget.attrs['class'] = 'form-control'
# 		# self.fields['email'].widget.attrs['class'] = 'form-control'              
# 		self.fields['password1'].widget.attrs['class'] = 'form-control'      
# 		self.fields['password2'].widget.attrs['class'] = 'form-control' 
# 		self.fields['state'].queryset = State.objects.none()

# 		if 'country' in self.data:
# 			try:
# 				country_id = int(self.data.get('country'))
# 				self.fields['state'].queryset = State.objects.filter(country_id=country_id).order_by('name')
# 			except (ValueError, TypeError):
# 				pass  # invalid input from the client; ignore and fallback to empty City queryset
# 		elif self.instance.pk:
# 			self.fields['state'].queryset = self.instance.country.branch_set.order_by('name')


class EditProfileForm(UserChangeForm):                                  										
	email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))                              																						
	username = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))   
	first_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))                                                                    
	# last_name = forms.DateField(widget=forms.TextInput(attrs={'class': 'form-control'}))  
	last_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))                                                                    
	# state = forms.ChoiceField() # id_state
	# city = forms.ChoiceField() # id_city                           																						
	# last_login = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))                                                                             
	# date_joined = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))    
      
	class Meta:                                                                                         
		model = User                                                                                    
		fields = ('username', 'email', 'first_name', 'last_name', 'state', 'city', 'password')   
		# fields = ('username', 'email', 'first_name', 'last_name', 'password', 'date_joined')   
		# fields = ('username', 'email', 'state', 'city', 'password', 'last_login', 'date_joined')   

	def __init__(self, *args, **kwargs):                                    
		super(EditProfileForm, self).__init__(*args, **kwargs)   
		self.fields['city'].queryset = City.objects.none()  

		if 'state' in self.data:
			try:
				state_id = int(self.data.get('state'))
				self.fields['city'].queryset = City.objects.filter(state_id=state_id).order_by('name')
			except (ValueError, TypeError):
				pass  # invalid input from the client; ignore and fallback to empty City queryset
		elif self.instance.pk:
			self.fields['city'].queryset = self.instance.state.city_set.order_by('name')   

	 
class PasswordChangingForm(PasswordChangeForm):                                                                                                                                                                    
	old_password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'type': 'password', 'placeholder': 'old password'}))                          																						
	new_password1 = forms.CharField(max_length=100, widget=forms.PasswordInput(attrs={'class': 'form-control', 'type': 'password'}))                                                                 
	new_password2 = forms.CharField(max_length=100, widget=forms.PasswordInput(attrs={'class': 'form-control', 'type': 'password'}))          

	class Meta:                                                                                                                                      
		model = User                                                                                     
		fields = ('old_password', 'new_password1', 'new_password2')                                                                        

class ProfilePageForm(forms.ModelForm):		
	class Meta:																							
		model = UserProfile 
		fields = ('first_name', 'last_name', 'bio', 'picture', 'website_url', 'birth_date', 'location', 'facebook_url', 'twitter_url', 'instagram_url', 'pinterest_url')
		widgets = {
			# 'username': forms.TextInput(attrs={'class': 'form-control'}),                                                                                                                                                                                                         
			'first_name': forms.TextInput(attrs={'placeholder': 'optional', 'class': 'form-control'}),                                                                                                                                                                                                         
			'last_name': forms.TextInput(attrs={'class': 'form-control'}),       
			'bio': forms.Textarea(attrs={'class': 'form-control'}),  
			'picture': forms.ImageField(required=False),  
			'birth_date': forms.Textarea(attrs={'class': 'form-control'}),                                                                                                                                  
			'location': forms.Textarea(attrs={'class': 'form-control'}),                                                                                                                                                                                                                                                                  
			'website_url': forms.TextInput(attrs={'class': 'form-control'}),                                                                    
			'facebook_url': forms.TextInput(attrs={'class': 'form-control'}),                                                                    
			'twitter_url': forms.TextInput(attrs={'class': 'form-control'}),                                                                    
			'instagram_url': forms.TextInput(attrs={'class': 'form-control'}),                                                                    
			'pinterest_url': forms.TextInput(attrs={'class': 'form-control'}),                                                                    
		}

# class PostForm(forms.ModelForm):
#     body = forms.CharField(
#         label='',
#         widget=forms.Textarea(attrs={
#             'rows': '3',
#             'placeholder': 'Say Something...'
#         })
#     )

#     image = forms.ImageField(
#         required=False,
#         widget=forms.ClearableFileInput(attrs={
#             'multiple': True
#         })
#     )

#     class Meta:
#         model = Post
#         fields = ['body', 'image']

# 	##tried adding placeholder .. 
# 	first_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'say something'}))
# 	last_name = forms.CharField(label='', widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'say something'}))
# 	bio = forms.CharField(label='', widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'say something'}))
# 	website_url = forms.CharField(label='', widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'say something'}))
# 	facebook_url = forms.CharField(label='', widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'say something'}))
# 	twitter_url = forms.CharField(label='', widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'say something'}))
# 	instagram_url = forms.CharField(label='', widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'say something'}))
# 	pinterest_url = forms.CharField(label='', widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'say something'}))

# 	class Meta:																							
# 		model = UserProfile 
# 		fields = ('first_name', 'last_name', 'bio', 'picture', 'website_url', 'facebook_url', 'twitter_url', 'instagram_url', 'pinterest_url')


