from django.shortcuts import render, get_object_or_404                                         
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView
from django.views import View
from .models import Survey
# , Survey_General
from members.models import UserProfile
from django.urls import reverse_lazy, reverse                                         
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from reportlab.pdfgen import canvas  
from django.shortcuts import redirect, render
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin



def HomeView(request):
	return render(request, 'home.html')

def AboutView(request):
	return render(request, 'about.html')

def SurveyView(request):
  survey = Survey.objects.all()
  # survey_general = Survey_General.objects.all()
  return render(request, 'surveys.html', {'survey':survey})
  # 'survey_general': survey_general

# @login_required
def like(request, id):
  user=request.user
  Likes=False
  Dislikes=False
  if request.method=="POST":
    survey_id=request.POST['survey_id']
    get_video=get_object_or_404(Survey, id=survey_id)

    if user in get_video.likes.all():
      get_video.likes.remove(user)
      Likes=False
      # get_video.save()
    elif user in get_video.dislikes.all():                                                      
      get_video.dislikes.remove(user) 
      Dislikes=False  
      # get_video.save()                                          
      get_video.likes.add(user)  
      Likes=True  
      # get_video.save()

    else:
      get_video.likes.add(user)
      Likes=True
      # get_video.save()

    data={
      "liked":Likes,
      "likes_count":get_video.likes.all().count(),
      "disliked":Dislikes,
      "dislikes_count":get_video.dislikes.all().count()
    }

    return JsonResponse(data, safe=False)
  return redirect(reverse("surveys", args=[str(id)]))


# @login_required
def dislike(request, id):
  user=request.user
  Dislikes=False
  Likes=False
  if request.method == "POST":
    survey_id=request.POST['survey_id']
    # print("printing ajax id", video_id)
    watch=get_object_or_404(Survey, id=survey_id)

    if user in watch.dislikes.all():
      watch.dislikes.remove(user)
      Dislikes = False
      # watch.save()

    elif user in watch.likes.all():
      watch.likes.remove(user)
      Likes=False
      # watch.save()
      watch.dislikes.add(user)                       
      Dislikes=True  
      # watch.save()
        
    else:                                                                               
      watch.dislikes.add(user)                                                            
      Dislikes=True  
      # watch.save()


    data={           
      "liked":Likes,
      "likes_count":watch.likes.all().count(),         
      "disliked":Dislikes,
      "dislikes_count":watch.dislikes.all().count()
    }
  
    return JsonResponse(data, safe=False)
  return redirect(reverse("surveys", args=[str(id)]))




















