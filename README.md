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
# django-admin command
```
(venv) I:\mydjangofirst>django-admin

Type 'django-admin help <subcommand>' for help on a specific subcommand.

Available subcommands:

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
    runserver
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
Note that only Django core commands are listed as settings are not properly configured (error: Requested setting INSTALLED_APPS, but settings are not configured. You must either define the environment variable DJANGO_SETTINGS_MODULE or call settings.configure() before accessing settings.).
```

# Create Project
<b>Command:</b>
django-admin startproject projectName
```
(venv) I:\mydjangofirst>django-admin startproject mydjangodoc

(venv) I:\mydjangofirst>
```

# Run the Django Project
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
