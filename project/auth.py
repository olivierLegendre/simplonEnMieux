from flask import Blueprint, render_template, redirect, url_for, request, flash, session, Response
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, login_required, logout_user
# from .models import User
# from .modeles.utilisateur import ModeleUtilisateur

# from .modeles.apprenant import creation_apprenant, ModeleApprenant
from .modeles.apprenant_certification import ModeleApprenant, creation_apprenant
from datetime import datetime, date

from .modeles.admin import ModeleAdmin

from . import db

auth = Blueprint('auth', __name__)

@auth.route('/login')
def login()-> Response:
    return render_template('login.html')

@auth.route('/login', methods=["POST"])
def login_post() -> Response:
    form = request.form
    login = form.get("login")
    mdp = form.get("mdp")
    
    user = ModeleApprenant.query.filter_by(login=login).first()
    if not user:
        flash("Verifier vos login / mot de passe")
        return redirect(url_for('auth.login'))
    if not check_password_hash(user.mdp, mdp):
        flash("Mauvais mot de passe , Oui j'ai honte")
        return redirect(url_for('auth.login'))

    session["user"] = user.to_dict()
    session["user_type"] = "appprenant"
    login_user(user, remember="remember")
    return redirect(url_for('main.profile'))

@auth.route('/signup')
def signup()-> Response:
    return render_template('signup.html')

@auth.route('/signup', methods=['POST'])
def signup_post()-> Response:
    # get the data from the form
    form = request.form
    nom = form.get("nom")
    prenom = form.get("prenom")
    email = form.get("email")
    login = form.get("login")
    mdp = form.get("mdp")
    date_creation = str(date.today())
    
    # if this returns a user, then the email already exists in database
    user_by_email = ModeleApprenant.query.filter_by(email=email).first()
    # if this returns a user, then the login already exists in database
    user_by_login = ModeleApprenant.query.filter_by(login=login).first()
    
    if user_by_login is not None:
        flash('Login address already exists')
        return redirect(url_for('auth.signup'))
    if user_by_email is not None:
        flash('Email address already exists')
        return redirect(url_for('auth.signup'))
    
    #create a new user
    #hash the password
    apprenant = creation_apprenant(email=email, nom=nom, prenom=prenom, date_creation=date_creation , login=login, mdp=generate_password_hash(mdp))
    db.session.commit()
    
    return redirect(url_for('auth.login'))

@auth.route('/logout')
@login_required
def logout()-> Response:
    logout_user()
    return redirect(url_for('main.index'))