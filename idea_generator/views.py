from django.shortcuts import render
from .models import Idea

def index_view(request):
    context = {
        'my_variable' : '',
    }

    if request.GET.get('btn'):
        pass

    return render(request,'main.html',context)
