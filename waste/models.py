from django.db import models

# Create your models here.

class Report(models.Model):
    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('In Progress', 'In Progress'),
        ('Cleaned', 'Cleaned'),
    ]

    title = models.CharField(max_length=100)
    location = models.CharField(max_length=150)
    description = models.TextField()
    reporter_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20, blank=True)
    photo = models.ImageField(upload_to='reports/', blank=True, null=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Pending')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} - {self.location}"