# Makefile
	
run:
	python manage.py runserver

migrate:
	python manage.py makemigrations
	python manage.py migrate

heroku:
	git push heroku master

lint:
	flake8
