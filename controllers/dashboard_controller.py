from flask import Blueprint, render_template, session, redirect
from models.main_model import get_tickets

dashboard_bp = Blueprint('dashboard', __name__)

@dashboard_bp.route('/dashboard')
def ReadBDD():
    if 'authentifie' in session and session['authentifie']:
        data = get_tickets()
        return render_template('dashboard.html', data=data)
    else:
        return redirect('/')