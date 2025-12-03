from django.db import models

DAY_CHOICES = [
    (0, 'Monday'),
    (1, 'Tuesday'),
    (2, 'Wednesday'),
    (3, 'Thursday'),
    (4, 'Friday'),
    (5, 'Saturday'),
    (6, 'Sunday'),
]


class Lesson(models.Model):
    day = models.IntegerField(choices=DAY_CHOICES)
    title = models.CharField(max_length=200)
    # store times as plain text (flexible formatting)
    start_time = models.CharField(max_length=32, blank=True)
    end_time = models.CharField(max_length=32, blank=True)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['day', 'start_time']

    def __str__(self):
        return f"{self.get_day_display()} - {self.title} ({self.start_time})"


class Task(models.Model):
    day = models.IntegerField(choices=DAY_CHOICES)
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    # store task times as text fields for flexibility
    start_time = models.CharField(max_length=32, blank=True)
    end_time = models.CharField(max_length=32, blank=True)

    class Meta:
        ordering = ['day', 'start_time']

    def __str__(self):
        return f"{self.get_day_display()} - {self.title}"
