from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(Credential)
admin.site.register(Message)
admin.site.register(Comment)