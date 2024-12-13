from django.shortcuts import render, redirect, get_object_or_404
from .forms import TaskForm
from .models import Task

def task_detail(request, pk):
    task = get_object_or_404(Task, pk=pk)
    return render(request, 'todo/task_detail.html', {'task': task})

def task_list(request):
    tasks = Task.objects.all()
    return render(request, 'todo/task_list.html', {'tasks': tasks})

def task_add(request):
    if request.method == 'POST':
        description = request.POST.get('description')
        status = request.POST.get('status').replace('_',' ')
        due_date = request.POST.get('due_date')
        Task.objects.create(description=description, status=status, due_date=due_date)
        return redirect('task_list')
    return render(request, 'todo/task_form.html', {'button_text': 'Создать задачу'})

def edit_task(request, pk):
    task = get_object_or_404(Task, id=pk)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('task_list')
    else:
        form = TaskForm(instance=task)
    return render(request, 'todo/task_edit.html', {'form': form, 'button_text': 'Сохранить изменения'})

def delete_task(request, pk):
    task = get_object_or_404(Task, id=pk)
    if request.method == 'POST':
        task.delete()
        return redirect('task_list')
    return render(request, 'todo/task_confirm_delete.html', {'task': task})
