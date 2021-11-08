from django.contrib import admin
from .models import Idea, Category, Difficulties

admin.site.register(Idea)
admin.site.register(Category)
admin.site.register(Difficulties)
