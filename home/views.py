from django.shortcuts import render, HttpResponse
from datetime import datetime
from home.models import Contact
from django.contrib import messages


# Create your views here.
#def index(request):
 #   context = {
  #      "variable1":"Rakesh",
   #     "variable2":"Shrestha"
    #}
    #return render(request,'index.html',context)

def index(request):
    #messages.success(request, "This messages has been sent!")
    return render(request,'index.html')
    
def about(request):
    return render(request,'about.html')
    #return HttpResponse("This is about page")

def services(request):
    return render(request,'services.html')
    #return HttpResponse("This is Services")
def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        message = request.POST.get('message')
        contact= Contact(name=name, email=email, phone=phone, message=message, date=datetime.today())
        contact.save()
        messages.success(request, 'Your message has been sent!')
    return render(request,'contact.html')
    #return HttpResponse("This is Contact")