from flask import Blueprint, render_template, session, redirect

suggestion_bp = Blueprint('suggestion', __name__)

@suggestion_bp.route('/suggestion', methods=['GET'])
def formulaire_suggestion():
    if 'authentifie' in session and session['authentifie']:
        return render_template('suggestions.html')
    else:
        return redirect('/')
