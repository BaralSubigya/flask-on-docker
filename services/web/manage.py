from flask.cli import FlaskGroup
from project import create_app, db
from project.models import User

app = create_app()
cli = FlaskGroup(create_app=create_app)

@cli.command("create_db")
def create_db():
    with app.app_context():
        db.create_all()

@cli.command("seed_db")
def seed_db():
    with app.app_context():
        if not User.query.filter_by(username="michael").first():
            db.session.add(User(username="michael"))
        if not User.query.filter_by(username="dwight").first():
            db.session.add(User(username="dwight"))
        db.session.commit()

if __name__ == "__main__":
    cli()
