from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'home/index.html', {})

def post_list(request):
    return render(request, 'blog/post_list.html', {})

def network_tools(request):
    return render(request, 'pages/index.html', {})

def bolsa_familia(request):
    return render(request, 'bolsa_familia/index.html', {})