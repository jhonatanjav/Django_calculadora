from django.shortcuts import render
# Create your views here.
def info(req):
    return render(req,'info.html')

    