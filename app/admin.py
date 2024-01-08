from django.contrib import admin

# Register your models here.

from app.models import *

class custamizeWebpage(admin.ModelAdmin):
    list_display=['topic_name','name','url','email']
    list_display_links=['name','url']
    list_editable=['email']
    search_fields=['name']
    list_filter=['topic_name','name','url','email']
    list_per_page=2

class custamizeTopic(admin.ModelAdmin):
    list_display=['topic_name']
    list_display_links=['topic_name']
    #list_editable=['email']
    search_fields=['topic_name']
    list_filter=['topic_name']
    list_per_page=2

class custamizeAccessRecord(admin.ModelAdmin):
    list_display=['name','date','author']
    list_display_links=['name','author']
    list_editable=['date']
    search_fields=['name']
    list_filter=['name','date','author']
    list_per_page=2    



admin.site.register(Topic,custamizeTopic)

admin.site.register(Webpage,custamizeWebpage)

admin.site.register(AccessRecord,custamizeAccessRecord)