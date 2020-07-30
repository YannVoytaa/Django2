from django.urls import path
from . import views

urlpatterns=[
    path('',views.home,name='home'),
    path('new_search/',views.new_search,name='new_search'),
    path('login/',views.login,name='login'),
    path('register/',views.register,name='register'),
    path('delete/<int:item_id>',views.delete,name='delete')
]