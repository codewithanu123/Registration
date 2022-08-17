from django.db import models

class UserD(models.Model) : 
    fname = models.CharField(max_length=50)
    lname = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    phone = models.CharField(max_length=12)
    add_line1 = models.CharField(max_length=200)
    add_line2 = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    zipcode = models.CharField(max_length=10)
    state = models.CharField(max_length=200)

    def __str__(self):
        return self.fname + ' ' + self.lname
