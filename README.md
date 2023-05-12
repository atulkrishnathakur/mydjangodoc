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
D:\mydjangofirst>venv\Scripts\activate.bat

(venv) D:\mydjangofirst>
```
# deactivate virtual environment
```
(venv) D:\mydjangofirst>venv\Scripts\deactivate.bat
D:\mydjangofirst>
```
# install Django with specific version
1. activate the virtual environment
```
(venv) D:\mydjangofirst>python -m pip install Django==4.2.1
```
# Check django version
```
(venv) D:\mydjangofirst>python -m django --version
4.2.1
```
# Create Project
<b>Command:</b>
django-admin startproject projectName
```
(venv) D:\mydjangofirst>django-admin startproject mydjangodoc

(venv) D:\mydjangofirst>
```

# Run the Django Project
<b>Command:</b>
python manage.py runserver
```
(venv) D:\mydjangofirst\mydjangodoc>python manage.py runserver
Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).

You have 18 unapplied migration(s). Your project may not work properly until you apply the migrations for app(s): admin, auth, contenttypes, sessions.
Run 'python manage.py migrate' to apply them.
May 11, 2023 - 10:43:31
Django version 4.2.1, using settings 'mydjangodoc.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CTRL-BREAK.
```
