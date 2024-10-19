from django.contrib import admin
from .models import *

def active_selected_record(self, request, queryset):
    queryset.update(is_active=True)

def inactive_selected_record(self, request, queryset):
    queryset.update(is_active=False)

class FineAdmin(admin.ModelAdmin):

    list_display =['student_id','name','isbn','amount','created_on','is_active']


admin.site.add_action(active_selected_record)
admin.site.add_action(inactive_selected_record)

admin.site.register(Book)
admin.site.register(Student)
admin.site.register(IssuedBook)
admin.site.register(Fine, FineAdmin)