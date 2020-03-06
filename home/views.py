from django.shortcuts import render
from .models import Contact
from django.contrib import messages
from blog.models import Post
# Create your views here.
def home(request):
    return render(request,'home/home.html')

def contact(request):
    if request.method=='POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        content = request.POST['content']
        if len(name)<2  or len(email)<3 or len(phone)<10 or len(content)<5:
            messages.error(request, 'Please fill the form correctly.')
        else:
            contact = Contact(name=name,email=email,phone=phone,content=content)
            contact.save()
            messages.success(request, 'Your message hes been successfully sent.')
        
    return render(request,'home/contact.html')

def about(request):

    messages.success(request, 'This Is About.')

    return render(request,'home/about.html')

def search(request):
    # allposts = Post.objects.all()
    query = request.GET['query']
    if len(query)>78:
        allposts=Post.objects.none()
    else:
        allpostsTitle = Post.objects.filter(title__icontains=query)
        allpostsConteint = Post.objects.filter(content__icontains=query)
        allposts = allpostsTitle.union(allpostsConteint)
    if allposts.count() == 0:
        messages.warning(request, 'No Search Result Found. Please Refine Your Query.')
    params = {'allposts': allposts, 'query':query}
    return render(request,"home/search.html", params)


