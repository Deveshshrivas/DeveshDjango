from django.urls import path
from home import views
from django.conf import settings
from django.conf.urls.static import static
 


urlpatterns = [
    
    path('',views.loginUser,name = "login"),
   
    path('home',views.index,name='home'),
    path('about',views.about,name = 'about'),
    path('contact',views.contact,name='contact'),
    path('Services',views.Services,name = 'Services'),
    path('Course',views.Course,name = 'Course'),
    # path('upload',views.upload,name = 'uplaod'),
    path('Dbms',views.Dbms,name = 'Dbms'),
    path('texRec',views.texRec,name='texRec'),
    path('logout', views.logoutUser, name="logout"),
    path('delete/<int:image_id>/', views.delete_image, name='delete_image'),
    # path('verification', views.verification, name="OTP_Ver"),
    # path('test', views.test, name="test"),


    

]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)


# STATICFILES_DIRS
 
