from .models import Category, Difficulties, Idea


def get_categories():
    """
    Get all categories from database
    :return: list of tuples
    """

    categories_list = []

    categories_list.append((0, 'Any'))
    categories = Category.objects.all()

    for category in categories:
        result = (category.id, category.category)
        categories_list.append(result)
    return categories_list


def get_difficulties():
    """
    Get all difficulty levels from database.
    :return: list of tuples
    """
    difficulty_list = []
    difficulty_list.append((0, 'Any'))

    difficulties = Difficulties.objects.all()

    for difficulty in difficulties:
        result = (difficulty.id, difficulty.difficulty)
        difficulty_list.append(result)
    return difficulty_list


def get_idea_list(difficulty_val, category_val):
    """
    Get the elements from the Idea model with the given parameters
    :param difficulty_val: difficulty level id
    :param category_val: category id
    :return: Idea model id list
    """
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


def recent_ideas(request, idea):
    """
    The method saves last drawn element and return the last 5 drawn elements of the Idea model
    :param idea: last drawn element
    :return list of tuples with idea name and description:
    """
    data = {}
    data['name'] = idea.name
    data['category'] = idea.category.category
    data['difficulty'] = idea.difficulty.difficulty
    data['description'] = idea.description
    recent = request.session.get('recent')
    if recent is None:
        recent = []
    recent.append(data)
    request.session['recent'] = recent
    recent = request.session.get('recent')

    recent = [(x['name'], x['description']) for x in recent]

    while len(recent) > 5:
        recent.remove(recent[0])

    recent.reverse()

    return recent


def save_id(request, idea):
    """
    Saves id of last drawn Idea model element
    :param idea: last drawn element
    :return: None
    """
    idea_id = request.session.get('idea_id')
    if idea_id is None:
        idea_id = []
    idea_id.append(idea.id)
    request.session['idea_id'] = idea_id
    request.session.save()


def remove_repetitions(ideas, request):
    """
    Removes Idea element that already has been drawn
    :param ideas: list of Idea model elements
    :return: list of Idea model elements that have not yet been drawn
    """
    last = request.session.get('idea_id')
    if last is not None:
        last = list(dict.fromkeys(last))
        for x in last:
            if x in ideas:
                ideas.remove(x)
    return ideas


def click_counter(request):
    """
    Saves the number of clicks on the draw button
    :param request:
    :return: None
    """
    clicks = request.session.get('clicks')
    if clicks is None:
        clicks = 0
    clicks = clicks + 1
    request.session['clicks'] = clicks
    request.session.save()


def get_clicks(request):
    """
    Get number of clicks
    :return: Number of clicks
    """
    return request.session.get('clicks')
