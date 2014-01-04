from django.core.urlresolvers import resolve
from django.test import TestCase
from django.http import HttpRequest
from django.template.loader import render_to_string

from lists.views import home_page

class HomePageTest(TestCase):

    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/')
        self.assertEqual(found.func, home_page)

	
    def test_home_page_can_save_a_POST_request(self):
		print 'test'
		request = HttpRequest()
		request.method = 'POST'
		request.POST['item_text'] = 'A new list item'
	
		response = home_page(request)

		#expected_html = render_to_string('home.html')
		#self.assertEqual(response.content.decode(), expected_html)
		#print response.content.decode()
		self.assertIn('A new list item',response.content.decode())

		expected_html = render_to_string('home.html',{'new_item_text':  'A new list item'})
		#print expected_html
		self.assertEqual(response.content.decode(), expected_html)
'''
	def test_home_page_can_save_a_POST_request(self):
		request = HttpRequest()
		request.method = 'POST'
		request.POST['item_text'] = 'A new list item'

		response = home_page(request)

		self.assertIn('A new list item', response.content.decode())
'''


