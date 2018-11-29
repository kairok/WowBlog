from django.contrib import admin

# Register your models here.
from news.models import *


admin.site.register(News)
admin.site.register(Category)
admin.site.register(Tag)
