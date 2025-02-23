from flask import Blueprint, render_template, request, redirect, url_for, flash
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, logout_user, login_required, current_user
from models import db, User
from routes import Blockchain

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        password = generate_password_hash(request.form['password'], method='pbkdf2:sha256')
        age = request.form['age']
        phone = request.form.get('phone')  # Capture phone number
        country = request.form['country']
        state = request.form['state']
        height = request.form['height']
        weight = request.form['weight']
        blood_group = request.form['blood_group']
        alcohol = request.form['alcohol']
        smoking = request.form['smoking']
        id_card = request.form['id_card']

        existing_user = User.query.filter_by(email=email).first()
        if existing_user:
            flash('Email already exists. Please log in.', 'danger')
            return redirect(url_for('auth.login'))

        # Generate the user's Vaibhav Code (first block hash)
        blockchain = Blockchain()
        vaibhav_code = blockchain.create_genesis_block(email)

        new_user = User(name=name, email=email, password=password, age=age, country=country,
                        state=state, height=height, weight=weight, blood_group=blood_group,
                        alcohol=alcohol, smoking=smoking, id_card=id_card, vaibhav_code=vaibhav_code, phone=phone
            )

        db.session.add(new_user)
        db.session.commit()

        flash(f'Account created! Your Vaibhav Code is {vaibhav_code}', 'success')
        return redirect(url_for('auth.login'))

    return render_template('signup.html')

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        user = User.query.filter_by(email=email).first()
        if user and check_password_hash(user.password, password):
            login_user(user)  # ✅ Use Flask-Login's login_user function
            flash('Login successful!', 'success')
            return redirect(url_for('routes.dashboard'))

        flash('Invalid credentials. Please try again.', 'danger')
    
    return render_template('login.html')

@auth_bp.route('/logout')
@login_required  # ✅ Require user to be logged in to logout
def logout():
    logout_user()  # ✅ Use Flask-Login's logout_user function
    flash('You have been logged out.', 'info')
    return redirect(url_for('auth.login'))