from django.shortcuts import render
from .models import ToDo

# Create your views here.

def todo_list (request):
    data = ToDo.objects.all() # model
    return render(request,'todo_list.html', {'todos':data})


def todo_detail (request,id):
    data = ToDo.objects.get(id=id)
    return render(request, 'todo_detail.html', {'todo':data})