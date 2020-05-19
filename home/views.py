from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Contact
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from blog.models import Post

# HTML Pages
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

#Authentication APIs
def handelSignup(request):
    if request.method == 'POST':
        #get the post perameter
        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']

        #check for errorneous inputs
        #username should be under 10 character
        if len(username) > 10:
            messages.error(request,"username must be 10 characters")
            return redirect('home')

        #username should be alphanumeric

        if not username.isalnum() :
            messages.error(request,"username should only contains laters and characters")
            return redirect('home')

        #password should match

        if pass1 != pass2 :
            messages.error(request,"password do not match")
            return redirect('home')


        #create the user
        myuser = User.objects.create_user(username, email, pass1)
        myuser.first_name = fname
        myuser.last_name = lname
        myuser.save()
        messages.success(request, "your icoder acount has been successfully created")
        return redirect('home')

    else:
        return HttpResponse('<br><br><br><br><br><br><h1 align="center">404 - Not Found</h1>')

def handelLogin(request):
    loginusername = request.POST['loginusername']
    loginpassword = request.POST['loginpassword']
    user = authenticate(username=loginusername, password=loginpassword)
    if user is not None:
        login(request, user)
        messages.success(request,"successfully logedd in")
        return redirect('/')
    else:
        messages.error(request,"invalid credential, please try again. ")
        return redirect('/')

    return HttpResponse('<br><br><br><br><br><br><h1 align="center">404 - Not Found</h1>')

def handelLogout(request):
    logout(request)
    messages.success(request,"successfully logedd out")
    return redirect('/')