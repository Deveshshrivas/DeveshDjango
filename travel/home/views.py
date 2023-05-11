# from os import login_tty
from math import ceil
from django.shortcuts import get_object_or_404,render, redirect, HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import logout, authenticate, login
from django.contrib import messages
from .forms import ImageForm
from .models import Image
import smtplib, time,random,string

from home.models import Contact
# Create your views here.


class Otp:
    def __init__(self, length=6):
        self._length = length
        self._characters = string.ascii_letters + string.digits
    
    def generate(self):
        return ''.join(random.sample(self._characters, self._length))
my_otp = Otp() 

#  login in user
def loginUser(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username, password)
        user = authenticate(username=username, password=password)

        if user is not None:
            # A backend authenticated the credentials
            login(request, user)
            return redirect("/home")

        else:
            # No backend authenticated the credentials
            return render(request, 'login.html')
    return render(request, "login.html")


# sign up user
# def signmup_user(request):
#     if request.method=="POST":
#         username = request.POST.get('username')
#         email1 = request.POST.get('email')
#         pass1 = request.POST.get('pass1')
#         pass2 = request.POST.get('pass2')

#         print(username,email1,pass1,pass2)
#         # if pass1 != pass2:
#         #     return HttpResponse("Your password is not match")
#         # else:
#             # my_user=User.objects.create_user(username,email,pass1)
#             # my_user.save()
#         return redirect("/verification")
#     return render(request, 'signup_user.html')        


    

def index(request):
    if request.user.is_anonymous:
        return redirect("/")
    return render(request, 'index.html')
    # return HttpResponse("this is homepage")


def about(request):
    if request.user.is_anonymous:
        return redirect("/")
    return render(request, 'About.html')


def Services(request):
    if request.user.is_anonymous:
        return redirect("/")
    return render(request, 'Services.html')


def contact(request):
    if request.user.is_anonymous:
        return redirect("/")
    if request.method == "POST":
        username = request.POST.get('username')
        First_name = request.POST.get('First_name')
        Last_name = request.POST.get('Last_name')
        city = request.POST.get('city')
        state = request.POST.get('state')
        zip = request.POST.get('zip')
        email = request.POST.get('email')
        desc = request.POST.get('desc')
        contact = Contact(username=username, First_name=First_name, Last_name=Last_name,
                          city=city, state=state, zip=zip, email=email, desc=desc)
        contact.save()
        my_otp = Otp()
        OTP_GEN_CONF = my_otp.generate()
        send_time = time.time() + 60
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login('plexotpconf@gmail.com' , 'bovgecarhawsxuyg')
        subject = 'Your OTP is here!'
        msg = f'Subject: {subject}\n\nHello! Your OTP is: {OTP_GEN_CONF}'
        server.sendmail('plexotpconf@gmail.com', 'email', msg)
        server.quit()
    return render(request, 'contact.html')


def Course(request):
    if request.user.is_anonymous:
        return redirect("/")
    return render(request, 'Course.html')


# def upload(request):
#     tex = tecRec_data.objects.all()
#     tec = {"name": tex}
#     return render(request, 'upload.html', tec)


def Dbms(request):
    if request.user.is_anonymous:
        return redirect("/")
    return render(request, 'Dbms.html')


def texRec(request):
    if request.method == "POST":
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
    form = ImageForm()
    img = Image.objects.all()

    return render(request, 'texRec.html',{'img': img, 'form': form})


def logoutUser(request):
    logout(request)
    return redirect("/")

# def verification(request):
#     if request.method=="POST":
#         pass
#     return render(request, 'verification.html',)



def delete_image(request, image_id):
    image = get_object_or_404(Image, pk=image_id)
    image.delete()
    return redirect('texRec')