from django.http import HttpResponse ,HttpRequest,HttpResponseRedirect
from django.shortcuts import render

def base(request):
    return HttpResponse("This is Landing page")


def aboutUs(request):
    return render(request,"about.html")
def contect(request):
    return render(request,"contect.html")
def job(request):
    return render(request,"job.html")

def cours(request):
    return HttpResponse("This is your cours")

def coursId(request,coursid):
    return HttpResponse(f"{coursid} : this is your ID")

def reg(request):
    data = {
        'title':'Registration Formm'
    }
    return render(request,"reg.html",data)

def log(request):
    data = {
        
    }    
    try:
        if request.method == "POST":
            
            n1 = request.POST.get('Email')
            n2 = request.POST.get('Password')
            email =n1
            password = n2
            
            return HttpResponseRedirect('/job/')
    except:
        pass

    
    return render(request,"login.html",data)

