from flask_migrate import Migrate
from flask_script import Manager, Server

from app import create_app, db
from app.models import  User

#Creating app instance
app = create_app('production')


migrate = Migrate(app,db)


@app.shell_context_processor
def make_shell_context():
    return dict(db = db, User = User )


if __name__ == '__main__':
    app.run(debug=True)

