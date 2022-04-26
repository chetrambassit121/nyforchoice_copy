from django import forms
from .models import Post, Comment, MessageModel

# class CommentForm(forms.ModelForm):
#     comment = forms.CharField(
#         label='',
#         widget=forms.Textarea(
#             attrs={'rows': '8',
#                    # 'cols': '68%',
#                    'placeholder': 'Add a Comment...'}
#         ))

#     class Meta:
#         model = Comment
#         fields = ['comment']

# class PostForm(forms.ModelForm):
#     body = forms.CharField(
#         label='',
#         widget=forms.Textarea(attrs={
#             'rows': '8',
#             'placeholder': 'Say Something...'
#             }))

#     image = forms.ImageField(
#         required=False,
#         widget=forms.ClearableFileInput(attrs={
#             'multiple': True
#             })
#     )

#     class Meta:
#         model = Post
#         fields = ['body', 'image']

# class EditPostForm(forms.ModelForm):
#     class Meta:
#         model = Post
#         fields = ('body', 'image')
#         widgets = {
#             'body': forms.TextInput(attrs={'class': 'form-control'}),
#         }


#     # body = forms.CharField(
#     #     label='',
#     #     widget=forms.Textarea(
#     #         attrs={'rows': '8',
#     #                # 'cols': '68%',
#     #                'placeholder': 'Edit your Post...'}
#     #     ))

#     # image = forms.ImageField(
#     #     required=False,
#     #     widget=forms.ClearableFileInput(attrs={
#     #         'multiple': True
#     #         })
#     # )

#     # class Meta:
#     #     model = Post
#     #     fields = ['body']





# # class ProfilePageForm(forms.ModelForm):     
# #     class Meta:                                                                                         
# #         model = UserProfile 
# #         fields = ('first_name', 'last_name', 'bio', 'picture', 'website_url', 'birth_date', 'location', 'facebook_url', 'twitter_url', 'instagram_url', 'pinterest_url')
# #         widgets = {
# #             # 'username': forms.TextInput(attrs={'class': 'form-control'}),                                                                                                                                                                                                         
# #             'first_name': forms.TextInput(attrs={'placeholder': 'optional', 'class': 'form-control'}),                                                                                                                                                                                                         
# #             'last_name': forms.TextInput(attrs={'class': 'form-control'}),       
# #             'bio': forms.Textarea(attrs={'class': 'form-control'}),  
# #             'birth_date': forms.Textarea(attrs={'class': 'form-control'}),                                                                                                                                  
# #             'location': forms.Textarea(attrs={'class': 'form-control'}),                                                                                                                                                                                                                                                                  
# #             'website_url': forms.TextInput(attrs={'class': 'form-control'}),                                                                    
# #             'facebook_url': forms.TextInput(attrs={'class': 'form-control'}),                                                                    
# #             'twitter_url': forms.TextInput(attrs={'class': 'form-control'}),                                                                    
# #             'instagram_url': forms.TextInput(attrs={'class': 'form-control'}),                                                                    
# #             'pinterest_url': forms.TextInput(attrs={'class': 'form-control'}),                                                                    
# #         }


# class ThreadForm(forms.Form):
#     username = forms.CharField(label='', max_length=100)

# class MessageForm(forms.ModelForm):
#     body = forms.CharField(label='', max_length=1000)

#     image = forms.ImageField(required=False)

#     class Meta:
#         model = MessageModel
#         fields = ['body', 'image']

# class ShareForm(forms.Form):
#     body = forms.CharField(
#         label='',
#         widget=forms.Textarea(attrs={
#             'rows': '3',
#             'placeholder': 'Say Something...',
#             }))

# class ExploreForm(forms.Form):
#     query = forms.CharField(
#         label="",
#         widget=forms.TextInput(attrs={
#             'placeholder': 'type in a tag',
#         })
#     )
    










class PostForm(forms.ModelForm):
    body = forms.CharField(
        label='',
        widget=forms.Textarea(attrs={
            'rows': '3',
            'placeholder': 'Say Something...'
        })
    )

    image = forms.ImageField(
        required=False,
        widget=forms.ClearableFileInput(attrs={
            'multiple': True
        })
    )

    video = forms.FileField(
        required=False,
        widget=forms.ClearableFileInput(attrs={
            'multiple': True
        })
    )

    class Meta:
        model = Post
        fields = ['body', 'image', 'video']


class EditPostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('body', 'image')
        widgets = {
            'body': forms.TextInput(attrs={'class': 'form-control'}),
        }

class CommentForm(forms.ModelForm):
    comment = forms.CharField(
        label='',
        widget=forms.Textarea(attrs={
            'rows': '3',
            'placeholder': 'Leave a Comment...'
            }))

    class Meta:
        model = Comment
        fields = ['comment']

# class ReplyForm(forms.ModelForm):
#     comment = forms.CharField(
#         label='',
#         widget=forms.Textarea(attrs={
#             'rows': '3',
#             'placeholder': 'Leave a Reply...'
#             }))

#     class Meta:
#         model = Comment
#         fields = ['comment']

class ThreadForm(forms.Form):
    username = forms.CharField(label='', max_length=100)

class MessageForm(forms.ModelForm):
    body = forms.CharField(
        label='',
        max_length=1000,
        widget=forms.Textarea(attrs={
            'rows': '3',
            
        }))
        

    image = forms.ImageField(required=False)

    class Meta:
        model = MessageModel
        fields = ['body', 'image']

class ShareForm(forms.Form):
    body = forms.CharField(
        label='',
        widget=forms.Textarea(attrs={
            'rows': '3',
            'placeholder': 'Say Something...'
        })
    )

    class Meta:
        model = MessageModel
        fields = ['body']


class ExploreForm(forms.Form):
    query = forms.CharField(
        label='',
        widget=forms.TextInput(attrs={
            'placeholder': 'Explore tags'
        })
    )
