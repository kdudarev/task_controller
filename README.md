# Task controller

The **[task controller](https://github.com/kdudarev/task_controller)** is a tool used to represent work and its path towards completion. You can create a task, assign it to a user, set a deadline, priority, and track the progress.

### Technology Stack:
- **[Python](https://www.python.org/)** - programming language (3.9.6)
- **[HTML](https://html.com/)** - markup language (HTML5)
- **[Django](https://www.djangoproject.com/)** - Python Web framework (4.0.3)
- **[PostgreSQL](https://www.postgresql.org/)** - object-relational database system (PostgreSQL 14)
- **[Bootstrap](https://getbootstrap.com/)** - HTML, CSS and JavaScript framework (django-bootstrap4 22.1)

# Installation

**1. Clone this repository:**
```
git clone https://github.com/kdudarev/task_controller.git
```
**2. Change SECRET_KEY in settings.py:**
```
SECRET_KEY = "Your Secret Key"
```
**3. Change DATABASES in settings.py to yours or use the example:**
```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
```
**4. Use virtualenv to install requirements:**
```
pip install -r requirements.txt
```
**5. Run the migration:**
```
python manage.py migrate
```
**6. Create super user:**
```
python manage.py createsuperuser
```
**7. Start the server:**
```
python manage.py runserver
```
