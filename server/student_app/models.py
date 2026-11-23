from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=255)
    student_email = models.EmailField(max_length=255)
    personal_email = models.EmailField(max_length=255)
    locker_number = models.IntegerField()
    locker_combination = models.CharField(max_length=8)
    good_student = models.BooleanField(default=True)
    
class Enrollment(models.Model):
    pass