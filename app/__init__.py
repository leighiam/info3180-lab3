from flask import Flask
from flask_mail import Mail
from flask_wtf.csrf import CSRFProtect


csrf = CSRFProtect()


app = Flask(__name__)
app.config['SECRET_KEY'] = '95b257ab06509d95dd64848a1a323b0dd399657a75b2b6685f'
csrf.init_app(app)
app.config['MAIL_SERVER'] = 'smtp.mailtrap.io' 
app.config['MAIL_PORT'] = '465' # (or try 2525) 
app.config['MAIL_USERNAME'] = 'username'
app.config['MAIL_PASSWORD'] = 'password'

mail = Mail(app)
from app import views
