# simplonEnMieux

#pour utiliser flask
export FLASK_APP=app
export FLASK_ENV=development

flask run

#Pour utiliser Migrate

flask db init
flask db migrate -m "nom de la migration"
flask db upgrade
