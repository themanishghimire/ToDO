from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Todo
# Create your views here.

def home(request):
    #return HttpResponse('Hello this is home page.')  #Or JsonResponse
    todo= Todo.objects.all()
    content ={'todos' : todo}
    return render(request,'index.html',context=content)


def create(request):
    if request.method == 'POST':
        name=request.POST.get('name')
        description=request.POST.get('description')
        status=request.POST.get('status')
        Todo.objects.create(name=name,description=description,status=status)
        return redirect('home')
    return render(request,'create.html')