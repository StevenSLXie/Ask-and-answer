from django.shortcuts import redirect,render
from lists.models import Item,List

# Create your views here.
def home_page(request):
	#if request.method == 'POST':
	#	new_item_text = request.POST['item_text']
	#	Item.objects.create(text=new_item_text)
	#	return redirect('/lists/the-only-list-in-the-world/')

	#items = Item.objects.all()
	#for i in items:
		#print i
	return render(request,'home.html')

	#item = Item()
	#item.text = request.POST.get('item_text','')
	#item.save()
	#return HttpResponse('<html><title>To-Do lists</title></html>')
	#return render(request,'home.html',{'new_item_text':request.POST.get('item_text',''),})

def view_list(request):
    items = Item.objects.all()
    return render(request, 'list.html', {'items': items})

def new_list(request):
    list_ = List.objects.create()
    Item.objects.create(text=request.POST['item_text'],list=list_)
    return redirect('/lists/the-only-list-in-the-world/')
