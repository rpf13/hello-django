from django.test import TestCase
from .models import Item

# To test the views, we use the Django included test client to check the sites.


class TestViews(TestCase):

    def test_get_todo_list(self):
        # we just want to access the main html site (home)
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'todo/todo_list.html')

    def test_get_add_item_page(self):
        response = self.client.get('/add')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'todo/add_item.html')

    def test_get_edit_item_page(self):
        # In order to edit an item, we need an item id. To be generic
        # and not have to refer to a specific one we import the Item
        # from .models
        # We create a Test Todo Item
        item = Item.objects.create(name='Test Todo Item')
        response = self.client.get(f'/edit/{item.id}')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'todo/edit_item.html')

    def test_can_add_item(self):
        # We test if we can add an item and get redirected back to the
        # main page - home
        response = self.client.post('/add', {'name': 'Test Added Item'})
        self.assertRedirects(response, '/')

    def test_can_delete_item(self):
        item = Item.objects.create(name='Test Todo Item')
        response = self.client.get(f'/delete/{item.id}')
        self.assertRedirects(response, '/')
        # we want to check if it really got deleted, so we filter on all
        # existing items and since we have created only one, it should be 0
        existing_items = Item.objects.filter(id=item.id)
        self.assertEqual(len(existing_items), 0)

    def test_can_toggle_item(self):
        # we create a new item with done set to true
        item = Item.objects.create(name='Test Todo Item', done=True)
        # we call the toggle view on the item id to toggle status
        response = self.client.get(f'/toggle/{item.id}')
        self.assertRedirects(response, '/')
        # finally we assert the changed state
        updated_item = Item.objects.get(id=item.id)
        self.assertFalse(updated_item.done)

    def test_can_edit_item(self):
        item = Item.objects.create(name='Test Todo Item')
        # in order to test the edit POST method, we will update the name
        response = self.client.post(f'/edit/{item.id}', {'name': 'Updated Name'})  # noqa
        self.assertRedirects(response, '/')
        updated_item = Item.objects.get(id=item.id)
        self.assertEqual(updated_item.name, 'Updated Name')
