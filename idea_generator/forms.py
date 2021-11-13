from django import forms
from .sub import get_categories,get_difficulties

class SelectCategoryForm(forms.Form):
    category = forms.ChoiceField(
        choices=get_categories(),
        required=False,
        label='Category',
        widget=forms.Select(attrs={'class':'choice-field'})
    )

class SelectDifficultyForm(forms.Form):
    difficulty = forms.ChoiceField(
        choices=get_difficulties(),
        required=False,
        label='Difficulty',
        widget=forms.Select(attrs={'class': 'choice-field'})
    )
