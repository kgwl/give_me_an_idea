from django import forms
from .models import Idea, Category, Difficulties


def get_categories():
    categories_list = []
    categories = Category.objects.all()

    for category in categories:
        result = (category.id, category.category)
        categories_list.append(result)
    return categories_list


def get_difficulties():
    difficulty_list = []
    difficulties = Difficulties.objects.all()

    for difficulty in difficulties:
        result = (difficulty.id, difficulty.difficulty)
        difficulty_list.append(result)
    return difficulty_list


class SelectCategoryForm(forms.Form):
    category = forms.ChoiceField(
        choices=get_categories(),
        required=False,
        label='Category',
    )

class SelectDifficultyForm(forms.Form):
    difficulty = forms.ChoiceField(
        choices=get_difficulties(),
        required=False,
        label='Difficulty',
    )