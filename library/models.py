from django.db import models
from django.contrib.auth.models import User
from datetime import datetime,timedelta
from django.utils.timezone import datetime

class Book(models.Model):
    name = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    isbn = models.PositiveIntegerField()
    category = models.CharField(max_length=50)

    def __str__(self):
        return str(self.name) + " ["+str(self.isbn)+']'

class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    classroom = models.CharField(max_length=10)
    branch = models.CharField(max_length=10)
    roll_no = models.CharField(max_length=3, blank=True)
    phone = models.CharField(max_length=10, blank=True)
    image = models.ImageField(upload_to="", blank=True)

    def __str__(self):
        return str(self.user) + " ["+str(self.branch)+']' + " ["+str(self.classroom)+']' + " ["+str(self.roll_no)+']'


def expiry():
    return datetime.today() + timedelta(days=14)
class IssuedBook(models.Model):
    student_id = models.CharField(max_length=100, blank=True) 
    isbn = models.CharField(max_length=13)
    issued_date = models.DateField(auto_now=True)
    expiry_date = models.DateField(default=expiry)

class Fine(models.Model):
    objects = models.Manager

    student_id = models.CharField(max_length=100, blank=True) 
    name = models.CharField(max_length=200)
    isbn = models.CharField(max_length=13)
    amount = models.CharField(max_length=12)
    is_active = models.BooleanField(
         default=True, null=True, blank=True, editable=False)
    created_on = models.DateField(
        default=datetime.now, editable=False, null=True, blank=True)
