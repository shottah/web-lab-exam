from django.contrib import admin

# Register your models here.
from .courses import Course

admin.site.register(Course)