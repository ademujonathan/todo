from django.contrib import admin

# Register your models here.
# from here we'll import models
from .models import *

admin.site.register(Task)

