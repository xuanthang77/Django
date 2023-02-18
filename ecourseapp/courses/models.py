from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class User(AbstractUser):
    pass
class BaseModel(models.Model):
    created_date = models.DateTimeField(auto_now_add=True, null=True)
    updated_date = models.DateTimeField(auto_now=True,)
    acvite = models.BooleanField(default=True)

    class Meta:
        abstract = True


class Category(models.Model):
    name = models.CharField(max_length=50)


class Course(BaseModel):
    subject = models.CharField(max_length=255)
    discription = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
