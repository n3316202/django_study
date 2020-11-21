from django.db import models

# Create your models here.
class Member(models.Model):
    name = models.CharField(max_length=100)
    ip = models.CharField(max_length=20)
    create_date = models.DateTimeField()

class Answer(models.Model):
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    content = models.TextField()
    create_date = models.DateTimeField()

class Choice(models.Model):
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    content = models.TextField()
    create_date = models.DateTimeField()
