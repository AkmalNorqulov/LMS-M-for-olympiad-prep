from django.shortcuts import render, redirect
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
