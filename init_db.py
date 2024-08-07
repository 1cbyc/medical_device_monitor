# from your_application import create_app, db
#
# app = create_app()
# with app.app_context():
#     db.create_all()

from app import create_app, db
from app.models import DeviceData  # will import the new models here

app = create_app()

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
        print("Database initialized and tables created.")
    app.run(debug=True)
