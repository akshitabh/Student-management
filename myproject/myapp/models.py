from django.db import models
class User(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField(max_length=100)
    password=models.CharField(max_length=100)

class AddCourse(models.Model):
    course=models.CharField(max_length=100)
    fees=models.IntegerField()
    duration=models.CharField(max_length=100)
    desc=models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)
    
    def __str__(self):
        return self.course


class Addstudents(models.Model):
    sname=models.CharField(max_length=100)
    semail=models.EmailField(max_length=100)
    smobile=models.CharField(max_length=10)
    saddress=models.CharField(max_length=255)
    scollege=models.CharField(max_length=255)
    sdegree=models.CharField(max_length=100)
    total_amount=models.IntegerField()
    paid_amount=models.IntegerField()
    due_amount=models.FloatField()
    scourse=models.ForeignKey(AddCourse, on_delete=models.CASCADE)
    def __str__(self) -> str:
        return self.sname





# Create your models here.
