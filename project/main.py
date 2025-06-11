from flask import Blueprint, render_template, session, request, flash
from flask_login import login_required, current_user
from .modeles.apprenant_certification import ModeleApprenant
from .schemas.apprenant import NiveauEtude
from datetime import datetime
from . import db

main = Blueprint('main', __name__)

@main.route("/")
def index():
    return render_template('index.html')

@main.route('/profile')
@login_required
def profile():
    user = session["user"]
    select_niveau_etude = NiveauEtude.get_select()
    data = {"user": user, "select_niveau_etude": select_niveau_etude}
    return render_template('profile.html', data=data)

@main.route('/profile', methods=["POST"])
@login_required
def profile_post():
    form = request.form
    id_apprenant = form.get("id_apprenant")
    # nom = form.get("nom")
    # prenom = form.get("prenom")
    # email = form.get("email")
    # login = form.get("login")
    # mdp = form.get("mdp")
    # date_naissance = form.get("date_naissance")
    # niveau_etude = form.get("niveau_etude")
    # commentaire = form.get("commentaire")
    
    user = ModeleApprenant.query.filter_by(id_apprenant=id_apprenant).first()
    print(repr(user))
    user.nom = form.get("nom")
    user.prenom = form.get("prenom")
    user.email = form.get("email")
    date_naissance = form.get("date_naissance")
    user.date_naissance = datetime.strptime(date_naissance, '%Y-%m-%d') if date_naissance else None
    user.niveau_etude = form.get("niveau_etude")
    user.commentaire = form.get("commentaire")
    db.session.commit()
    session["user"] = user.to_dict()
    # user = ModeleApprenant.query.filter_by(id_apprenant=id_apprenant).first()
    print(repr(user))
    flash("Merci d'avoir mis a jour votre profil")
    select_niveau_etude = NiveauEtude.get_select()
    data = {"user": user, "select_niveau_etude": select_niveau_etude}
    return render_template('profile.html', data=data)