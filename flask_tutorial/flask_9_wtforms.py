# pip install flask-WTF


from wtforms import  Form, StringField, PasswordField, SubmitField, validators
from flask import *

class RegisterForm(Form):
    name = StringField("İsim")
    surname = StringField("Soyisim")
    username = StringField("Kullanıcı İsimi")
    password = PasswordField("Parola")    
    confirm = PasswordField("Parola tekrar")
    submit = SubmitField("Kayıt")

class UsersForm(Form):
    name = StringField("İsim",validators=[validators.DataRequired("Lütfen Email giriniz")])
    surname = StringField("Soyisim",validators=[validators.DataRequired("Lütfen Email giriniz")])
    email = StringField("Email",validators=[validators.DataRequired("Lütfen Email giriniz")])
    password = PasswordField("Parola",validators=[validators.DataRequired("Lütfen parola giriniz"),
                validators.Length(min=6,max=12,message="Lütfen en az 6 en fazla 12 karakter parola giriniz"),
                validators.EqualTo(fieldname="confirm", message="Parolar uyuşmuyor")])
    confirm = PasswordField("Parola tekrar")
    submit = SubmitField("Kayıt")

app = Flask(__name__)

@app.route("/")
def index():
 
    return  render_template("block_kalitim_index.html")

@app.route("/register", methods =['POST','GET'])
def register():
    form = UsersForm()
 
    return render_template('wtf_register.html', form=form)

@app.route("/users", methods =['POST','GET'])
def users():
    try:
        if request.method == 'POST':
 
            name = request.form.get('name')
            surname = request.form.get('surname')
            email = request.form.get('email')
            password = request.form.get('password')
 
        return render_template("wtf_users.html", name=name, surname=surname, email= email, password=password)
    except:
        return render_template("wtf_users.html", hata="hata oluştu")

if __name__ =="__main__":
    app.run(debug =True)