from django.shortcuts import render,redirect
from django.http  import HttpResponse,Http404
from django.forms.widgets import DateTimeInput
from instagramapp.models import Comment, Image, Profile

# Create your views here.
def homepage(request):
    """
    View function to display homepage content
    """
    posts = Image.objects.all()
    profile = Profile.objects.all()
    comment = Comment.objects.all()

    return render(request, 'all-templates/home.html',{"posts":posts,"profile":profile,"comment":comment})