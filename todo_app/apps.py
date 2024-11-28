from django.shortcuts import render

def task_list(request):
    return render(request, 'todo/task_list.html')

def add_task(request):
    return render(request, 'todo/add_task.html')