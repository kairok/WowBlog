from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
# Register your models here.
from news.models import *


class NewsAdmin(SummernoteModelAdmin):
    summernote_fields = ('text_min', 'text')




admin.site.register(News, NewsAdmin)

admin.site.register(Category)
admin.site.register(Tag)

class CommentAdmin(admin.ModelAdmin):
    list_display = ('user', 'new', 'created', 'moderration')

admin.site.register(Comments, CommentAdmin)
