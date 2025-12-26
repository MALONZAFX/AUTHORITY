
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
    department=models.CharField(max_length=255,null=True)
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


class BoardMember(models.Model):
    name = models.CharField(max_length=255)
    role = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='board_members/')
    def __str__(self):
        return self.name
    

class Management(models.Model):
    name = models.CharField(max_length=255)
    role = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='management/')
    def __str__(self):
        return self.name
        
class AccessToInformation(models.Model):
    title = models.CharField(max_length=255)
    document_link = models.URLField()

    def __str__(self):
        return self.title

class Policy(models.Model):
    title = models.CharField(max_length=255)
    document_link = models.URLField()

    def __str__(self):
        return self.title

class ProcurementReport(models.Model):
    title = models.CharField(max_length=255)
    document_link = models.URLField()

    def __str__(self):
        return self.title
    
from django.db import models

class MDNote(models.Model):
    title = models.CharField(max_length=255)
    document_link = models.URLField()

    def __str__(self):
        return self.title

class ChairmanNote(models.Model):
    title = models.CharField(max_length=255)
    document_link = models.URLField()

    def __str__(self):
        return self.title

class PressRelease(models.Model):
    title = models.CharField(max_length=255)
    document_link = models.URLField()

    def __str__(self):
        return self.title

class WebStory(models.Model):
    title = models.CharField(max_length=255)
    document_link = models.URLField()

    def __str__(self):
        return self.title

class PSSpeech(models.Model):
    title = models.CharField(max_length=255)
    document_link = models.URLField()

    def __str__(self):
        return self.title
    
class SuccessStory(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='success_stories/')
    description = models.TextField()


class Tender(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    closing_date = models.DateField(null=True, blank=True)
    document_link = models.URLField()

    def __str__(self):
        return self.title

    
class Eoi(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    closing_date = models.DateField(null=True, blank=True)
    document_link = models.URLField()

    def __str__(self):
        return self.title


class Faq(models.Model):
    question = models.CharField(max_length=255)
    answer = models.TextField()

    def __str__(self):
        return self.question


