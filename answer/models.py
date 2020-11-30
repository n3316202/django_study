from django.db import models


# python manage.py makemigrations
# python manage.py migrate

# Create your models here.
class Member(models.Model):
    name = models.CharField(max_length=100)
    ip = models.CharField(max_length=20)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=20)
    create_date = models.DateTimeField()
    login_date = models.DateTimeField()

    def __str__(self):  # 추가 return self.title
        return self.name + ":" + self.email


class Answer(models.Model):
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    content = models.TextField()
    create_date = models.DateTimeField()


class Choice(models.Model):
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    content = models.TextField()
    create_date = models.DateTimeField()


class LoginTime(models.Model):
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    login_date = models.DateTimeField()
