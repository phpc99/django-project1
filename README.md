A simple Django project created as a first step to learn the framework and practice core concepts like views, templates, and URL routing.
It displays three different pages: **Home**, **About**, and **Contact**. None of them have been styled with CSS yet, but styling will be added soon as the next step in the learning process.

# How to Run the Project

Follow these steps to run this Django project on your machine.

## 1. **Clone the repository**

`git clone https://github.com/phpc99/django-project1.git `
`cd django-project1` 

## 2. **Create a virtual environment**

`python -m venv venv` 

## 3. **Activate the virtual environment**

### Windows (PowerShell or CMD):

`venv\Scripts\activate` 

### macOS / Linux:

`source venv/bin/activate` 

You should now see `(venv)` at the start of your terminal prompt.

## 4. **Install dependencies**

`pip install -r requirements.txt` 

## 5. **Apply migrations**

`python manage.py migrate` 

## 6. **Run the development server**

`python manage.py runserver` 

## 7. **Open the website**

Go to: http://127.0.0.1:8000/
