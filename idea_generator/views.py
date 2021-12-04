from django.shortcuts import render
from .models import Idea
from .forms import SelectCategoryForm,SelectDifficultyForm
from .sub import get_idea_list,recent_ideas,save_id,remove_repetitions,click_counter,get_clicks
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
        'difficulty_form':'',
        'recent':'',
        'is_empty': 0
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

        ideas = remove_repetitions(ideas,request)
        if len(ideas) == 0:
            ideas = get_idea_list(difficulty_val=difficulty_val, category_val=category_val)

        if len(ideas) != 0:
            select_id = random.choice(ideas)

            idea = Idea.objects.get(id=select_id)

            save_id(request, idea)

            recent = recent_ideas(request, idea)

            click_counter(request)
            clicks = get_clicks(request)

            context['name'] = idea.name
            context['category'] = idea.category.category
            context['difficulty'] = idea.difficulty.difficulty
            context['description'] = idea.description
            context['recent'] = recent
            context['clicks'] = clicks

            save_id(request, idea)
        else:
            context['is_empty'] = 1
    return render(request, 'main.html', context)
