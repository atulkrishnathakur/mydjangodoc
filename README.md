# Check python version
```
Microsoft Windows [Version 10.0.19044.2251]
(c) Microsoft Corporation. All rights reserved.

C:\Users\ATUL>python --version
Python 3.10.11

```
# Check PIP version
```
C:\Users\ATUL>pip --version
pip 23.0.1 from C:\Users\ATUL\AppData\Local\Programs\Python\Python310\lib\site-packages\pip (python 3.10)
```
# create virtual environment
Syntax:
python -m venv virtualEnvironmentName
```
D:\mydjangofirst>python -m venv venv
D:\mydjangofirst>
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
