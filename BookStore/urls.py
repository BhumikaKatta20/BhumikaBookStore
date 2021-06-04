from django.contrib import admin
from django.urls import path,include
from Book_Store import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('Book_Store.urls')),

]
