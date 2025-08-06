from django.db import models
from datetime import date
from django.utils import timezone


class Participant(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length= 200)
    description = models.TextField()

    def __str__(self):
        return self.name

class Event(models.Model):
    location = (
        ('RAJSHAHI', 'Rajshahi'),
        ('DHAKA', 'Dhaka'),
        ('KHULNA', 'Khulna'),
        ('CUMILLA', 'Cumilla'),
        ('CHITTAGONG', 'Chittagong'),
        ('MYMENSHINGH', 'Mymenshingh'),
        ('RANGPUR', 'Rangpur'),
        ('SYLLET', 'Syllet')
    )
    name = models.CharField(max_length=200)
    description = models.TextField()
    date = models.DateField(default=date.today)
    time = models.TimeField(default=timezone.now)
    locations = models.CharField(default='RAJSHAHI')
    category = models.ForeignKey(
        Category,
        on_delete= models.CASCADE,
        default=1
    )
    participants = models.ManyToManyField(Participant, related_name='event')

    def __str__(self):
        return self.name



