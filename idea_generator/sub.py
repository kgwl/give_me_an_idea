from .models import Category, Difficulties, Idea


def get_categories():
    categories_list = []

    categories_list.append((0, 'Any'))
    categories = Category.objects.all()

    for category in categories:
        result = (category.id, category.category)
        categories_list.append(result)
    return categories_list


def get_difficulties():
    difficulty_list = []
    difficulty_list.append((0, 'Any'))

    difficulties = Difficulties.objects.all()

    for difficulty in difficulties:
        result = (difficulty.id, difficulty.difficulty)
        difficulty_list.append(result)
    return difficulty_list


def get_idea_list(difficulty_val,category_val):
    categories = Category.objects.all()
    difficulties = Difficulties.objects.all()

    cat_list = []
    diff_list = []

    if category_val == 0:
        cat_list = [category.id for category in categories]
    else:
        cat_list.append(category_val)

    if difficulty_val == 0:
        diff_list = [difficulty.id for difficulty in difficulties]
    else:
        diff_list.append(difficulty_val)

    idea_list = []
    ideas = Idea.objects.all()

    for idea in ideas:
        if idea.category.id in cat_list and idea.difficulty.id in diff_list:
            idea_list.append(idea.id)

    return idea_list




