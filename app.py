from project import db, create_app
from project.modeles.apprenant_certification import ModeleApprenant, ModeleCertification
from project.modeles.admin import ModeleAdmin
from project.modeles.formateur import ModeleFormateur
from project.modeles.support import ModeleSupport
from project.modeles.salle import ModeleSalle

with create_app().app_context():
    # db.create_all()
    pass