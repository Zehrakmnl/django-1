from django.db import models
from django.contrib.auth.models import User
#database tables is will cretae here


class Topic(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name 



class Room(models.Model):
    host = models.ForeignKey(User, on_delete=models.SET_NULL,null=True)
    topic = models.ForeignKey(Topic, on_delete=models.SET_NULL,null=True)
    name = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    participants = models.ManyToManyField(User,related_name='participants', blank=True)
    updated = models.DateTimeField(auto_now=True) 
    created = models.DateTimeField(auto_now_add=True)
    # auto_now ve auto_now_add farklı. Biri her kayıt alındığında kayıt eder...

    class Meta:
        ordering = ['-updated', '-created']
    # Meta sınıfı sayesinde update edilen en üstte görünür. - işareti konmazsa bu çalışmaz!!!

    def __str__(self):
        return self.name

#MODEL EKLEDİĞİN ZAMAN MIGRATION YAPMAYI UNUTMA 
#MIGRATION DAN SONRA MIGRATE ÇALIŞTIRARAK GÜNCEL KODLARI ÇALIŞIR HALE GETİRMEYİ DE UNUTMAAA


class Message(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    body = models.TextField()

    updated = models.DateTimeField(auto_now=True) 
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-updated', '-created']

    def __str__(self):
        return self.body[0:50]
    
    # Meta sınıfı sayesinde update edilen en üstte görünür. - işareti konmazsa bu çalışmaz!!!
     
