from django.contrib import admin
from blog.models import post,category,Comment


# Register your models here.
class PostAdmin(admin.ModelAdmin):
    date_hierarchy = "created_date"
    empty_value_display = '-empty-'
    list_display = ('title','status','author','published_date','created_date','counted_veiws')
    list_filter = ('status','author',)
    ordering = ['published_date']
    search_fields = ['title','content']
    #test
   
class CommentAdmin(admin.ModelAdmin):
    date_hierarchy = "created_date"
    empty_value_display = '-empty-'
    list_display = ('name','post','approved','created_date')
    list_filter = ('post','approved',)
    search_fields = ['name','post']
    
admin.site.register(Comment, CommentAdmin)    
admin.site.register(post,PostAdmin)
admin.site.register(category)

