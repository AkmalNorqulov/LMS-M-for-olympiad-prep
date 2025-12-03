from django.shortcuts import render, redirect, get_object_or_404
from .models import Homework
from .forms import HomeworkForm

def homeworks(request):
    homeworks_list = Homework.objects.all()
    return render(request, 'homeworks/homework_list.html', {'homeworks': homeworks_list})

def add_homework(request):
    if request.method == 'POST':
        form = HomeworkForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('homeworks:homeworks')
    else:
        form = HomeworkForm()
    return render(request, 'homeworks/homework_form.html', {'form': form})

def delete_homework(request, pk):
    homework = get_object_or_404(Homework, pk=pk)
    if request.method == 'POST':
        homework.delete()
        return redirect('homeworks:homeworks')
    return render(request, 'homeworks/homework_confirm_delete.html', {'homework': homework})
