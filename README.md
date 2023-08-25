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

# custom user 
'Django' highly recomended that create a custom user and custom user model. If you not create custom user model then django create problem when you want to alter auth_user table. You can also create custom user in mid level of project but it some dificult.

1. create customusers app. You can also use users name for app.
2. create Model CustomUser. You can also use 'User' name for model 
   ```
from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class CustomUser(AbstractUser):
    phone = models.CharField(max_length=20,null=True,db_column='phone')
    
    class Meta:
        db_table = 'auth_user'
   ```
3. register custom user in setting.py
4. AUTH_USER_MODEL = "user.CustomUser" add this in settings.py  
5. now use any where in your code
```
from user.models import CustomUser
```

# How to create Custom User after some development in Django
1. Create the users app
```
python manage.py startapp users

``` 
2. Add the following to the models.py:
```
from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    class Meta:
        db_table = 'auth_user'
```
Note: If you don't specify the name, you'll receive an error "django.db.utils.OperationalError: no such table: users_customuser"

3. Register the new Model in the admin panel:
```
# In users/admin.py
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    model = CustomUser

admin.site.register(CustomUser, CustomUserAdmin)
```
4. Register the users app in setting.py 
INSTALLED_APPS = [
    .....,
	.....,
    'users',
    .....,
	.....
]

4. Add following in setting.py file.
```
AUTH_USER_MODEL = "users.CustomUser"
```
5. Replace Users imports

In your project code, replace all imports of the Django User model:

```
from django.contrib.auth.models import User

```
with the new, custom one:
```
from user.models import CustomUser

```

5. Delete Old Migrations

Run the following two commands in your terminal, from the root of your project:

command-1: find . -path "*/migrations/*.py" -not -name "__init__.py" -delete
command-2: find . -path "*/migrations/*.pyc" -delete

Note: You can also manualy delete all migrations file with .py extension and .pyc extension

6. Create New Migrations
```
python manage.py makemigrations

```

7. Truncate or delete data of the django_migrations table

Note: Now you can add new field in auth_user table 

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
2. create the **productmanagement** directory inside templates directory like *productmanagement/templates/productmanagement/*
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
4. if a common html in full project then create html file for include in template directory of project
```
{% extends 'productmanagementbase.html' %}
{% block content %}
<h1>Home Page</h1>
{% endblock content %}

{% block footercontent %}
{% include "productmanagement/include/footer.html" %}
{% endblock footercontent %}
```

# static configuration
1. write the code in setting.py file
```
STATIC_URL = 'static/'
STATICFILES_DIRS = [BASE_DIR / 'static']
```

2. create the **static** directory in app directory like *productmanagement/static/*
3. create the **productmanagement** directory inside static directory like *productmanagement/static/productmanagement/*
4. create the **css** directory inside productmanagement directory like *productmanagement/static/productmanagement/css/*
5. create the **style.css** directory inside css directory like *productmanagement/static/productmanagement/css/style.css*

Note: same way use for js and image

*productmanagement/static/productmanagement/css/style.css*
```
.head{
	background-color:red;
	color:white;
}
```

*productmanagement/static/productmanagement/js/main.js*
```
console.log("Hello World");
```

*mydjangodoc/templates/productmanagementbase.html*
```
<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="UTF-8" />
        <meta name="viewport" content="width=device-width, initial-scale=1.0" />
        <title>{% block contenttitle %}{% endblock contenttitle %}</title>
    </head>
    <body>
	    {% block csscontent %} {% endblock %}
        {% block content %} {% endblock %}
		{% block footercontent %} {% endblock %}
		{% block jscontent %} {% endblock %}
    </body>
</html>
```
*productmanagement/templates/productmanagement/home.html*
```
{% extends 'productmanagementbase.html' %}
{% load static %}

{% block csscontent %} 
<link rel="stylesheet" href="{% static 'productmanagement/css/style.css' %}">
{% endblock csscontent %}

{% block contenttitle %} Home Page {% endblock contenttitle %}

{% block content %}
<h1 class="head">Home Page</h1>
{% endblock content %}

{% block jscontent %} 
<script src="{% static 'productmanagement/js/main.js' %}" ></script>
{% endblock jscontent %}

{% block footercontent %}
{% include "productmanagement/include/footer.html" %}
{% endblock footercontent %}
```
Note: extendes will be the first element.
Note: If you want to create common statics then create the static directory in project like in *mydjangodoc/static/css/style.css*
Note: If you have small project then you can use static from project directory but you have multiple app in your project then create statics in app.

# Organizing views in a package
step-1: remove views.py file from app directory<br>
step-2: create the views directory in app<br>
step-3: create the __init__.py file in app directory like *productmanagement/views/__init__.py*<br>
step-4: create the files in views directory like *productmanagement/views/product.py*<br>
step-5: Import all view file in __init__.py file 
```
from .category import *
from .product import *
```
step-6: import the views from views directory in *productmanagement/urls.py* 
```
from django.urls import path
from .views import category
from .views import product

urlpatterns = [
    path('', category.home, name='home'),
    path('about/', category.about, name='about'),
    path('home-temp/', category.home_temp, name='hometemp'),
    path('about-temp/', category.about_temp, name='abouttemp'),
    path('showdata/', category.show_data, name='showdata'),
]
```

# Edit Admin 
1. click on username link in admin to open and edit user details
2. Here you can add an user to group 
3. Here You can add user to permision


# Create Group for Users and Permission
1. click on add group in admin 
2. Enter Name: ....name of group....
3. Save

# How to write own config in settings in Django
In Django, you can create your own configuration settings using the settings.py file, which is a Python module that holds all the configuration options for your Django project. Here's a step-by-step guide on how to write your own config in Django:

1. Open the settings.py file:
First, locate the settings.py file in your Django project. It is typically located in the project's root directory.

2. Define your custom configuration settings:
In the settings.py file, you can add your own configuration settings as attributes of the module. You can use any Python variable name to define your settings. For example, let's create a custom setting called "MY_CUSTOM_SETTING":

```python
# settings.py
MY_CUSTOM_SETTING = 'Hello, this is my custom setting!'
```

3. Use the custom setting in your code:
Once you have defined your custom setting, you can use it in your Django project code. For example, let's say you want to use the "MY_CUSTOM_SETTING" in one of your views:

```python
# views.py
from django.conf import settings
from django.http import HttpResponse

def my_view(request):
    custom_setting_value = settings.MY_CUSTOM_SETTING
    return HttpResponse(custom_setting_value)
```

4. Accessing the custom setting from other parts of the project:
You can access the custom setting from any part of your Django project by importing the `settings` object as shown above. This includes views, models, forms, middleware, and other modules within your project.

5. Default values for custom settings:
You can provide default values for your custom settings in case they are not set in the settings.py file. This can be done using the `getattr` function along with the `default` argument:

```python
# settings.py
MY_CUSTOM_SETTING = getattr(settings, 'MY_CUSTOM_SETTING', 'This is the default value.')
```

By using `getattr`, Django will first attempt to retrieve the setting from the settings.py file, and if it's not found, it will use the default value you specified.

6. Using environment variables:
For sensitive information or configurations that may vary depending on the deployment environment, it is a good practice to use environment variables. Django allows you to read environment variables as custom settings. To do this, you need to import the `os` module and use `os.environ` to access environment variables:

```python
# settings.py
import os

MY_SECRET_KEY = os.environ.get('MY_SECRET_KEY', 'default_secret_key')
```

By using this approach, you can set the value of `MY_SECRET_KEY` as an environment variable on your server, which can be kept separate from your source code repository.

Remember to restart your Django server or development environment whenever you make changes to the settings.py file for the changes to take effect. Also, make sure to handle sensitive information securely and follow best practices for managing configurations in production environments.


In Django, you can create constants by defining them in a separate Python module and then importing that module wherever you need to use the constants. This approach allows you to centralize the constants and reuse them throughout your Django project.

Here's a step-by-step guide on how to create constants in Django:

1. Create a new Python module for constants:
In your Django app, create a new Python file (e.g., constants.py) to store your constants. It's a good practice to name the file in a way that reflects its purpose.

```
your_app/
    ├── __init__.py
    ├── models.py
    ├── views.py
    ├── constants.py   # <-- Create this file
    └── ...
```

2. Define constants in the constants.py module:
In the constants.py file, you can define your constants using regular Python variables. For example:

```python
# constants.py

# Example of integer constant
MAXIMUM_RETRIES = 5

# Example of string constant
DEFAULT_USERNAME = "guest"

# Example of list constant
VALID_STATUSES = ["ACTIVE", "INACTIVE"]

# Example of dictionary constant
ERROR_CODES = {
    "NOT_FOUND": 404,
    "SERVER_ERROR": 500,
}
```

3. Import and use the constants in your Django code:
Now that you have defined your constants in constants.py, you can import and use them in other parts of your Django app, such as views, models, or other utility modules.

```python
# views.py
from django.shortcuts import render
from .constants import MAXIMUM_RETRIES, DEFAULT_USERNAME, VALID_STATUSES

def my_view(request):
    max_retries = MAXIMUM_RETRIES
    default_username = DEFAULT_USERNAME
    valid_statuses = VALID_STATUSES

    # Your view logic here...
    return render(request, "template_name.html", context)
```

By following this approach, you can easily manage your constants in one place, making it more maintainable and reducing the chance of typos or inconsistencies when using the same constant in multiple places.

Remember that constants defined in this manner are still mutable in Python. If you want to enforce immutability, you can use `tuple` or `frozenset` for lists and sets, respectively. For dictionaries, you can use `MappingProxyType` from the `types` module to create an immutable proxy.

Also, be cautious when defining sensitive information as constants. For sensitive data like API keys or passwords, it's better to use environment variables to keep them secure and separate from your source code.

# How to create separate setting file for production and development

In Django, it's common practice to have separate settings files for different environments, such as production and development. This allows you to configure settings specific to each environment, ensuring a smooth and secure deployment process. Here's how you can create separate settings files for production and development:

1. Create separate settings files:
In your Django project, create two separate Python modules for settings: `settings.py` and `settings_production.py`. The `settings.py` file will contain the common settings applicable to all environments, while the `settings_production.py` file will include the settings specific to the production environment.

```
your_project/
    ├── your_project/
    │   ├── settings.py
    │   ├── settings_production.py
    │   └── ...
    ├── manage.py
    └── ...
```

2. Define common settings in settings.py:
In the `settings.py` file, define all the common settings shared by both the development and production environments. These could include settings like database configuration, installed apps, middleware, static files, etc.

```python
# settings.py

# Common settings applicable to all environments
INSTALLED_APPS = [
    # ... List of installed apps ...
]

# Database configuration
DATABASES = {
    # ... Database settings ...
}

# Other common settings ...
```

3. Override specific settings in settings_production.py:
In the `settings_production.py` file, override the settings specific to the production environment. For example, you might want to set `DEBUG` to False, use a different database configuration, or adjust security-related settings.

```python
# settings_production.py
from .settings import *

# Override specific settings for production environment
DEBUG = False

# Use a different database for production
DATABASES = {
    # ...
}

# Other production-specific settings ...
```

4. Set the DJANGO_SETTINGS_MODULE environment variable:
To switch between different settings files based on the environment, you need to set the `DJANGO_SETTINGS_MODULE` environment variable. In your development environment, set it to `your_project.settings`, and in your production environment, set it to `your_project.settings_production`.

For Linux/macOS terminal:

```bash
# Development environment
export DJANGO_SETTINGS_MODULE=your_project.settings

# Production environment
export DJANGO_SETTINGS_MODULE=your_project.settings_production
```

For Windows Command Prompt:

```bash
# Development environment
set DJANGO_SETTINGS_MODULE=your_project.settings

# Production environment
set DJANGO_SETTINGS_MODULE=your_project.settings_production
```

5. Use the correct settings file in manage.py:
In the `manage.py` file, modify the `os.environ.setdefault` line to use the correct settings file:

```python
# manage.py
import os
import sys

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "your_project.settings")  # Use your_project.settings_production for production
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError("Couldn't import Django. Are you sure it's installed and available on your PYTHONPATH environment variable? Did you forget to activate a virtual environment?") from exc
    execute_from_command_line(sys.argv)
```

With this setup, when you run your Django project using `python manage.py runserver`, it will use the settings from `settings.py` for development, and when deploying in a production environment, make sure to set the `DJANGO_SETTINGS_MODULE` environment variable to `your_project.settings_production`.

Remember to handle sensitive information, such as API keys or database credentials, securely in your production settings, using environment variables or a dedicated secrets manager, to ensure they are not exposed in version control or deployment scripts.


# How to configure and use bassics logging

check url: https://docs.djangoproject.com/en/4.2/howto/logging/#logging-how-to

In your settings.py:

```
LOGGING = {
    "version": 1,  # the dictConfig format version
    "disable_existing_loggers": False,  # retain the default loggers
    "handlers": {
        "file": {
            "class": "logging.FileHandler",
            "filename": "general.log",
            "level": "DEBUG",
        },
    },
    "loggers": {
        "": {
            "level": "DEBUG",
            "handlers": ["file"],
        },
    },
}
```

1. DEBUG: Low level system information for debugging purposes
2. INFO: General system information
3. WARNING: Information describing a minor problem that has occurred.
4. ERROR: Information describing a major problem that has occurred.
5. CRITICAL: Information describing a critical problem that has occurred.

Important notea:-
1. Note1: if you are using debug then debug, info,warning, error, critical messages will be print in general.log file
2. Note2: if you are using critical then debug,info,warning, error messages will not print in general.log file only critical messages will be print in general.log file.
3. Note3: if you are using warning then only debug,info,warning messages will be print in general.log file.

# loggers format 

```
LOGGING = {
    "version": 1,  # the dictConfig format version
    "disable_existing_loggers": False,  # retain the default loggers
    "formatters": {
        "verbose": {
            "format": "{name} {levelname} {asctime} {module} {process:d} {thread:d} {message}",
            "style": "{",
        },
        "simple": {
            'format': '[%(asctime)s] %(levelname)s %(message)s',
            'datefmt': '%Y-%m-%d %H:%M:%S'
        },
    },
    "handlers": {
        "file": {
            "class": "logging.FileHandler",
            "filename": "general.log",
            "level": "DEBUG",
            "formatter": "simple",
        },
    },
    "loggers": {
        "": {
            "level": "DEBUG",
            "handlers": ["file"],
        },
    },
}
```