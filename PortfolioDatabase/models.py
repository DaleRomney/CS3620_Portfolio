from django.db import models


# Create your models here.
class Hobbies(models.Model):

    def __str__(self):
        return 'Hobby Name: ' + self.h_name + ', Hobby Description: ' + self.h_desc + "<br>"

    h_name = models.CharField(max_length=200)
    h_desc = models.CharField(max_length=200)
    h_image = models.CharField(max_length=500, default="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSVsf9a8CMJ07MTLXvICC1qn8EkFqbZaacuww&usqp=CAU")


class Portfolio(models.Model):

    def __str__(self):
        return 'Project Name: ' + self.p_name + ', Project Description: ' + self.p_desc + "<br>"

    p_name = models.CharField(max_length=200)
    p_desc = models.CharField(max_length=200)
    p_image = models.CharField(max_length=500, default="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQWJYOlsYxx93OW2G8M30CE83UGgTWbcZKObA&usqp=CAU")


class Contact(models.Model):

    c_name = models.CharField(max_length=200)
    c_email = models.CharField(max_length=200)
    c_message = models.CharField(max_length=500, default="Personal Message goes here.")

    def __str__(self):
        return 'Name: ' + self.c_name + ' Email: ' + self.c_email + ' Personal Message: ' + self.c_message