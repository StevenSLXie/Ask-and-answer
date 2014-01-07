from django.shortcuts import redirect,render
from lists.models import Item,List
from django.core.exceptions import ValidationError


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

def view_list(request,list_id):
    list_ = List.objects.get(id=list_id)
    if request.method == 'POST':
        Item.objects.create(text=request.POST['item_text'], list=list_)
        return redirect('/lists/%d/' % (list_.id,))
    return render(request, 'list.html', {'list': list_})


def new_list(request):
    list_ = List.objects.create()
    try:
		Item.objects.create(text=request.POST['item_text'],list=list_)
    except ValidationError:
		error_text = 'You can\'t have an empty list item'
		return render(request,'home.html',{'error':error_text})
    return redirect('/lists/%d/' % (list_.id,))

def add_item(request,list_id):
    list_ = List.objects.get(id=list_id)
    Item.objects.create(text=request.POST['item_text'], list=list_)
    return redirect('/lists/%d/' %(list_.id,))
