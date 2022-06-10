# learning-material
# community-pot


clone & cd

```git clone https://github.com/Licceeee/community-pot.git && cd community-pot```

create venv

```virtualenv -p python3 venv```

activate venv

```source venv/bin/activate```

install dependencies

```poetry install```

migrate db

```python3 manage.py makemigrations```

```python3 manage.py migrate```


apply static files

```python3 manage.py collectstatic```

create superuser

```python3 manage.py createsuperuser```

start

```python3 manage.py runserver```

hit 
localhost:port/admin to enter the admin panel with credentials created 
with createsuperuser

e.g with standard port
```localhost:8000/admin```

----

production settings

rename project/project/production_settings.example.py to production_settings.py

replace placeholders with your credentials
