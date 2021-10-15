from django.shortcuts import render,redirect
from django.forms.widgets import DateTimeInput
from django.http.response import HttpResponse, HttpResponseRedirect
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

def search(request): 
    if 'profile' in request.GET and request.GET['profile']:
        user = request.GET.get("profile")

        print(user)
        results = Profile.search_profile(user)
        message = f'profile'
        return render(request, 'all-templates/search.html',{'profiles': results,'message': message})
    else:
        message = "You haven't entered anything to search. Please enter a user profile to search."
    return render(request, 'all-templates/search.html', {'message': message})