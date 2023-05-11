from django.shortcuts import render,redirect,HttpResponse
from django.core.mail import send_mail
from .verf import Otp
from django.contrib.auth.models import User





# # def send_otp(request):
# #     # Generate the OTP
# #     my_otp = Otp()
# #     OTP_GEN_CONF = my_otp.generate()

# #     # Retrieve the user's email from the signmup_user() function
# #     email1 = signmup_user()
# #     recipient_email = User.objects.get(email=email1).email

# #     # Compose the email message
# #     subject = 'Your OTP is here!'
# #     message = f'Hello! Your OTP is: {OTP_GEN_CONF}'
# #     from_email = 'plexotpconf@gmail.com'
# #     recipient_list = [recipient_email]

# #     try:
# #         # Send the email
# #         send_mail(
# #             subject=subject,
# #             message=message,
# #             from_email=from_email,
# #             recipient_list=recipient_list,
# #             fail_silently=False,
# #         )
# #         # Render a template to show that the email was sent
# #         context = {'message': f'Email sent to {recipient_email} with OTP {OTP_GEN_CONF}'}
# #         return render(request, 'send_otp.html', context)
# #     except Exception as e:
# #         # Handle the exception
# #         context = {'message': f'Error sending email: {e}'}
# #         return render(request, 'send_otp.html', context)


# # def verification(request):
# #     if request.method == "POST":
# #         email = request.POST.get('email')
# #         # TODO: verify the OTP code and do something with it
# #     return render(request, 'verification.html',)

# import smtplib
# import time
# import string
# import random

# class Otp:
#     def __init__(self, length=6):
#         self._length = length
#         self._characters = string.ascii_letters + string.digits
    
#     def generate(self):
#         return ''.join(random.sample(self._characters, self._length))
    


# my_otp = Otp()
# OTP_GEN_CONF = my_otp.generate()

# global OTPGEN
# def OTPGEN():
#     return(OTP_GEN_CONF)




# send_time = time.time() + 60
# server = smtplib.SMTP('smtp.gmail.com', 587)
# server.starttls()
# server.login('plexotpconf@gmail.com' , 'bovgecarhawsxuyg')
# subject = 'Your OTP is here!'
# msg = f'Subject: {subject}\n\nHello! Your OTP is: {OTP_GEN_CONF}'
# server.sendmail('plexotpconf@gmail.com', 'deveshshrivas060@gmail.com', msg)
# server.quit()







def signmup_user(request):
    if request.method=="POST":
        username = request.POST.get('username')
        email1 = request.POST.get('email')
        pass1 = request.POST.get('pass1')
        pass2 = request.POST.get('pass2')

        print(username,email1,pass1,pass2)
        if pass1 != pass2:
            return HttpResponse("Your password is not match")
        else:
            my_user=User.objects.create_user(username,email1,pass1)
            my_user.save()
        return redirect("/")
    return render(request, 'signmup_user.html') 

def verification(request):
    return render(request, 'verification.html'),