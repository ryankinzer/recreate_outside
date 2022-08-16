from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Menu, MenuItems
from .forms import MenuForm, MenuItemsForm
from django.urls import reverse_lazy

# Create your views here.
class MenuList(ListView):
	model = Menu
	template_name = 'menu/menu.html'
	#ordering = ['-id']
	ordering = ['-meal', 'category', 'name']

class MenuNew(CreateView):
	model = Menu
	form_class = MenuForm
	template_name = 'menu/menu_new.html'
	#fields = '__all__'
	#field = ('title', 'uploaded_by', 'primary_author', 'secondary_authors', 'body')

class MenuEdit(UpdateView):
	model = Menu
	form_class = MenuForm
	template_name = 'menu/menu_edit.html'
	#fields = '__all__'

class MenuDelete(DeleteView):
	model = Menu
	template_name = 'menu/menu_delete.html'
	success_url = reverse_lazy('menu')