from django.http import HttpResponse
from django.shortcuts import render, redirect
from store.models.customer import Customer
from store.models.volunteer import Volunteer
from django.contrib.auth.hashers import make_password
from django.views import View


class VolunteerSignup(View):
    def get(self, request):
        return render(request, 'volunteersignup.html')

    def post(self, request):
        postData = request.POST
        first_name = postData.get('firstname')
        last_name = postData.get('lastname')
        phone = postData.get('phone')
        email = postData.get('email')
        address = postData.get('address')
        city = postData.get('city')
        pincode = postData.get('pincode')
        password = postData.get('password')
        # validation
        value = {
            'first_name': first_name,
            'last_name': last_name,
            'phone': phone,
            'email': email,
            'address': address,
            'city': city,
            'pincode':pincode,

        }
        error_message = None

        volunteer = Volunteer(first_name=first_name,
                              last_name=last_name,
                              phone=phone,
                              email=email,
                              address=address,
                              city=city,
                              pincode=pincode,
                              password=password)

        error_message = self.validateVolunteer(volunteer)
        # saving
        if not error_message:
            print(first_name, last_name, phone, password, email,address)
            volunteer.password = make_password(volunteer.password)
            volunteer.register()
            return redirect('homepage')
        else:
            data = {
                'error': error_message,
                'values': value
            }
            return render(request, 'VolunteerSignup.html', data)

    def validateVolunteer(self, volunteer):
        error_message = None
        if not volunteer.first_name:
            error_message = "First Name Required"
        elif len(volunteer.first_name) < 4:
            error_message = 'First name must be 4 characters long'
        elif not volunteer.last_name:
            error_message = 'Last name required'
        elif not volunteer.phone:
            error_message = "Please enter phone number again"
        elif len(volunteer.phone) < 4:
            error_message = 'Phone number must be 10 char long'
        elif len(volunteer.pincode) < 6:
            error_message = 'Pincode must be 10 numbers long'
        elif len(volunteer.city) < 2:
            error_message = 'Enter City name again'
        elif len(volunteer.email) < 5:
            error_message = 'Email must be 5 char long'
        elif len(volunteer.address) < 5:
            error_message = 'Please enter address again'
        elif volunteer.isExists():
            error_message = 'Email address already registered'
        return error_message
