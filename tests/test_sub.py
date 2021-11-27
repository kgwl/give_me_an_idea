from django.test import TestCase,RequestFactory
from idea_generator.models import Idea,Difficulties,Category
from idea_generator.sub import get_categories,get_difficulties,get_idea_list,save_id,recent_ideas,remove_repetitions

from django.contrib.sessions.middleware import SessionMiddleware

class TestSub(TestCase):

    def setUp(self):
        self.request_factory = RequestFactory().get('idea_id')
        self.middleware = SessionMiddleware()
        self.middleware.process_request(self.request_factory)

        self.category = Category.objects.create(
            category='Cat'
        )

        self.difficulty = Difficulties.objects.create(
            difficulty='Dif'
        )

        self.idea = Idea.objects.create(
            name='Idea1',
            category=self.category,
            difficulty=self.difficulty,
            description='123'
        )

    def test_get_categories_type(self):
        categories = get_categories()
        self.assertEqual(type(categories),list)
        self.assertEqual(type(categories[0]),tuple)

    def test_get_categories_items(self):
        categories = get_categories()
        item = self.category.category
        flag = False
        for category in categories:
            if category[1] == item:
                flag = True
        self.assertTrue(flag)

    def test_get_difficulties_type(self):
        difficulties = get_difficulties()
        self.assertEqual(type(difficulties),list)
        self.assertEqual(type(difficulties[0]),tuple)

    def test_get_difficulties_items(self):
        difficulties = get_difficulties()
        item = self.difficulty.difficulty
        flag = False
        for difficulty in difficulties:
            if difficulty[1] == item:
                flag = True
        self.assertTrue(flag)

    def test_get_idea_list(self):
        difficulty_val = self.difficulty.id
        category_val =  self.category.id

        idea_list = get_idea_list(difficulty_val,category_val)
        self.assertEqual(idea_list[0],self.idea.id)

    def test_save_id(self):
        save_id(self.request_factory,self.idea)
        idea_id = self.request_factory.session.get('idea_id')[0]
        self.assertEqual(idea_id,self.idea.id)

    def test_recent_ideas(self):
        idea_name = recent_ideas(self.request_factory,self.idea)[0][0]
        self.assertEqual(idea_name,self.idea.name)

    def test_remove_repetitions(self):
        idea1 = Idea.objects.create(
            name='Idea1',
            category=self.category,
            difficulty=self.difficulty,
            description='123'
        )
        save_id(self.request_factory,idea1)
        save_id(self.request_factory,idea1)
        ideas = self.request_factory.session.get('idea_id')
        ideas_without_repetitions = remove_repetitions(ideas,self.request_factory)
        self.assertEqual(len(ideas_without_repetitions),1)
        self.assertEqual(ideas[0],ideas_without_repetitions[0])








