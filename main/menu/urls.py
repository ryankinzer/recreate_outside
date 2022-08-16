# blog/urls.py
from django.urls import path
from .views import MenuList, MenuNew, MenuEdit, MenuDelete

urlpatterns = [
	path('', MenuList.as_view(), name = 'menu'),
	path('new/', MenuNew.as_view(), name='menu_new'),
    path('edit/<int:pk>', MenuEdit.as_view(), name='menu_edit'),
    path('<int:pk>/delete', MenuDelete.as_view(), name='menu_delete'),
]