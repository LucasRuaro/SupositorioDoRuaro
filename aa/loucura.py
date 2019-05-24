from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo

class UserForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    password2 = PasswordField(
        'Repeat Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Registrar')

from flask import Flask
from flask import render_template
from forms.usuarioForm import UserForm

app = Flask(__name__)
app.config.update(SECRET_KEY = 'you-will-never-guess')

@app.route('/')
@app.route('/index')
def index():
    form = UserForm()
    return render_template("index.html", title='Home Page', form = form)

@app.route("/registrar", methods=["post"])
def registrar():
    form = UserForm()
    print(form.username.data)


app.run()