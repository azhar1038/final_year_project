# Steps to run this Django App

1. Install all requirements on the machine using pip

```
pip install -r requirements.txt
```

2. Start the Django Development Server

```
python manage.py runserver
```

# Placement of model in the directory
Refer the following tree to find the location for placement of model :
```
.
├── app
├── db.sqlite3
├── manage.py
├── model.tf
├── piece.jpg
├── predictor
├── README.md
├── requirements.txt
└── templates

4 directories, 6 files
```

# Full Directory structure for reference only

```
.
├── app
│   ├── admin.py
│   ├── apps.py
│   ├── __init__.py
│   ├── migrations
│   │   └── __init__.py
│   ├── models.py
│   ├── tests.py
│   ├── utils.py
│   └── views.py
├── db.sqlite3
├── manage.py
├── model.tf
│   ├── assets
│   ├── saved_model.pb
│   └── variables
│       ├── variables.data-00000-of-00001
│       └── variables.index
├── piece.jpg
├── predictor
│   ├── asgi.py
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── README.md
├── requirements.txt
└── templates
    └── home.html

7 directories, 23 files

```