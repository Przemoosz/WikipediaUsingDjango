# Wikipedia using Django

This is my own project in Django 3.2.8, it's called wikipedia. It main reason is to create a page which will contain all information about my field of study which is electrical science, information like courses, Instructors, students, etc. The database used in this project is PostgreSQL. This project is unfinished because now I'm focused on .NET 6 and ASP.NET Core MVC 6 with EF, see my projects in .NET technology on my GitHub

## Installation

Make sure you have installed python 3.9.2

Install PostgreSQL or change database system in wikipedia\settings.py

Activate virtual environment using cmd, type:

```bash
.\Scripts\activate
```
In wikipedia\settings.py apply your own secret code:
```python
SECRET_KEY = 'Type your own secret key'
```
Make the migration to set up a database with tables, to achieve this go to wikipedia folder:
```bash
cd wikipedia
py manage.py migration
```
Create Super User (Admin) by typing:
```bash
py manage.py createsuperuser
```
Run the server and enjoy the page:
```bash
py manage.py runserver
```

Note: if there occurs any error with the missing package, make sure you have it installed!
