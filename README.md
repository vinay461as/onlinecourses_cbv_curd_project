# onlinecourses_cbv_curd_project
This is an online course selling project based on class-based views with add, edit, view, and delete operation. This project includes template creation, static folder setup, and integration of bootstrap framework with Django crispy forms.

# Install Required Packages
The project was built and tested with Django 3.x version.The Django project need some Python package to install
```
pip install Django
pip install django-crispy-forms
```
# Running the Application
Before running the application we need to create the needed DB tables:
```
python manage.py makemigrations
python manage.py migrate
 ```
Now run the server
```
python manage.py runserver
```
To access the applications, go to the URL http://localhost:8000/

