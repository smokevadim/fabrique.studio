from django.contrib import admin
from .models import *

# Register your models here.
@admin.register(Poll, Question, Answer, User)
class PersonAdmin(admin.ModelAdmin):
    pass
