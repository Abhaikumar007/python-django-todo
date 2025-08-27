from django.shortcuts import render, redirect, get_object_or_404
from .models import Tasks 
# Create your views here.

def list_items(request):
    tasks=Tasks.objects.all()
    return render(request,"task_list.html",{"tasks":tasks})

def create_items(request):
    if request.method=='POST':
        text=request.POST['text']
        Tasks.objects.create(text=text)
        return redirect('list')
    return render(request, 'task_list.html')

def complete_task(request,task_id):
    task=Tasks.objects.get(id=task_id)
    task.completed=True 
    task.save()
    return redirect('list')

def delete_task(request,task_id):
    task=Tasks.objects.get(id=task_id)
    task.delete()
    return redirect('list')