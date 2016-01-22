from django.test import TestCase
from django.core.urlresolvers import resolve
from django.http import HttpRequest
from django.template.loader import render_to_string


from apps.views import home_page

# Create your tests here.
class PostWebTests(TestCase):

	def test_untuk_mengetes_testcase(self):
		'''2 x 2 = 4'''
		self.assertEqual(4, 2*2)

	def test_home_page(self):
		'''cek eksistensi function home page'''
		found = resolve('/')
		self.assertEqual(found.func, home_page)

	def test_html_home_page(self):
		'''cek html pada home page'''
		request = HttpRequest()
		response = home_page(request)
		self.assertTrue(response.content.startswith(b'<!DOCTYPE html>'))
		self.assertIn(b'<title>Super Posts</title>', response.content)
		self.assertTrue(response.content.endswith(b'</html>'))

	def test_home_page_cocok_dengan_template(self):
		request = HttpRequest()
		response = home_page(request)
		expected_html = render_to_string('home/index.html')
		self.assertEqual(response.content.decode(), expected_html)

	def test_home_page_simpan_POST_request(self):
		request = HttpRequest()
		request.method = 'POST'
		request.POST['item_text'] = 'A new post item'

		response = home_page(request)
		self.assertIn('A new post item', response.content.decode())
		expected_html = render_to_string(
			'home/index.html',
			{'new_item_text': 'A new post item'}
			)
		self.assertEqual(response.content.decode(), expected_html)