from django.shortcuts import render, redirect
from .models import Item


# Create your views here.
def get_todo_list(request):
    items = Item.objects.all()
    context = {
        'items': items
    }
    return render(request, 'todo/todo_list.html', context)


# If add item url is clicked - if it is a get request, we will just return the
# the add_item.html but if it is a post request, we will get the information
# from the form to create a new item and then redirect to the get_todo_list
# view in order to display all.
def add_item(request):
    if request.method == "POST":
        name = request.POST.get('item_name')
        done = 'done' in request.POST
        Item.objects.create(name=name, done=done)

        return redirect('get_todo_list')
    return render(request, 'todo/add_item.html')
