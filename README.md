# Check python version
```
I:\>python --version
Python 3.10.11
```
# Check PIP version
```
I:\mydjangofirst>pip --version
pip 23.0.1 from C:\Users\ATUL\AppData\Local\Programs\Python\Python310\lib\site-packages\pip (python 3.10)
```
# create virtual environment
<b>Command</b>:python -m venv virtualEnvironmentName
```
I:\mydjangofirst>python -m venv venv
```
# activate virtual environmet
```
I:\mydjangofirst>venv\Scripts\activate.bat
(venv) I:\mydjangofirst>
```
# deactivate virtual environment
```
(venv) I:\mydjangofirst>venv\Scripts\deactivate.bat
I:\mydjangofirst>
```
# install Django with specific version
1. activate the virtual environment
```
(venv) I:\mydjangofirst>python -m pip install Django==4.2.1
Collecting Django==4.2.1
  Using cached Django-4.2.1-py3-none-any.whl (8.0 MB)
Collecting asgiref<4,>=3.6.0
  Using cached asgiref-3.6.0-py3-none-any.whl (23 kB)
Collecting tzdata
  Using cached tzdata-2023.3-py2.py3-none-any.whl (341 kB)
Collecting sqlparse>=0.3.1
  Using cached sqlparse-0.4.4-py3-none-any.whl (41 kB)
Installing collected packages: tzdata, sqlparse, asgiref, Django
Successfully installed Django-4.2.1 asgiref-3.6.0 sqlparse-0.4.4 tzdata-2023.3

[notice] A new release of pip is available: 23.0.1 -> 23.1.2
[notice] To update, run: python.exe -m pip install --upgrade pip

(venv) I:\mydjangofirst>
```
# Check django version
```
(venv) I:\mydjangofirst>python -m django --version
4.2.1
```
# Check help
```
(venv) I:\mydjangofirst\mydjangodoc>python manage.py help

Type 'manage.py help <subcommand>' for help on a specific subcommand.

Available subcommands:

[auth]
    changepassword
    createsuperuser

[contenttypes]
    remove_stale_contenttypes

[django]
    check
    compilemessages
    createcachetable
    dbshell
    diffsettings
    dumpdata
    flush
    inspectdb
    loaddata
    makemessages
    makemigrations
    migrate
    optimizemigration
    sendtestemail
    shell
    showmigrations
    sqlflush
    sqlmigrate
    sqlsequencereset
    squashmigrations
    startapp
    startproject
    test
    testserver

[sessions]
    clearsessions

[staticfiles]
    collectstatic
    findstatic
    runserver

```

# Create Project
<b>Command:</b>
django-admin startproject projectName
```
(venv) I:\mydjangofirst>django-admin startproject mydjangodoc

(venv) I:\mydjangofirst>
```

# Run the Django Project (Start the development server)
<b>Command:</b>
python manage.py runserver
```
(venv) I:\mydjangofirst\mydjangodoc>python manage.py runserver
Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).

You have 18 unapplied migration(s). Your project may not work properly until you apply the migrations for app(s): admin, auth, contenttypes, sessions.
Run 'python manage.py migrate' to apply them.
May 12, 2023 - 10:46:45
Django version 4.2.1, using settings 'mydjangodoc.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CTRL-BREAK.
```
# MySQL connection with Django
```
DATABASES = {  
    'default': {  
        'ENGINE': 'django.db.backends.mysql',  
        'NAME': 'mydjangodoc',  
        'USER':'root',  
        'PASSWORD':'',  
        'HOST':'localhost',  
        'PORT':'3306'  
    }  
} 
```
Note: If you are getting error of mysqlclient then install mysql client

# install mysqlclient
```
(venv) I:\mydjangofirst\mydjangodoc>pip install mysqlclient
Collecting mysqlclient
  Downloading mysqlclient-2.1.1-cp310-cp310-win_amd64.whl (178 kB)
     ---------------------------------------- 178.4/178.4 kB 672.8 kB/s eta 0:00:00
Installing collected packages: mysqlclient
Successfully installed mysqlclient-2.1.1

[notice] A new release of pip is available: 23.0.1 -> 23.1.2
[notice] To update, run: python.exe -m pip install --upgrade pip

(venv) I:\mydjangofirst\mydjangodoc>
```

# show migrations
```
(venv) I:\mydjangofirst\mydjangodoc>python manage.py showmigrations
admin
 [ ] 0001_initial
 [ ] 0002_logentry_remove_auto_add
 [ ] 0003_logentry_add_action_flag_choices
auth
 [ ] 0001_initial
 [ ] 0002_alter_permission_name_max_length
 [ ] 0003_alter_user_email_max_length
 [ ] 0004_alter_user_username_opts
 [ ] 0005_alter_user_last_login_null
 [ ] 0006_require_contenttypes_0002
 [ ] 0007_alter_validators_add_error_messages
 [ ] 0008_alter_user_username_max_length
 [ ] 0009_alter_user_last_name_max_length
 [ ] 0010_alter_group_name_max_length
 [ ] 0011_update_proxy_permissions
 [ ] 0012_alter_user_first_name_max_length
contenttypes
 [ ] 0001_initial
 [ ] 0002_remove_content_type_name
sessions
 [ ] 0001_initial
```
Note-1: [] indicates migration files are not migrate
Note-2: [X] indicates migration files are migrated

# show migration of specific app
```
(venv) I:\mydjangofirst\mydjangodoc>python manage.py showmigrations auth
auth
 [X] 0001_initial
 [X] 0002_alter_permission_name_max_length
 [X] 0003_alter_user_email_max_length
 [X] 0004_alter_user_username_opts
 [X] 0005_alter_user_last_login_null
 [X] 0006_require_contenttypes_0002
 [X] 0007_alter_validators_add_error_messages
 [X] 0008_alter_user_username_max_length
 [X] 0009_alter_user_last_name_max_length
 [X] 0010_alter_group_name_max_length
 [X] 0011_update_proxy_permissions
 [X] 0012_alter_user_first_name_max_length
```

# migrate all migrations
```
(venv) I:\mydjangofirst\mydjangodoc>python manage.py migrate
Operations to perform:
  Apply all migrations: admin, auth, contenttypes, sessions
Running migrations:
  Applying contenttypes.0001_initial... OK
  Applying auth.0001_initial... OK
  Applying admin.0001_initial... OK
  Applying admin.0002_logentry_remove_auto_add... OK
  Applying admin.0003_logentry_add_action_flag_choices... OK
  Applying contenttypes.0002_remove_content_type_name... OK
  Applying auth.0002_alter_permission_name_max_length... OK
  Applying auth.0003_alter_user_email_max_length... OK
  Applying auth.0004_alter_user_username_opts... OK
  Applying auth.0005_alter_user_last_login_null... OK
  Applying auth.0006_require_contenttypes_0002... OK
  Applying auth.0007_alter_validators_add_error_messages... OK
  Applying auth.0008_alter_user_username_max_length... OK
  Applying auth.0009_alter_user_last_name_max_length... OK
  Applying auth.0010_alter_group_name_max_length... OK
  Applying auth.0011_update_proxy_permissions... OK
  Applying auth.0012_alter_user_first_name_max_length... OK
  Applying sessions.0001_initial... OK
```
# reverse(rollback) all migration of an app
If you want to reverse all migrations applied for an app, use the name zero:
```
(venv) I:\mydjangofirst\mydjangodoc>python manage.py migrate auth zero
Operations to perform:
  Unapply all migrations: auth
Running migrations:
  Rendering model states... DONE
  Unapplying auth.0012_alter_user_first_name_max_length... OK
  Unapplying auth.0011_update_proxy_permissions... OK
  Unapplying auth.0010_alter_group_name_max_length... OK
  Unapplying auth.0009_alter_user_last_name_max_length... OK
  Unapplying auth.0008_alter_user_username_max_length... OK
  Unapplying auth.0007_alter_validators_add_error_messages... OK
  Unapplying auth.0006_require_contenttypes_0002... OK
  Unapplying auth.0005_alter_user_last_login_null... OK
  Unapplying auth.0004_alter_user_username_opts... OK
  Unapplying auth.0003_alter_user_email_max_length... OK
  Unapplying auth.0002_alter_permission_name_max_length... OK
  Unapplying admin.0003_logentry_add_action_flag_choices... OK
  Unapplying admin.0002_logentry_remove_auto_add... OK
  Unapplying admin.0001_initial... OK
  Unapplying auth.0001_initial... OK
```
# migrate all migration of specific app
```
(venv) I:\mydjangofirst\mydjangodoc>python manage.py migrate auth
Operations to perform:
  Apply all migrations: auth
Running migrations:
  Applying auth.0001_initial... OK
  Applying auth.0002_alter_permission_name_max_length... OK
  Applying auth.0003_alter_user_email_max_length... OK
  Applying auth.0004_alter_user_username_opts... OK
  Applying auth.0005_alter_user_last_login_null... OK
  Applying auth.0006_require_contenttypes_0002... OK
  Applying auth.0007_alter_validators_add_error_messages... OK
  Applying auth.0008_alter_user_username_max_length... OK
  Applying auth.0009_alter_user_last_name_max_length... OK
  Applying auth.0010_alter_group_name_max_length... OK
  Applying auth.0011_update_proxy_permissions... OK
  Applying auth.0012_alter_user_first_name_max_length... OK
```

# reverse(rollback) to previous migrations
suppose that your 0012 migtration migrated but you want to reverse to previouse migration like 0011 <br>
<b>command: python manage.py migrate auth [previous migration number]</b>
```
(venv) I:\mydjangofirst\mydjangodoc>python manage.py migrate auth 0011
Operations to perform:
  Target specific migration: 0011_update_proxy_permissions, from auth
Running migrations:
  Rendering model states... DONE
  Unapplying auth.0012_alter_user_first_name_max_length... OK
```

# migrate only one migration file
```
(venv) I:\mydjangofirst\mydjangodoc>python manage.py migrate auth 0012
Operations to perform:
  Target specific migration: 0012_alter_user_first_name_max_length, from auth
Running migrations:
  Applying auth.0012_alter_user_first_name_max_length... OK
```
# create an app in Django
<b>Command: python manage.py startapp [appname]</b>
```
(venv) I:\mydjangofirst\mydjangodoc>python manage.py startapp productmanagement
```
# Register app
Open the setting.py file
```
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'user',
    'productmanagement',
]
```
# create migration for all app
It create the migrations for all apps.<br>
<b>Command: python manage.py makemigrations</b>
```
(venv) I:\mydjangofirst\mydjangodoc>python manage.py makemigrations
Migrations for 'productmanagement':
  productmanagement\migrations\0001_initial.py
    - Create model Category
```
# create migration for a specific app
It create the migrations for a specific app.<br>
<b>Command: python manage.py makemigrations [app_name]</b>
```
(venv) I:\mydjangofirst\mydjangodoc>python manage.py makemigrations productmanagement
Migrations for 'productmanagement':
  productmanagement\migrations\0001_initial.py
    - Create model Category
```
# create the meaningfull migration file name
--name is used to create meaningfull migration file name
```
(venv) I:\mydjangofirst\mydjangodoc>python manage.py makemigrations --name=create_long_description_field productmanagement
Migrations for 'productmanagement':
  productmanagement\migrations\0025_create_long_description_field.py
    - Add field lg_description to category
```
# Show the sql query of migration
<b>Command: python manage.py sqlmigrate [app_name] [migration_name]</b>
```
(venv) I:\mydjangofirst\mydjangodoc>python manage.py sqlmigrate productmanagement 0001
--
-- Create model Category
--
CREATE TABLE `productmanagement_category` (`id` bigint AUTO_INCREMENT NOT NULL PRIMARY KEY, `category_name` varchar(120) NOT NULL);
```
# migrate the migration file
<b>Command: python manage.py migrate [app_name] [migration_name] </b>
```
(venv) I:\mydjangofirst\mydjangodoc>python manage.py migrate productmanagement 0001
Operations to perform:
  Target specific migration: 0001_initial, from productmanagement
Running migrations:
  Applying productmanagement.0001_initial... OK
```
# Create a simple model
Write code in models.py file of app
```
from django.db import models

class Category(models.Model):
    category_name = models.CharField(max_length=120)
```
Note: Django create table name automaticaly <b>appname_modelclassname</b><br>
Note: Django automatically create auto incremented field with primary key. Field name will be id.

#  To specify table name and auto incremented field name with primary key in database
Write code in models.py file of app
```
from django.db import models

class Category(models.Model):
    cat_id = models.BigAutoField(primary_key=True)
    category_name = models.CharField(max_length=120)
    
    class Meta:
        db_table = 'categories'
```
Note: cat_id = models.BigAutoField(primary_key=True) used to create auto incremented field with primary key. field name is cat_id
Note: db_table = 'categories' used in meta class to create table name. Here table name is categories.

# db_column used to write database table field name according to you
```
from django.db import models

class Category(models.Model):
    cat_id = models.BigAutoField(primary_key=True)
    category_name = models.CharField(max_length=120,null=True)
    category_code = models.CharField(max_length=50,null=True,unique=True)
    description = models.CharField(max_length=50,null=True)
    sh_description = models.CharField(max_length=10,null=True,db_column='short_description')
    class Meta:
        db_table = 'categories'
```
Note: db_column used to create field name according to you. <b>sh_description = models.CharField(max_length=10,null=True,db_column='short_description')</b> according to this code database table field name will be short_description not sh_description. If you do not used db_column then database field name will be sh_description.<br>
Note: db_column is very usefull when you want to create database table filed name from python keyword. And it is also usefull when you create field name for foreign key because Django automatically append <b>_id</b> in field name.

# Create a nullable field
Note: write code in models.py file of app<br>
If null=True, Django will store empty values as NULL in the database. Default is False.
```
from django.db import models

class Category(models.Model):
    cat_id = models.BigAutoField(primary_key=True)
    category_name = models.CharField(max_length=120,null=True)
    
    class Meta:
        db_table = 'categories'
```
# Create a unique filed
Note: write code in models.py file of app<br>
If unique=True used then unique field will be create.
```
from django.db import models

class Category(models.Model):
    cat_id = models.BigAutoField(primary_key=True)
    category_name = models.CharField(max_length=120,null=True)
    category_code = models.CharField(max_length=50,null=True,unique=True)
    
    class Meta:
        db_table = 'categories'
```
# Organizing models in a package
<p>The manage.py startapp command creates an application structure that includes a models.py file. If you have many models, organizing them in separate files may be useful.</p>
<p>To do so, create a models package. Remove models.py and create a myapp/models/ directory with an __init__.py file and the files to store your models. You must import the models in the __init__.py file. For example, if you had organic.py and synthetic.py in the models directory:</p>
<p>myapp/models/__init__.py</p>

```
from .organic import Person
from .synthetic import Robot

```
<p>Explicitly importing each model rather than using from .models import * has the advantages of not cluttering the namespace, making code more readable, and keeping code analysis tools useful.</p>

# create super user 
```
(venv) I:\mydjangofirst\mydjangodoc>python manage.py createsuperuser
Username (leave blank to use 'atul'): atulkrishnathakur
Email address: atul@yopmail.com
Password:
Password (again):
This password is too common.
This password is entirely numeric.
Bypass password validation and create user anyway? [y/N]: y
Superuser created successfully.
```
start the development server by <b>python manage.py runserver</b> command. Now, open a Web browser and go to “/admin/” on your local domain – e.g., http://localhost:8000/admin/. You should see the admin’s login screen

# how to add model to show in Django adminstration for super user
Step1: open the admin.py file from app. here projectmanagement/admin.py
Step2: register the model in admin.py file
```
from django.contrib import admin

# Register your models here.
from .models.categories import Category

admin.site.register(Category)
```
# open the admin login screen 
http://localhost/admin <br>
enter the username and password

# show the data instead of Category object (1) in Admin
When you display a Model as a list, Django displays each record as the string representation of the record object, which in our case is "Member object (1)", "Member object(2)". <br>

To change this to a more reader-friendly format, we have two choices: <br>

Change the string representation function, __str__() of the Member Model <br>
Set the list_details property of the Member Model <br>

To change the string representation, we have to define the __str__() function of the models, like this:
```
from django.db import models

class Category(models.Model):
    cat_id = models.BigAutoField(primary_key=True)
    category_name = models.CharField(max_length=120,null=True)
    category_code = models.CharField(max_length=50,null=True,unique=True)
    description = models.CharField(max_length=50,null=True)
    sh_description = models.CharField(max_length=10,null=True,db_column='short_description')
    lg_description = models.CharField(max_length=20,null=True,db_column='long_description')
    class Meta:
        db_table = 'categories'
    def __str__(self):
        return f"{self.categoryname} {self.description}"
 
```
# Show the list data instead of Category object (1) in Admin
1. If you want to show the list of module in admin then write code in **productmanagement/admin.py**
2. create a class CategoryListAdmin
3. list_display tuple with DB table fielname. Note list_display name do not change
4. register create class with and model
```
from django.contrib import admin

# Register your models here.
from .models.categories import Category

#admin.site.register(Category)

class CategoryListAdmin(admin.ModelAdmin):
  list_display = ("category_name", "category_code", "description",)
  
admin.site.register(Category, CategoryListAdmin)
```
# view in Django
A view function, or view for short, is a Python function that takes a web request and returns a web response. This response can be the HTML contents of a web page, or a redirect, or a 404 error, or an XML document, or an image . . . or anything, really. <br>
When you create an app then <b>views.py</b> file will created by django with the following code.
```
from django.shortcuts import render

# Create your views here.

```

# Types of views in django
1. Function-Based Views
2. Class-Based Views

# Function based views
A view is a function that takes an HttpRequest object and returns an HttpResponse object.<br>

write a simple view function in *productmanagement/views.py*
```from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse('<h1>Hello World</h1>')

def about(request):
    return HttpResponse('<h1>About</h1>')
```

# create urls in app directory
1. create urls.py file in app directory like *productmanagement/urls.py*
2. Write bellow code in urls.py file of directory like *productmanagement/urls.py*
```
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
]
```
Note1: The path() function is passed four arguments, two required: route and view, and two optional: kwargs, and name.<br>
**route**: Route is a string that contains a URL pattern.<br>
**view**: When Django finds a matching pattern, it calls the specified view function with an HttpRequest object as the first argument and any “captured” values from the route as keyword arguments.<br>
**kwargs**: Arbitrary keyword arguments can be passed in a dictionary to the target view.<br>
**name**: Naming your URL lets you refer to it unambiguously from elsewhere in Django, especially from within templates. This powerful feature allows you to make global changes to the URL patterns of your project while only touching a single file.

# include urls in urls.py file of project
1. write bellow code in urls.py file of project like *mydjangodoc/mydjangodoc/urls.py*
```
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('product/',include('productmanagement.urls')),
]
```
Note1: Type http://localhost:8000/product/ url in browser <br>
Note2: Type http://localhost:8000/product/about/ url in browser

# configure the template directory
**create a base template directory**
   1. create a **templates** directory in project directory like *mydjangodoc/templates/*. This is the sibling of manage.py file.
   2. Now configrue the base templates directory
   3. open the setting.py file and write bellow code
   ```
   TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]
   ```
**create the templates for app**
1. create the **templates** directory in app directory like *productmanagement/templates/*
2. create the **productmanagement** directory inside template directory like *productmanagement/templates/productmanagement/*
3. create the home.html file like *productmanagement/templates/productmanagement/home.html*
4. create the about.html file like *productmanagement/templates/productmanagement/about.html*

# render tempolate file from view
*productmanagement/views.py*
```
from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse('<h1>Hello World</h1>')

def about(request):
    return HttpResponse('<h1>About</h1>')
    
def home_temp(request):
    return render(request,'productmanagement/home.html')
    
def about_temp(request):
    return render(request,'productmanagement/about.html')    
```

*productmanagement/urls.py*
```
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('home-temp/', views.home_temp, name='hometemp'),
    path('about-temp/', views.about_temp, name='abouttemp'),
]
```

# extends the base html template
1. creata a base html file in project template directory like *mydjangodoc/templates/productmanagementbase.html
```
<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="UTF-8" />
        <meta name="viewport" content="width=device-width, initial-scale=1.0" />
        <title>Title</title>
    </head>
    <body>
        {% block content %}
        {% endblock %}
    </body>
</html>

```
2. extends  *productmangementbase.html* into *productmanagement/templates/productmanagement/home.html*
```
{% extends 'productmangementbase.html' %}
{% block content %}
<h1>Home Page</h1>
{% endblock content %}
```

note: "content" is the name of block


# include common  html template
1. creata a base html file in project template directory like *mydjangodoc/templates/productmanagementbase.html
```
<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="UTF-8" />
        <meta name="viewport" content="width=device-width, initial-scale=1.0" />
        <title>Title</title>
    </head>
    <body>
        {% block content %} {% endblock %}
		{% block footercontent %} {% endblock %}
    </body>
</html>
```
2. extends  *productmangementbase.html* into *productmanagement/templates/productmanagement/home.html*
3. include the footer.html file
```
{% extends 'productmanagementbase.html' %}
{% block content %}
<h1>Home Page</h1>
{% endblock content %}

{% block footercontent %}
{% include "productmanagement/include/footer.html" %}
{% endblock footercontent %}
```
