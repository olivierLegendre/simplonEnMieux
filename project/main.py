from flask import (
    Blueprint,
    render_template,
    session,
    request,
    flash,
    redirect,
    url_for,
    Response,
)
from flask_login import login_required, logout_user
from .modeles.apprenant_certification import ModeleApprenant, maj_apprenant
from .schemas.apprenant import NiveauEtude
from datetime import datetime
from . import db

main = Blueprint("main", __name__)


@main.route("/")
def index():
    return render_template("index.html")


@main.route("/profile")
@login_required
def profile() -> Response:
    """
    affiche le profil utilsateur
    Returns:
        Response: page profile
    """
    user = session["user"]
    select_niveau_etude = NiveauEtude.get_select()
    data = {"user": user, "select_niveau_etude": select_niveau_etude}
    return render_template("profile.html", data=data)


@main.route("/profile", methods=["POST"])
@login_required
def profile_post() -> Response:
    """
    gere le post sur le profil
    offre la possiblité de l'editer et de le supprimer
    Returns:
        Response: page profile
    """
    
    form = request.form
    id_apprenant = form.get("id_apprenant")

    user = ModeleApprenant.query.filter_by(id_apprenant=id_apprenant).first()
    date_naissance = form.get("date_naissance")
    user_is_valid = maj_apprenant(
        user,
        nom=form.get("nom"),
        prenom=form.get("prenom"),
        email=form.get("email"),
        date_naissance=datetime.strptime(date_naissance, "%Y-%m-%d")
        if date_naissance
        else None,
        niveau_etude=form.get("niveau_etude"),
        commentaire=form.get("commentaire"),
    )
    if user_is_valid:
        db.session.commit()

    session["user"] = user.to_dict()
    flash("Merci d'avoir mis a jour votre profil")
    select_niveau_etude = NiveauEtude.get_select()
    data = {"user": user, "select_niveau_etude": select_niveau_etude}
    return render_template("profile.html", data=data)


@main.route("/delete", methods=["POST"])
@login_required
def profile_delete() -> Response:
    """
    Suppression de l'utilsateur actuel

    Returns:
        Response: page login
    """
    form = request.form
    id_apprenant = form.get("id_apprenant")

    ModeleApprenant.query.filter_by(id_apprenant=id_apprenant).delete()
    db.session.commit()
    logout_user()
    del session["user"]
    flash("Vous avez supprimé votre profil")
    return redirect(url_for("auth.login"))
