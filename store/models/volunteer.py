from django.db import models

class Volunteer(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=15)
    email = models.EmailField()
    password = models.CharField(max_length=500)
    address = models.CharField(max_length=500,default='')
    city = models.CharField(max_length=500, default='')
    pincode = models.CharField(max_length=500, default='')


    def register(self):
        self.save()

    @staticmethod
    def get_volunteer_by_email(email):
        try:

            return Volunteer.objects.get(email = email)
        except:
            return False
    def __str__(self):
        return 'Volunteer: '+ self.first_name+' '+self.last_name

    def isExists(self):
        if Volunteer.objects.filter(email = self.email):
            return True
        return False