from django.shortcuts import render , HttpResponse

# Create your views here.
def index(request):
    return render(request, "index.html")

    #return HttpResponse("this is homepage")
    #return HttpResponse("this is homepage")

def about(request):
        return render(request, 'about.html')
    #return HttpResponse("this is about page")

def services(request):
    return render(request, 'services.html')

def contact(request):
        return render(request, 'contact.html')
    #return HttpResponse('this is contact page')
