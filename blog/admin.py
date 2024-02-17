from django.contrib import admin
from .models import post
# Register your models here.
class PostAdmin(admin.ModelAdmin):
    date_hierarchy = "created_date"
    empty_value_display = '-empty-'
    list_display = ('title','status','published_date','created_date','counted_veiws')
    list_filter = ('status',)
    ordering = ['created_date']
    search_fields = ['title','content']
    
admin.site.register(post,PostAdmin)

