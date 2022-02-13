class User:
    """
    Init method that helps defie properties of our objects
    """
    """
    ARGS:
        firstName: Users first name
        lastNmae: Users last name
        email: Users email address
        password: Users password
        password2: Password confirmation
    """
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