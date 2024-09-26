from flask import Blueprint, render_template, session, redirect
from models.main_model import get_tickets

main_bp = Blueprint('main', __name__)

@main_bp.route('/')
def ReadBDD():
    if 'authentifie' in session and session['authentifie']:
        data = get_tickets()
        return render_template('home.html', data=data)
    else:
        return redirect('/sign_in')
