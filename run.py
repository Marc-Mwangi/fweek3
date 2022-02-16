from app import create_app, db
from flask_script import Manager,Server
from app.models import User
from flask_migrate import Migrate, MigrateCommand
from flask_login import LoginManager

from app.models import User

app = create_app('production')
app.config.update(dict(
    SECRET_KEY="powerful secretkey",
    WTF_CSRF_SECRET_KEY="a csrf secret key"
))


manager = Manager(app)
manager.add_command('server',Server)

migrate = Migrate(app,db)
manager.add_command('db', MigrateCommand)


@manager.shell
def make_shell_context():
    return dict(app=app, db = db, User= User)


if __name__ == '__main__':
    manager.run()