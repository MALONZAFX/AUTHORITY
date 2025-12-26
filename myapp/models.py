
from django.db import models
from django.utils.timezone import now
from simple_history.models import HistoricalRecords


class CustomHistoricalRecords(HistoricalRecords):
    def get_history_record(self, instance):
        history_instance = super().get_history_record(instance)
        history_instance.custom_str = f'{history_instance.history_date} - {history_instance.history_user} - {history_instance.history_type} - TITLE: {history_instance.title}'
        return history_instance
# Create your models here.
class Gallery(models.Model):
    image = models.ImageField(upload_to='gallery_images/')
    created_at = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100,blank=True,null=True)
    history = CustomHistoricalRecords()

    def __str__(self):
        return self.title

class Video(models.Model):
    video_url= models.URLField(default="")
    created_at = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100,blank=True,null=True)
    history = CustomHistoricalRecords()

    def __str__(self):
        return self.title
    
#users model
class PrivitasationUsers(models.Model):
    email=models.EmailField()
    password= models.TextField()
    name=models.CharField(max_length=30,blank=True,null=True)
    kra=models.TextField(blank=True,null=True)
    phone=models.TextField(blank=True,null=True)
    company=models.TextField(blank=True,null=True)


    def __str__(self):
        return self.email
    
class AvailableOpening(models.Model):
    title = models.CharField(max_length=255)
    date_today = models.DateField()
    link_to_opening=models.URLField(blank=True,null=True)
    department=models.CharField(max_length=255,default=None)
    history = CustomHistoricalRecords()

    def __str__(self):
        return self.title


class  News(models.Model):
    title=models.CharField(max_length=255)
    date_today = models.DateField()
    text=models.CharField(max_length=255)
    image = models.ImageField(upload_to='gallery_images/')
    history = CustomHistoricalRecords()
    def __str__(self):
        return self.title

class  RecentActivities(models.Model):
    title=models.CharField(max_length=255)
    date_today = models.DateField()
    text=models.CharField(max_length=255)
    image = models.ImageField(upload_to='gallery_images/')
    link_url=models.URLField(blank=True,null=True)
    history = CustomHistoricalRecords()
    def __str__(self):
        return self.title
