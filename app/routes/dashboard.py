from flask import Blueprint, render_template, request, session, redirect, flash, url_for
import json
from app import db
from app.models.cryptocurrency import Cryptocurrency
from app.models.price import Price
from app.models.user import User

# Create a Blueprint for dashboard routes
bp = Blueprint('dashboard', __name__, url_prefix='/dashboard')

@bp.route('/profile')
def profile():
    user = User.query.filter_by(id=session['user_id']).first()
    if not user:
        flash("User not found. Please login again!")
        return redirect(url_for('auth.login'))
    
    return render_template('dashboard/profile.html', user=user)


# Define a route for the dashboard homepage
@bp.route('/')
def index():
    selected_currency = request.args.get('currency')
    selected_crypto = None

    if selected_currency:
        selected_crypto = Cryptocurrency.query.filter_by(short_name=selected_currency).first()

    # Set default to first crypto if not selected or Not found
    if not selected_crypto:
        selected_crypto = Cryptocurrency.query.first()

    selected_crypto_short_name = selected_crypto.short_name

    prices_and_timestamps = db.session.query(Price.price_cad, Price.last_updated_at) \
    .join(Price.cryptocurrency) \
    .filter(Cryptocurrency.short_name == selected_crypto_short_name) \
    .all()

    serialized_price_data = [{'price': float(price), 'timestamp': timestamp} for price, timestamp in prices_and_timestamps]


    return render_template('dashboard/main.html', 
                           currency_name=selected_crypto.name,
                           currency_short_name=selected_crypto.short_name,
                           prices_and_timestamps=json.dumps(serialized_price_data)
                           )
