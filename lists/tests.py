from django.core.urlresolvers import resolve
from django.test import TestCase
from django.http import HttpRequest
from django.template.loader import render_to_string
from lists.models import Item,List
from lists.views import home_page

class HomePageTest(TestCase):

    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/')
        self.assertEqual(found.func, home_page)
	
    
    def test_home_page_only_saves_items_when_necessary(self):
        request = HttpRequest()
        home_page(request)
        self.assertEqual(Item.objects.all().count(),0)

class ListAndItemModelTest(TestCase):
	def test_saving_and_retrieving_items(self):
		list_ = List()
		list_.save()

		first_item = Item()
		first_item.text = 'The first (ever) list item'
		first_item.list = list_
		first_item.save()

		second_item = Item()
		second_item.text = 'Item the second'
		second_item.list = list_
		second_item.save()

		saved_lists = List.objects.all()
		self.assertEqual(saved_lists.count(),1)
		self.assertEqual(saved_lists[0],list_)
		saved_items = Item.objects.all()
		self.assertEqual(saved_items.count(),2)

		first_saved_item = saved_items[0]
		second_saved_item = saved_items[1]
		self.assertEqual(first_saved_item.text,'The first (ever) list item')
		self.assertEqual(first_saved_item.list,list_)
		self.assertEqual(second_saved_item.text,'Item the second')
		self.assertEqual(second_saved_item.list,list_)

class ListViewTest(TestCase):
    def test_uses_list_template(self):
        response = self.client.get('/lists/%d/' % (list_.id,))
        self.assertTemplateUsed(response,'list.html')

    def test_displays_all_items(self):
        correct_list = List.objects.create()
        Item.objects.create(text='itemey 1',list=correct_list)
        Item.objects.create(text='itemey 2',list=correct_list)

		other_list = List.objects.create()
		Item.objects.create(text='other list item 1',list=other_list)
		Item.objects.create(text='other list item 2',list=other_list)
        response = self.client.get('/lists/%d/' % (correct_list.id,)) #1

        self.assertContains(response, 'itemey 1') 
        self.assertContains(response, 'itemey 2') 
		self.assertNotContains(response,'other list item 1')
		self.assertNotContains(response,'other list item 2')

class NewListTest(TestCase):
    def test_saving_a_POST_request(self):
        self.client.post('/lists/new',data={'item_text': 'A new list item'})
        self.assertEqual(Item.objects.all().count(), 1)
        new_item = Item.objects.all()[0]
        self.assertEqual(new_item.text, 'A new list item')

    def test_redirects_after_POST(self):
        response = self.client.post('/lists/new',data={'item_text': 'A new list item'})
		#self.assertEqual(response.status_code, 302)
		#self.assertEqual(response['location'], '/lists/the-only-list-in-the-world/')
        self.assertRedirects(response,'/lists/the-only-list-in-the-world/')




