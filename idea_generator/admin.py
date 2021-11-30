from django.contrib import admin
from .models import Idea, Category, Difficulties

admin.site.register(Category)
admin.site.register(Difficulties)


class IdeaAdmin(admin.ModelAdmin):
    list_display = ('name','category','difficulty')

admin.site.register(Idea,IdeaAdmin)