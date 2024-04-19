from flask import Blueprint, redirect, url_for

# Create a Blueprint for base routes
bp = Blueprint('base', __name__)

# Define a route for the base URL
@bp.route('/')
def index():
    return redirect(url_for('auth.login'))