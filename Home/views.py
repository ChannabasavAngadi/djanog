from django.shortcuts import render,HttpResponse

def index(request):
    return render(request,'index.html')
    #return HttpResponse("This is home page, Guvi")

def about(request):
    return HttpResponse("This is about page, Guvi")

def classes(request):
    return HttpResponse("This is classes page, Guvi")

def certificates(request):
    return HttpResponse("This is certificates page, Guvi")
