#pip install flask-bcrypt
from flask_bcrypt import Bcrypt

password = 'Test'

bcrypt = Bcrypt()

hashed_password = bcrypt.generate_password_hash(password=password)

#Store in data base




#take out hashed password

enteredpassword = 'Test'

check = bcrypt.check_password_hash(hashed_password,enteredpassword)

#check = True or False







