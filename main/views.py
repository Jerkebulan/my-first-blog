from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import *


def home(request):
    ps = Post.objects.order_by('published_date')
    return render(request, 'home.html', {'posts': ps})


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'post_detail.html', {'post': post})
