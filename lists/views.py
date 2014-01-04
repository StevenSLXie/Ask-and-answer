from django.shortcuts import render

# Create your views here.
def home_page(request):
	#return HttpResponse('<html><title>To-Do lists</title></html>')
	return render(request,'home.html',{'new_item_text':request.POST.get('item_text',''),})
