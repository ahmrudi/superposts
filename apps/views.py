from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
from apps.models import Item

# Create your views here.
def home_page(request):
	return render(request, "home/index.html")


def view_post(request):
	items = Item.objects.all()
	return render(request, 'home/post.html', {'items':items})


def new_post(request):
	Item.objects.create(text=request.POST['item_text'])
	return redirect('/posts/posts-your-heart-with-god/')