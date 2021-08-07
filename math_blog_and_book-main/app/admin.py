from django.contrib import admin
from .models import Chapter
from .models import Content
from .models import About


# Register your models here.
class ContentAdmin(admin.ModelAdmin):
    class Media:
        css = {
            "all": ("css/main.css",)
        }

        js = ("js/content.js",)


class AboutAdmin(admin.ModelAdmin):
    class Media:
        css = {
            "all": ("css/main.css",)
        }

        js = ("js/about.js",)


class ChapterAdmin(admin.ModelAdmin):
    list_display = ['chapter_name']


admin.site.register(Chapter, ChapterAdmin)
admin.site.register(Content, ContentAdmin)
admin.site.register(About, AboutAdmin)
