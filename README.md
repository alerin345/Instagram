## Table of contents
* [General info](#general-info)
* [Technologies](#technologies)
* [Setup](#setup)

## General info
It is a smaller copy of Instagram.
The project was written for the purpose of completing the course at university.
	
## Technologies
Project is created with:
* Django
* Javascript
* Ajax
* Bootstrap4

## Setup
To run this project:

```
$easy_install virtualenv
```
Create project folder 
```
$virtualenv -p python env
```
Go to folder env/Scripts and next:
```
$activate
```
Back to project folder and next:
```
$cd Instagram
```
Install libraries:
```
$pip install django
$pip install django-extensions
$python -m pip install Pillow
$pip install django-bootstrap4
```
To run project:
```
$python manage.py runserver
```