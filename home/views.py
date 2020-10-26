from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'home/index.html', {})

def post_list(request):
    return render(request, 'blog/post_list.html', {})