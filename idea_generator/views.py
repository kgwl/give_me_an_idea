from django.shortcuts import render
import random

# Create your views here.

def index_view(request):
    context = {
        'my_variable' : '',
    }

    if request.GET.get('btn'):
        pass

    return render(request,'main.html',context)
