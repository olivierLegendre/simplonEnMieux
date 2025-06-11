from project import db, create_app

def main():
    #pass the create_app result so Flask-SQLAlchemy gets the configuration.
    # db.create_all(app = create_app())
    
    with create_app().app_context():
        db.create_all()
        pass
    
if __name__ == "__main__":
    main()

