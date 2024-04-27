from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import *
# Register your models here.
# admin.py

from django.contrib import admin
from .models import Feedback

class FeedbackAdmin(admin.ModelAdmin):
    list_display = ['user', 'message', 'created_at']
    search_fields = ['user__username', 'message']
    list_filter = ['created_at']

admin.site.register(Feedback, FeedbackAdmin)


