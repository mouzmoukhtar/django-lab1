from django.shortcuts import render
# from django.http import HttpResponse
# Create your views here.
def index(request):
    x1 = {"id":1, "name":"book1", "description":"book1_description"}
    x2 = {"id":2, "name":"book1", "description":"book2_description"}
    x3 = {"id":3, "name":"book1", "description":"book3_description"}
    x4 = {"id":4, "name":"book1", "description":"book4_description"}
    #return HttpResponse ("moaz here")
    return render(request, 'myapp/index.html',x1)


def about(request):
    return render(request,'myapp/about .html')

def contact(request):
    return render(request,'myapp/contact.html')