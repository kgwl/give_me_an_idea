from django.shortcuts import render
from .models import Idea
import random

def index_view(request):

    context = {
        'name' : '',
        'category':'',
        'difficulty':'',
        'description':'',
        'language':''
    }

    if request.GET.get('btn'):
        select_id = random.choice([i.id for i in Idea.objects.all()])
        idea = Idea.objects.get(id=select_id)

        context['name'] = idea.name
        context['category'] = idea.category
        context['difficulty'] = idea.difficulty
        context['language'] = idea.language_category
        context['description'] = idea.description


    return render(request,'main.html',context)
