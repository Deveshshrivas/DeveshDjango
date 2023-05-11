from django.urls import path
from home import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [

 path('signmup_user',views.signmup_user,name = 'signmup_user'),




 ]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)