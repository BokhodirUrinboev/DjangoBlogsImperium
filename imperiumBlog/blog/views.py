from django.shortcuts import render, HttpResponse

# Create your views here.

def index(request):
    return render(request, 'blog/index.html')

def about(request):
    return render(request, 'blog/about.html')


def post(request):
    return render(request, 'blog/post.html')