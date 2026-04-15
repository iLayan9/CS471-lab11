from django.contrib import admin

# Register your models here.
from .models import Book, Address, Student

admin.site.register(Address)
admin.site.register(Student)