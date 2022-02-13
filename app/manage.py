from app.modules import User
from app import app, db
from flask_script import Manager

manager = Manager(app)

@manager.shell
def make_shell_context():
    return dict(app=app , db =db , User = User)
if __name__=='__main__':
    manager.run()