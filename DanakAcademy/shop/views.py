from django.shortcuts import render

def home(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about_us.html')


def tutorials(request):
    return render(request, 'tutorials.html')


def blog(request):
    return render(request, 'blog.html')


def contact_us(request):
    return render(request, 'contact_us.html')
