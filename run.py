# from app import create_app
#
# app = create_app()
#
# if __name__ == "__main__":
#     app.run(debug=True)
from app import create_app, db
from flask_migrate import MigrateCommand
# from flask_script import Manager # i removed this as it is not needed again
from flask.cli import AppGroup

app = create_app()
migrate = Migrate(app, db)

# for cli commands
cli = AppGroup('cli')

@cli.command('create_db')
def create_db():
    """Create the database tables."""
    with app.app_context():
        db.create_all()
        print("Database initialized and tables created.")

app.cli.add_command(cli)
# manager = Manager(app)
# manager.add_command('db', MigrateCommand)

# if __name__ == "__main__":
#     with app.app_context():
#         db.create_all()  # will create the tables
#         print("Database initialized and tables created.")
#     app.run(debug=True)
#
if __name__ == "__main__":
    app.run(debug=True)
