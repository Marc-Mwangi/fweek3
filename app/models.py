from . import db
class User(db.Model):

    __tablename__= 'users'
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(255))
    
    def __repr__(self):
        return f'User{self.username}'
    #class variable for user data
    user_email=[]
    user_password=[]
    #initializing class
    def  __init__(self, firstName, lastName, email, password , password2):
        self.f_Name = firstName
        self.l_name= lastName
        self.email = email
        self.password = password
        self.password2 = password2 
    
    #Saving  user email
    def save_email(self):
        User.user_email.append(self.email)

    #Saving user password
    def save_password(self):
        User.user_password.append(self.password)