from django.shortcuts import render
from .models import About

# Create your views here.

def about_me(request):
    """
    Renders the About page
    """
    about = About.objects.all().order_by('-updated_on').first()
    return render(
        "about/about.html",
        {"about": about},
    )
