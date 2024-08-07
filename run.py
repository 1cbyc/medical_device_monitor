# from app import create_app
#
# app = create_app()
#
# if __name__ == "__main__":
#     app.run(debug=True)
from flask_migrate import MigrateCommand
from flask_script import Manager

app = create_app()

manager = Manager(app)
manager.add_command('db', MigrateCommand)

if __name__ == "__main__":
    with app.app_context():
        db.create_all()  # will create the tables
        print("Database initialized and tables created.")
    app.run(debug=True)
