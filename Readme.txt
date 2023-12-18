source /.venv/bin/activate

# new app
python3 manage.py startapp shop

python3 manage.py runserver

python3 manage.py runserver 9000        # port 9000

python manage.py createsuperuser

# create migration
python manage.py makemigrations

# utilization migration
python manage.py migrate