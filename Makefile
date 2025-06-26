mig:
	python3 manage.py makemigrations
	python3 manage.py migrate


app:
	python3 manage.py startapp app

run:
	python3 manage.py runserver


superuser:
	python3 manage.py createsuperuser