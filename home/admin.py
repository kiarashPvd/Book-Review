from django.contrib import admin
from home.models import contact
from home.models import newsletter
# Register your models here.

class ContactAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_date'
    list_display = ('name', 'email','subject','message', 'created_date')
    list_filter = ('email',)
    search_fields = ('name', 'message')
    
admin.site.register(contact, ContactAdmin)
admin.site.register(newsletter)
