from django.db import models

class students(models.Model):
    stname=models.CharField(max_length=50)
    stemail=models.CharField(max_length=50)
    stphone=models.CharField(max_length=50)

    def __str__(self):
        return self.stname
    

