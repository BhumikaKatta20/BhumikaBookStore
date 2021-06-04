from django.urls import path,re_path
from . import views
from django.contrib.auth import views as auth_views
urlpatterns=[
	path('',views.index,name='index'),
	path('index/',views.index,name='index'),
    path('SignUp/',views.SignUp,name='SignUp'),
    path('Store_User/',views.Store_User,name='Store_User'),
	path('Login/', views.login, name="login"),
	path('Logout/', views.logout, name="logout"),
	path('AddNewBook/', views.AddNewBook, name="AddNewBook"),
	path('view_Stores/',views.view_Stores,name='view_Stores'),
	path('view_Stores/(?P <user_name>[\W-]+)',views.info,name='info'),
	path('view_Stores/(? <id>[\W-]+)',views.getbook,name='getbook'),
	path('Update_list/',views.Update_list,name='Update_list'),
	path('Update_list/(?P <id>[\W-]+)',views.Update_record,name='Update_record'),
	path('Delete_book/',views.Delete_book,name='Delete_book'),
	path('Delete_book/(?P <id>[\W-]+)',views.Delete_record,name='Delete_record'),
]
