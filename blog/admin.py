from django.contrib import admin
from .models import post,category
from django_semmernote.admin import SummerNoteAdmin

# Register your models here.
class PostAdmin(SummerNoteAdmin):
    date_hierarchy = "created_date"
    empty_value_display = '-empty-'
    list_display = ('title','status','author','published_date','created_date','counted_veiws')
    list_filter = ('status',)
    ordering = ['created_date']
    search_fields = ['title','content']
    summernote_fields = ('content',)
    
admin.site.register(post,PostAdmin)
admin.site.register(category)

