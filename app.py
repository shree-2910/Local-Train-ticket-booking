from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'  # Required for flashing messages


# -----------------------------
# HOME ROUTE
# -----------------------------
@app.route('/')
def home():
    return render_template('home.html')


# -----------------------------
# REGISTER ROUTE
# -----------------------------
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        password = request.form.get('password')

        # Simple validation
        if not name or not email or not password:
            flash('All fields are required!', 'error')
            return redirect(url_for('register'))

        # TODO: Save user to database here
        print(f"✅ New user registered: {name} ({email})")

        flash('Registration successful! You can now log in.', 'success')
        return redirect(url_for('login'))

    return render_template('register.html')


# -----------------------------
# LOGIN ROUTE
# -----------------------------
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        # TODO: Validate user from database
        if email == "admin@example.com" and password == "admin":
            flash('Login successful! Welcome back.', 'success')
            return redirect(url_for('home'))
        else:
            flash('Invalid email or password. Try again.', 'error')
            return redirect(url_for('login'))

    return render_template('login.html')


# -----------------------------
# MAIN DRIVER
# -----------------------------
if __name__ == '__main__':
    app.run(debug=True)
