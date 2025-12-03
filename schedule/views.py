from django.shortcuts import render, get_object_or_404
from .models import Lesson, Task, DAY_CHOICES


DAY_NAMES = [name for _, name in DAY_CHOICES]


from django.db.models import TimeField
from django.db.models.functions import Cast
import datetime

def index(request):
    week = []
    for i, name in enumerate(DAY_NAMES):
        lessons = (
            Lesson.objects
            .filter(day=i)
            .annotate(start_time_cast=Cast('start_time', TimeField()))
            .order_by('start_time_cast')
        )

        tasks = (
            Task.objects
            .filter(day=i)
            .annotate(start_time_cast=Cast('start_time', TimeField()))
            .order_by('start_time_cast')
        )

        week.append({
            'index': i,
            'name': name,
            'lessons': lessons,
            'tasks': tasks
        })

    # compute today's weekday index (Monday=0..Sunday=6)
    today_index = datetime.date.today().weekday()
    return render(request, 'schedule/index.html', {'week': week, 'today_index': today_index})



from django.db.models import TimeField
from django.db.models.functions import Cast

def day_detail(request, day):
    day = int(day)
    name = DAY_NAMES[day]

    lessons = (
        Lesson.objects
        .filter(day=day)
        .annotate(start_time_cast=Cast('start_time', TimeField()))
        .order_by('start_time_cast')
    )

    tasks = (
        Task.objects
        .filter(day=day)
        .annotate(start_time_cast=Cast('start_time', TimeField()))
        .order_by('start_time_cast')
    )

    return render(request, 'schedule/day_detail.html', {
        'day_index': day,
        'day_name': name,
        'lessons': lessons,
        'tasks': tasks,
    })
