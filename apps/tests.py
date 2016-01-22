from django.test import TestCase
from django.core.urlresolvers import resolve
from django.http import HttpRequest
from django.template.loader import render_to_string


from apps.views import home_page
from apps.models import Item
from apps.models import List

# Create your tests here.
class NewPostTest(TestCase):

	def test_home_page_simpan_POST_request(self):
		self.client.post(
			'/posts/new/',
			data={'item_text': 'A new post item'}
			)

		self.assertEqual(Item.objects.count(), 1)
		new_item = Item.objects.first()
		self.assertEqual(new_item.text, 'A new post item')

	def test_home_page_redirect_setelah_POST(self):
		response = self.client.post(
			'/posts/new/',
			data={'item_text': 'A new post item'}
			)
		new_list = List.objects.first()
		self.assertRedirects(response, '/posts/%d/' % new_list.id)

	def test_simpan_POST_ke_list_yang_ada(self):
		correct_list = List.objects.create()
		other_list = List.objects.create()

		self.client.post(
			'/posts/%d/add_item' % correct_list.id,
			data={'item_text': 'Post baru untuk list yang ada'})

		self.assertEqual(Item.objects.count(), 1)

		new_item = Item.objects.first()
		self.assertEqual(new_item.text, 'Post baru untuk list yang ada')
		self.assertEqual(new_item.list, correct_list)

	def test_redirects_to_list_view(self):
		other_list = List.objects.create()
		correct_list = List.objects.create()

		response = self.client.post(
			'/posts/%d/add_item' % correct_list.id,
			data={'item_text': 'Post baru untuk list yang ada'})

		self.assertRedirects(response, '/posts/%d/' % correct_list.id)

class PostViewTest(TestCase):

	def test_pakai_post_template(self):
		list_ = List.objects.create()
		response = self.client.get('/posts/%d/' % (list_.id, ))
		self.assertTemplateUsed(response, 'home/post.html')

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

	def test_home_page_tampilkan_semua_list_item_post(self):
		list_ = List.objects.create()
		Item.objects.create(text='posted 1', list=list_)
		Item.objects.create(text='posted 2', list=list_)

		response = self.client.get('/posts/%d/' % list_.id)

		self.assertContains(response, 'posted 1')
		self.assertContains(response, 'posted 2')

	def test_tampilan_hanya_item_untuk_post_atau_list(self):
		correct_list = List.objects.create()
		Item.objects.create(text='posted 1', list=correct_list)
		Item.objects.create(text='posted 2', list=correct_list)

		other_list = List.objects.create()

		Item.objects.create(text='0 posted 1', list=other_list)
		Item.objects.create(text='0 posted 2', list=other_list)

		response = self.client.get('/posts/%d/' % (correct_list.id, ))

		self.assertContains(response, 'posted 1')
		self.assertContains(response, 'posted 2')
		self.assertNotContains(response, '0 poster 1')
		self.assertNotContains(response, '0 poster 2')



class ListAndItemModelsTest(TestCase):

	def test_simpan_listing_items(self):
		list_ = List.objects.create()

		item_satu = Item()
		item_satu.text = "Item satu"
		item_satu.list = list_
		item_satu.save()

		item_dua = Item()
		item_dua.text = "Item dua"
		item_dua.list = list_
		item_dua.save()

		item_tiga = Item()
		item_tiga.text = "Item tiga"
		item_tiga.list = list_
		item_tiga.save()

		list_tersimpan = List.objects.first()
		self.assertEqual(list_tersimpan, list_)

		item_tersimpan = Item.objects.all()
		self.assertEqual(item_tersimpan.count(), 3)

		item_tersimpan_satu = item_tersimpan[0]
		item_tersimpan_dua = item_tersimpan[1]
		item_tersimpan_tiga = item_tersimpan[2]
		self.assertEqual(item_tersimpan_satu.text, "Item satu")
		self.assertEqual(item_tersimpan_satu.list, list_)
		self.assertEqual(item_tersimpan_dua.text, "Item dua")
		self.assertEqual(item_tersimpan_dua.list, list_)
		self.assertEqual(item_tersimpan_tiga.text, "Item tiga")
		self.assertEqual(item_tersimpan_tiga.list, list_)