from django.shortcuts import render
from .models import Post
# Create your views here.

def bloghome(request):
    allposts = Post.objects.all()
    context = {
        'allposts': allposts
    }
    return render(request,'blog/bloghome.html', context)

def blogpost(request, slug):
    
    return render(request,'blog/blogpost.html')