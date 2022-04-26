from django.db import models
from django.contrib.auth.models import User             
from django.urls import reverse	
from datetime import datetime   
from django.utils import timezone                  
from ckeditor.fields import RichTextField      
from ckeditor_uploader.fields import RichTextUploadingField      
from members.models import User 
                                  				


  

class Survey(models.Model):
	question = models.CharField(null=True, blank=True, max_length=255)
	extra_info = models.CharField(null=True, blank=True, max_length=1000)
	likes = models.ManyToManyField(User, blank=True ,related_name='likes')
	dislikes = models.ManyToManyField(User, blank=True ,related_name='dislikes')  

	def get_absolute_url(self):
		return reverse('surveys', args=[str(self.id)])
	
	def num_likes(self):
		return self.likes.count()

	def num_dislikes(self):
		return self.dislikes.count()



# class Survey_General(models.Model):
# 	question = models.CharField(null=True, max_length=255)
# 	extra_info = models.CharField(null=True, blank=True, max_length=1000)
# 	like = models.ManyToManyField(User, blank=True, related_name='likeeeeee')
# 	dislike = models.ManyToManyField(User, blank=True ,related_name='dislikeeeeee')  

# 	def total_like(self):                                                 
# 		return self.like.count()                                           

# 	def total_dislike(self):                                                
# 		return self.dislike.count()


class BroadCast_Email(models.Model):
	subject = models.CharField(max_length=200)
	created = models.DateTimeField(default=datetime.now)
	message = RichTextUploadingField(config_name="default")

	def __unicode__(self):
		return self.subject

	class Meta:
		verbose_name = "BroadCast Email to all Member"
		verbose_name_plural = "BroadCast Email"  


# class Random(models.Model):
# 	testing = models.CharField(null=True, blank=True, max_length=200)                 
# 	question = models.CharField(null=True, max_length=255)
# 	extra_info = models.CharField(null=True, blank=True, max_length=1000)
# 	like = models.ManyToManyField(User, blank=True, related_name='likee')
# 	dislike = models.ManyToManyField(User, blank=True ,related_name='dislikee')  

# 	def total_like(self):                                                 
# 		return self.like.count()                                           

# 	def total_dislike(self):                                                
# 		return self.dislike.count()


# class Randomm(models.Model):
# 	testing = models.CharField(null=True, blank=True, max_length=200)                 
# 	question = models.CharField(null=True, max_length=255)
# 	extra_info = models.CharField(null=True, blank=True, max_length=1000)
# 	like = models.ManyToManyField(User, blank=True, related_name='likeee')
# 	dislike = models.ManyToManyField(User, blank=True ,related_name='dislikeee')  

# 	def total_like(self):                                                 
# 		return self.like.count()                                           

# 	def total_dislike(self):                                                
# 		return self.dislike.count()






		

# class Comment(models.Model):
#   comment = models.TextField()
#   created_on = models.DateTimeField(default=timezone.now)
#   survey = models.ForeignKey('Survey', on_delete=models.CASCADE)
#   author = models.ForeignKey(User, on_delete=models.CASCADE)


# class Comment(models.Model):

#   post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
#   # survey = models.ForeignKey(Survey, on_delete=models.CASCADE, related_name='comments')
#   name = models.CharField(max_length=50)
#   email = models.EmailField()
#   content = models.TextField()
#   publish = models.DateTimeField(auto_now_add=True)
#   status = models.BooleanField(default=True)

#   class Meta:
#     ordering = ('publish',)

#   def __str__(self):
# 			return f'Comment by {self.name}'