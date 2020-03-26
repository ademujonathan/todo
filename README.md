#pip install django

To upgrade
#pip install --upgrade django==3.0

To make a directory for the installation,

#mkdir c:\   location of your directory.

#pip install virtualenv
	or
#pip3 install virtualenv
# virtualenv.


#pip install django

#django-admin.py startproject "Project Name"
To check the list of file installed

#ls

To enter the file you created.
# cd file path\file name

To start the server
#python manage.py runserver

stop your server and migrate
#python manage.py migrate

To create Admin userName and password:
#python manage.py createsuperuser

#python manage.py runserver
localhost:8000/Admin

Once Django is set,

stop server:
create your app.
#python manage.py startapp "tasks"





setting. py add project name: 'tasks'

=======>
 set views function
 
To verrified your Http Response:

from django.shortcuts import render
from django.http import HttpResponse
 

def index(request):
    return HttpResponse('Hello world')
Create a urls.py on you app and link it to django 
urls.py you have as default include it.

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('tasks.urls'))
]
 
 StartUp steps:

Your new urls.py
from django.urls import path
from . import views 

urlpatterns = [
	path('', views.index)

]

You can create you templates folder
on your templates folder
====> 
create a tasks folder
======>
create your list.html,
update_task.html
delete.html


 
