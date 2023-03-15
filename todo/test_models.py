from django.test import TestCase
from .models import Item

# Create your tests here.


class TestModels(TestCase):

    def test_done_defaults_to_false(self):
        item = Item.objects.create(name='Test Todo Item')
        self.assertFalse(item.done)

    def test_item_string_method_returns_name(self):
        # to test the string method of our items model we
        # create a new item and then assert if the name is
        # returned when we render the item as a string.
        item = Item.objects.create(name='Test Todo Item')
        self.assertEqual(str(item), 'Test Todo Item')
