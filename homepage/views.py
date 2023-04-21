from django.shortcuts import render, get_object_or_404
from django.views import generic, View




def index(request):
    """
    Index view
    """
    return render(request, 'index.html')
