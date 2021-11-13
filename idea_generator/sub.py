from .models import Category, Difficulties

def get_categories():
    categories_list = []

    categories_list.append((0,'Any'))
    categories = Category.objects.all()

    for category in categories:
        result = (category.id, category.category)
        categories_list.append(result)
    return categories_list

def get_difficulties():
    difficulty_list = []
    difficulty_list.append((0,'Any'))

    difficulties = Difficulties.objects.all()

    for difficulty in difficulties:
        result = (difficulty.id, difficulty.difficulty)
        difficulty_list.append(result)
    return difficulty_list
