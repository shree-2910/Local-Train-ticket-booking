from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Home Page
@app.route('/')
def home():
    return render_template('home.html')

# Register Page
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        # Later we’ll add code here to save the user in the database
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']
        print(f"New user registered: {name}, {email}")
        return redirect(url_for('home'))
    return render_template('register.html')

# Login Page (we’ll create this next)
@app.route('/login')
def login():
    return render_template('login.html')

if __name__ == '__main__':
    app.run(debug=True)
