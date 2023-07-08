from django.contrib import admin
from django.utils.html import format_html
from .models import *

# Register your models here.
@admin.register(Royal)
class RoyalAdmin(admin.ModelAdmin):
    list_display=['id','name','slug']
    prepopulated_fields={'slug':('name',)}


@admin.register(Family)
class FamilyAdmin(admin.ModelAdmin):
    list_display=['id','title','royal','image_tag','created_at','updated_at','is_published']  
    search_fields=['title','content'] 
    list_editable=['is_published']
    prepopulated_fields={'slug':('title',)} 

    def image_tag(self, obj):
        if obj.photo:
            return format_html('<img src="{}" width="100"/>'.format(obj.photo.url))
        else:
            return 'No Image Found'

    
@admin.register(Page)
class PageAdmin(admin.ModelAdmin):
    list_display=['id', 'title', 'slug']    
    prepopulated_fields={'slug':('title',)}

@admin.register(Popular)
class PopularAdmin(admin.ModelAdmin):
    list_display=['id', 'title', 'slug']
    prepopulated_fields={'slug':('title',)}