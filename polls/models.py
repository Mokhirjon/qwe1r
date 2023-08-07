from django.db import models

# Create your models here.
class Subjects(models.Model):
    subjects_name= models.CharField(max_length=12,default='')

    def __str__(self):
        return self.subjects_name