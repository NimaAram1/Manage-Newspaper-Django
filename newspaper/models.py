from django.db import models
from django.utils import timezone
class Notes(models.Model):
    title = models.CharField(max_length=80,verbose_name='عنوان یادداشت')
    body = models.TextField(verbose_name='متن یادداشت')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.title
     
class NewsPaper(models.Model):
    newspaper_stable = models.IntegerField(verbose_name='شماره')
    image = models.ImageField(upload_to='images',verbose_name='عکس روزنامه')
    notes = models.ManyToManyField(Notes)
    file = models.FileField(upload_to='files',verbose_name='فایل پی دی اف')
    pub_date = models.DateField(default=timezone.now,verbose_name='تاریخ انتشار')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    def __str__(self):
        return "روزنامه شماره : "+str(self.newspaper_stable)
    