from django.shortcuts import render,HttpResponse 

# Create your views here.
def index(request):
    context = {
       "variable": "This is sent"
    }
    return render(request,'index.html',context)
    # return HttpResponse("This is a Homepage")

def about(request):
    # return HttpResponse("This is about page")
    return render(request,'about.html')

def services(request):
    # return HttpResponse("This is for services page")
    return render(request,'services.html')

def contact(request):
    # return HttpResponse("This is contact page.")
    return render(request,'contact.html')