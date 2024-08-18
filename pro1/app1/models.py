from django.db import models

# Create your models here.
class Student(models.Model):
    roll = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=20)
    highest_edu = models.CharField(max_length=20)
    city = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.roll}----{self.name}---{self.highest_edu}-----{self.city}"