from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
from apps.models import Item
from apps.models import List

# Create your views here.
def home_page(request):
	return render(request, "home/index.html")


def view_post(request, list_id):
	list_ = List.objects.get(id=list_id)
	items = Item.objects.filter(list=list_)
	return render(request, 'home/post.html', {'items':items, 'list':list_})


def new_post(request):
	list_ = List.objects.create()
	Item.objects.create(text=request.POST['item_text'], list=list_)
	return redirect('/posts/%d/' % list_.id)


def add_item(request, list_id):
	list_ = List.objects.get(id=list_id)
	Item.objects.create(text=request.POST['item_text'], list=list_)
	return redirect('/posts/%d/' % list_.id)