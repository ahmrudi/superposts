from django.test import TestCase
from django.core.urlresolvers import resolve
from django.http import HttpRequest
from django.template.loader import render_to_string


from apps.views import home_page
from apps.models import Item

# Create your tests here.
class HomePageTest(TestCase):

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
		self.assertEqual(response.status_code, 200)

	def test_home_page_simpan_POST_request(self):
		request = HttpRequest()
		request.method = 'POST'
		request.POST['item_text'] = 'A new post item'

		response = home_page(request)

		self.assertEqual(Item.objects.count(), 1)
		new_item = Item.objects.first()
		self.assertEqual(new_item.text, 'A new post item')

	def test_home_page_redirect_setelah_POST(self):
		request = HttpRequest()
		request.method = 'POST'
		request.POST['item_text'] = 'A new post item'

		response = home_page(request)

		self.assertEqual(response.status_code, 302)
		self.assertEqual(response['location'], '/')

	def test_home_page_tampilkan_semua_list_item_post(self):
		Item.objects.create(text='posted 1')
		Item.objects.create(text='posted 2')

		request = HttpRequest()
		response = home_page(request)

		self.assertIn('posted 1', response.content.decode())
		self.assertIn('posted 2', response.content.decode())
		


class ItemModelTest(TestCase):

	def test_simpan_listing_items(self):

		item_satu = Item()
		item_satu.text = "Item satu"
		item_satu.save()

		item_dua = Item()
		item_dua.text = "Item dua"
		item_dua.save()

		item_tiga = Item()
		item_tiga.text = "Item tiga"
		item_tiga.save()

		item_tersimpan = Item.objects.all()
		self.assertEqual(item_tersimpan.count(), 3)

		item_tersimpan_satu = item_tersimpan[0]
		item_tersimpan_dua = item_tersimpan[1]
		item_tersimpan_tiga = item_tersimpan[2]
		self.assertEqual(item_tersimpan_satu.text, "Item satu")
		self.assertEqual(item_tersimpan_dua.text, "Item dua")
		self.assertEqual(item_tersimpan_tiga.text, "Item tiga")