from django.shortcuts import render,redirect
from .models import Post,BlogComment
from django.contrib import messages
from blog.templatetags import extras
# Create your views here.

def bloghome(request):
    allposts = Post.objects.all()
    context = {
        'allposts': allposts
    }
    return render(request,'blog/bloghome.html', context)

def blogpost(request, slug):
    post = Post.objects.filter(slug=slug).first()
    post.views = post.views + 1
    post.save()
    comments = BlogComment.objects.filter(post=post, parents=None)
    replies = BlogComment.objects.filter(post=post).exclude(parents=None)
    replyDict = {}
    for reply in replies:
        if reply.parents.sno not in replyDict.keys():
            replyDict[reply.parents.sno] = [reply]
        else:
            replyDict[reply.parents.sno].append(reply)

    context = { 'post' : post , 'comments' : comments , 'user' : request.user , 'replydict' : replyDict}
    return render(request,'blog/blogpost.html', context)

def postComment(request):
    if request.method=="POST":
        comment = request.POST.get("comment")
        user = request.user
        postSno = request.POST.get("postSno")
        post = Post.objects.get(sno=postSno)
        parentsno = request.POST.get("parentsno")
        if parentsno=="":
            comment = BlogComment(comment=comment, user=user, post=post)
            comment.save()
            messages.success(request, "your comment has been posted successfully")
        else:
            parent = BlogComment.objects.get(sno=parentsno)
            comment = BlogComment(comment=comment, user=user, post=post, parents=parent)

            comment.save()
            messages.success(request, "your reply has been posted successfully")

    return redirect(f"/blog/{post.slug}")