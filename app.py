from flask import Flask , render_template , request , session , redirect , url_for
from forms import RegistrationForm , validators

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("home.html")
@app.route('/login')
def login():
    return render_template("login.html")

@app.route("/submit" , methods=["POST"])
def submit():
    form=RegistrationForm(request.form)
    if form.validate():
        username=request.form['username']
        email=request.form['email']
        return f"Hello {username} ! , Your email address is {email}"
    
    else:
        return "Invalid data please try again"
@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('home'))

@app.route("/mountains")
def mountain():
    return render_template("mountains.html")

@app.route("/lakes")
def lakes():
    return render_template("lakes.html")
@app.route("/contact")
def contact():
    return render_template("contact.html")

app.run(debug=False , host='0.0.0.0')