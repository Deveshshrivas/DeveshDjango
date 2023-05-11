from django.contrib import admin
from .models import Image
# Register your models here.
from .models import OpsPageInfo,Contact
admin.site.register(OpsPageInfo)
admin.site.register(Contact)

@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
 list_display = ['id', 'photo', 'date']
