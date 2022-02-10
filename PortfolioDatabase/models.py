from django.db import models


# Create your models here.
class Hobbies(models.Model):

    def __str__(self):
        return 'Hobby Name: ' + self.h_name + ', Hobby Description: ' + self.h_desc + "<br>"

    h_name = models.CharField(max_length=200)
    h_desc = models.CharField(max_length=200)


class Portfolio(models.Model):

    def __str__(self):
        return 'Project Name: ' + self.p_name + ', Project Description: ' + self.p_desc + "<br>"

    p_name = models.CharField(max_length=200)
    p_desc = models.CharField(max_length=200)