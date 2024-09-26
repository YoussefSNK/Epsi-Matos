from flask import Blueprint, render_template, session, redirect

report_bp = Blueprint('report', __name__)

@report_bp.route('/report', methods=['GET'])
def formulaire_signalement():
    if 'authentifie' in session and session['authentifie']:
        return render_template('report.html')
    else:
        return redirect('/')
