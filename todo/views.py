from django.shortcuts import render, redirect, get_object_or_404
from .models import Item
from .forms import ItemForm


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
# view in order to display all. We use the Django forms and therefore Django
# will check if the form is valid or not.
# The form will be instantiated and a hash with the result will be returned.
def add_item(request):
    if request.method == "POST":
        form = ItemForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('get_todo_list')
    form = ItemForm()
    context = {
        'form': form
    }
    return render(request, 'todo/add_item.html', context)


# The form in the edit section gets prepopulated data,
# form = ItemForm(instance=item), and item in this case is the data we got
# from the database (1st line). The part in between this, will make sure that
# once we update the form, the data will be populated.
def edit_item(request, item_id):
    item = get_object_or_404(Item, id=item_id)
    if request.method == "POST":
        form = ItemForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
        return redirect('get_todo_list')
    form = ItemForm(instance=item)
    context = {
        'form': form
    }
    return render(request, 'todo/edit_item.html', context)


# Similar to above's views. The item.done = not item.done will get
# the current state and flip the state, so if toggled then untoggle
# and vice versae. The item will then be saved and we get redirected
# to the mian get_todo_list view.
def toggle_item(request, item_id):
    item = get_object_or_404(Item, id=item_id)
    item.done = not item.done
    item.save()
    return redirect('get_todo_list')


# This view is pretty much the same as obove, just to delete the items
# and redirect back.
def delete_item(request, item_id):
    item = get_object_or_404(Item, id=item_id)
    item.done = not item.done
    item.delete()
    return redirect('get_todo_list')
