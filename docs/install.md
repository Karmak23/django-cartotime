
# Installation sommaire de cartotime

Création d'un environnement virtuel pour cloisonner le projet :

	pip install virtualwrapper
	mkvirtualenv cartotime

Installation du projet :

	git clone github.com:CapSciences/django-cartotime
	cd django-cartotime
	pip install -r requirements.txt

Création de la base de données initiale (SQLite3, par défaut) :

	cd cartotime
	./manage syncdb
	# création de l'utilisateur "admin"…

Lancement du server web (ne pas trop le charger, sinon passer à gunicorn ou µWSGI) :

	./manage runserver 0.0.0.0:8000

L'interface est accessible sur http://localhost:8000/

L'interface d'administration de Django est à http://localhost:8000/admin/
