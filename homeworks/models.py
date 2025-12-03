from django.db import models
from django.utils import timezone
from datetime import datetime, time

class Homework(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    due_date = models.DateField(null=True, blank=True)
    due_time = models.TimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.title

    def is_due_time_passed(self):
        """Check if the due time has passed"""
        if not self.due_date:
            return False
        try:
            # Combine date and time (use midnight if time is not set)
            due_time = self.due_time if self.due_time else time(0, 0, 0)
            due_datetime = timezone.make_aware(datetime.combine(self.due_date, due_time))
            return timezone.now() > due_datetime
        except (ValueError, TypeError):
            return False
