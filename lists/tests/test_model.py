from django.test import TestCase
from django.template.loader import render_to_string
from lists.models import Item,List

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




