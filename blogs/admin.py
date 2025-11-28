from django.contrib import admin

# Register your models here.
from .models import Category ,Blog
#Category model admin panel la register pannudhu
class CategoryAdmin(admin.ModelAdmin):
    list_display=['category_name', 'created_at', 'updated_at'] #admin panel la category model la ethana fields display pannanum nu sollanum


class BlogAdmin(admin.ModelAdmin):
    prepopulated_fields={'slug':('title',)} #create unique filed #produce the tuple effect
    list_display = ["title",'slug','category','author','created_at','updated_at','is_featured','status']
    search_fields=('id','title','category__category_name','status') 
    
    #Unsupported lookup 'icontains' for ForeignKey or join on the field not permitted. ethunala category foriegn so forign key iruthu name edkaram so we 
    #category__category_name :fethc name edukarum
    
    list_editable=('is_featured',)
    
admin.site.register(Category, CategoryAdmin)
admin.site.register(Blog,BlogAdmin)
