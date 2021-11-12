from django.shortcuts import render
from .models import Idea
from .forms import SelectCategoryForm,SelectDifficultyForm
import random

def index_view(request):

    select_category_from = SelectCategoryForm(request.POST)
    select_difficulty_form = SelectDifficultyForm(request.POST)

    context = {
        'name': '',
        'category': '',
        'difficulty': '',
        'description': '',
        'category_form':'',
        'difficulty_form':''
    }

    if select_category_from.is_valid():
        context['category_form'] = select_category_from

    if select_difficulty_form.is_valid():
        context['difficulty_form'] = select_difficulty_form

    if request.method == 'POST':
        select_id = random.choice([i.id for i in Idea.objects.all()])
        idea = Idea.objects.get(id=select_id)

        context['name'] = idea.name
        context['category'] = idea.category.category
        context['difficulty'] = idea.difficulty.difficulty
        context['description'] = idea.description

    return render(request, 'main.html', context)
