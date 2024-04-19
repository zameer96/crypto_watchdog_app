from flask import (Blueprint, 
                   redirect, url_for, 
                   request, 
                   render_template, 
                   flash, session)
from werkzeug.security import generate_password_hash, check_password_hash
from app import db
from app.models.user import User


bp = Blueprint('auth', __name__, url_prefix='/auth')

@bp.route('/')
def index():
    return redirect(url_for('auth.login'))

@bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Handle login form submission
        email_mobile = request.form.get('email_mobile')
        password = request.form.get('password')

        # Fetch user from the database by email or mobile
        user = User.query.filter((User.email == email_mobile) | (User.mobile == email_mobile)).first()

        if user and check_password_hash(user.password, password):
            # Password matches, login successful
            flash('Login successful!', 'success')
            # Set user information in session
            session['user_id'] = user.id
            session['email'] = user.email
            session['full_name'] = f"{user.first_name} {user.last_name}"
            session['user_type'] = user.user_type
            # Redirect to dashboard if login is successful
            return redirect(url_for('dashboard.index'))
        else:
            # Invalid credentials
            flash('Invalid email/mobile or password', 'danger')

    return render_template('auth/login.html')


@bp.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        first_name = request.form.get('first_name')
        last_name = request.form.get('last_name')
        date_of_birth = request.form.get('date_of_birth')
        mobile = request.form.get('mobile')
        email = request.form.get('email')
        password = request.form.get('password')
        confirm_password = request.form.get('confirm_password')
        print(confirm_password)
        print("==========")

        # Check if passwords match
        if password != confirm_password:
            flash("Passwords don't match", 'danger')
            return redirect(url_for('auth.register'))

        # Check if email already exists
        existing_email = User.query.filter_by(email=email).first()
        if existing_email:
            flash('Email already exists. Please use a different email', 'danger')
            return redirect(url_for('auth.register'))

        # Check if mobile already exists
        existing_mobile = User.query.filter_by(mobile=mobile).first()
        if existing_mobile:
            flash('Mobile number already exists. Please use a different mobile number', 'danger')
            return redirect(url_for('auth.register'))

        # Hash the password
        hashed_password = generate_password_hash(password)

        # Create a new user instance
        new_user = User(first_name=first_name, last_name=last_name, date_of_birth=date_of_birth,
                        mobile=mobile, email=email, password=hashed_password)
        
        # Add the new user to the database
        db.session.add(new_user)
        db.session.commit()

        flash('Registration successful! Please login', 'success')
        return redirect(url_for('auth.login'))

    return render_template('auth/register.html')

@bp.route('/logout')
def logout():
    session.clear()
    flash('Logged out successfully!', 'success')
    return redirect(url_for('auth.login'))