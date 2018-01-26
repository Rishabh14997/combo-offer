from django.db import models
from django.core.urlresolvers import reverse

class Code(models.Model):
    title=models.CharField(max_length=140)
    date=models.DateTimeField()

    def __str__(self):
        return self.title

class model1(models.Model):
    title=models.ForeignKey(Code,on_delete=models.CASCADE)
    file=models.FileField()
    upper_limit=models.IntegerField()
    lower_limit=models.IntegerField()
    email=models.EmailField()

    def __str__(self):
        return str(self.file.name) + " with upper limit: " + str(self.upper_limit) + " and lower limit: " + str(self.lower_limit)
