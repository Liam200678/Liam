from django.shortcuts import render
from .models import Blog

# Create your views here.
def home(request):
    blogs = Blog.objects.all()
    context = {
        'blogs' : blogs
    }
    return render(request, 'local/home.html',context)
