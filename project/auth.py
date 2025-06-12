from flask import (
    Blueprint,
    render_template,
    redirect,
    url_for,
    request,
    flash,
    session,
    Response,
)
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, login_required, logout_user
from .modeles.apprenant_certification import ModeleApprenant, creation_apprenant
from datetime import date

from . import db

auth = Blueprint("auth", __name__)


@auth.route("/login")
def login() -> Response:
    """
    affiche la form login
    Returns:
        Response: url de la page login
    """
    return render_template("login.html")


@auth.route("/login", methods=["POST"])
def login_post() -> Response:
    """
    Gere le post du login
    Redirige vers le login si l'utilisateur n'existe pas 
    ou si le mdp n'est pas bon
    Redirige vers la page de profil si l'utilsateur existe
    Returns:
        Response: url de page login ou profil
    """
    form = request.form
    login = form.get("login")
    mdp = form.get("mdp")

    user = ModeleApprenant.query.filter_by(login=login).first()
    if not user:
        flash("Verifier vos login / mot de passe")
        return redirect(url_for("auth.login"))
    if not check_password_hash(user.mdp, mdp):
        flash("Mauvais mot de passe , Oui j'ai honte")
        return redirect(url_for("auth.login"))

    session["user"] = user.to_dict()
    session["user_type"] = "appprenant"
    login_user(user, remember="remember")
    return redirect(url_for("main.profile"))


@auth.route("/signup")
def signup() -> Response:
    """
    affiche la form de creation du compte
    Returns:
        Response: page signup
    """
    return render_template("signup.html")


@auth.route("/signup", methods=["POST"])
def signup_post() -> Response:
    """
    gere le post de la creation de compte
    creer un nouvel apprenant
    Returns:
        Response: page signup
    """
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
        flash("Login address already exists")
        return redirect(url_for("auth.signup"))
    if user_by_email is not None:
        flash("Email address already exists")
        return redirect(url_for("auth.signup"))

    # create a new user
    # hash the password
    apprenant = creation_apprenant(
        email=email,
        nom=nom,
        prenom=prenom,
        date_creation=date_creation,
        login=login,
        mdp=generate_password_hash(mdp),
    )
    db.session.commit()

    return redirect(url_for("auth.login"))


@auth.route("/logout")
@login_required
def logout() -> Response:
    """
    gestion logout
    on vide la session
    Returns:
        Response: page index
    """
    logout_user()
    return redirect(url_for("main.index"))
