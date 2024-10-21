
# rm db.sqlite3
rm -rf video_course/migrations/*
rm -rf course/migrations/*
rm -rf user/migrations/*
rm -rf core/migrations/*

python manage.py migrate admin zero
python manage.py migrate auth zero
python manage.py migrate contenttypes zero
python manage.py migrate sessions zero

python manage.py makemigrations
python manage.py makemigrations user
python manage.py makemigrations core
python manage.py makemigrations video_course
python manage.py makemigrations course

python manage.py migrate
python manage.py createsuperuser

