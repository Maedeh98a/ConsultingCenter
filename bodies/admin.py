from django.contrib import admin
from .models import *


@admin.register(UniversityComment)
class UniCommentAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'active']
    list_filter = ['name', 'email']
    search_fields = ['name', 'email']
    # list_editable = ['active']


@admin.register(ConsultantComment)
class ConsultantAdmin(admin.ModelAdmin):
    list_display = ['name', 'email']
    list_filter = ['name', 'email']
    search_fields = ['name', 'email']
    # list_editable = ['active']


@admin.register(AllComment)
class AllCommentAdmin(admin.ModelAdmin):
    list_display = ['name', 'email']
    list_filter = ['name', 'email']
    search_fields = ['name', 'email']
    # list_editable = ['active']
