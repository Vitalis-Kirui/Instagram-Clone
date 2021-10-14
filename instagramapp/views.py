from django.shortcuts import render,redirect
from django.http  import HttpResponse,Http404

# Create your views here.
def homepage(request):
    """
    View function to display homepage content
    """
    return render(request, 'all-templates/home.html')