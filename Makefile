mig:
	python3 manage.py makemigrations
	python3 manage.py migrate


app:
	python3 manage.py startapp app

run:
	python3 manage.py runserver


superuser:
	python3 manage.py createsuperuser

ws:
	daphne -b 0.0.0.0 -p 8001 config.asgi:application