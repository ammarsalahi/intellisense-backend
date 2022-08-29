from django.contrib import admin
from .models import CenterSlider, Roadmap, Util, FAQ
from solo.admin import SingletonModelAdmin
from django_summernote.admin import SummernoteModelAdmin
# Register your models here.

@admin.register(Roadmap)
class SomeModelAdmin(admin.ModelAdmin):  # instead of ModelAdmin
    list_display = ['id', 'title', 'sequence', 'content', 'status']

@admin.register(Util)
class UtilAdmin(admin.ModelAdmin):  # instead of ModelAdmin
    list_display = ['id', 'title', 'sequence', 'content']

    
@admin.register(FAQ)
class FAQAdmin(admin.ModelAdmin):  # instead of ModelAdmin
    list_display = ['id', 'title', 'sequence', 'content']


class SliderAdmin(SummernoteModelAdmin, SingletonModelAdmin):  # instead of ModelAdmin
    summernote_fields = ('first_slide_content',  'second_slide_content', 'third_slide_content')

admin.site.register(CenterSlider, SliderAdmin)
# admin.site.register(CenterSlider, SingletonModelAdmin)
