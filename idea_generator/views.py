from django.shortcuts import render
from .models import Idea
from .forms import SelectCategoryForm,SelectDifficultyForm
from .sub import get_idea_list
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

    context['category_form'] = select_category_from
    context['difficulty_form'] = select_difficulty_form

    if request.method == 'POST':
        difficulty_val = 0
        category_val = 0
        if select_difficulty_form.is_valid():
            difficulty_val = int(select_difficulty_form.cleaned_data['difficulty'])

        if select_category_from.is_valid():
            category_val = int(select_category_from.cleaned_data['category'])

        ideas = get_idea_list(difficulty_val=difficulty_val,category_val=category_val)

        select_id = random.choice(ideas)
        idea = Idea.objects.get(id=select_id)

        context['name'] = idea.name
        context['category'] = idea.category.category
        context['difficulty'] = idea.difficulty.difficulty
        context['description'] = idea.description

    return render(request, 'main.html', context)
