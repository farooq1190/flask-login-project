from flask import Flask, render_template, request
from flask import session, redirect, url_for
from werkzeug.security import generate_password_hash, check_password_hash


app = Flask(__name__)

app.secret_key = 'secret123'

USER = {
    'username': 'admin',
    'password': generate_password_hash('1234')
}

@app.route('/')
def home():
    return "Home Page"

@app.route('/login', methods =['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if (
            username == USER['username'] and 
            check_password_hash(USER['password'], password)
        ):
            session['user'] = username
            return redirect(url_for('dashboard'))
            #return "Login successful!"
        else:
            return "Invalid credentials, please try again."
        
    return render_template('login.html')  # Ensure you have a login.html template in the templates folder

@app.route('/dashboard')
def dashboard():
    if 'user' in session:
        return render_template('dashboard.html')
    return redirect(url_for('login'))

@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect(url_for('login'))

if __name__ == "__main__":
    app.run(debug=True)
