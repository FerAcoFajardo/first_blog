from django.db.models import query
from django.http import request
from django.shortcuts import render
from .models import Categoria, Post
from django.shortcuts import get_object_or_404
from django.db.models import Q
from django.core.paginator import Paginator

# Create your views here.

def detail_post(request,slug):
    #post = Post.objects.get(slug = slug)
    post = get_object_or_404(Post,slug=slug)
    print(post)
    return render(request,'post.html',{'detail_post':post})

def home(request):
    queryset = request.GET.get('buscar')
    print(queryset)
    posts = Post.objects.filter(estado = True)
    #print(posts)
    if queryset:
        posts = Post.objects.filter(
            Q(titulo__icontains = queryset) | 
            Q(descripcion__icontains = queryset)
        ).distinct()

    paginator = Paginator(posts,1)
    page = request.GET.get('page')
    posts = paginator.get_page(page)

    return render(request, 'index.html',{'posts':posts})

def about_me(request):
    return render(request, 'about_me.html')

def posts(request):
    queryset = request.GET.get('buscar')
    print(queryset)
    posts = Post.objects.filter(estado = True)
    #print(posts)
    if queryset:
        posts = Post.objects.filter(
            Q(titulo__icontains = queryset) |
            Q(descripcion__icontains = queryset)
        ).distinct()

    paginator = Paginator(posts,15)
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    return render(request,'posts.html',{'posts':posts})

def contact(request):
    return render(request,'contact.html')

def evidences(request):
    return render(request,'evidences.html')