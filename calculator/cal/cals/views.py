from django.shortcuts import render
# import django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request,'index.html')
    # return HttpResponse('hello world')
