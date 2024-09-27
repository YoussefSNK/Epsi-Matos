from flask import Blueprint, render_template, session, redirect, request
from models.suggestion_model import add_suggestion, get_all_suggestions

suggestion_bp = Blueprint('suggestion', __name__)

@suggestion_bp.route('/suggestion', methods=['GET'])
def formulaire_suggestion():
    if 'authentifie' in session and session['authentifie']:
        return render_template('suggestions.html')
    else:
        return redirect('/')
    
@suggestion_bp.route('/suggestion', methods=['POST'])
def upload_suggestion():
    if 'authentifie' in session and session['authentifie']:
        nom_materiel = request.form['nom_materiel']
        nombre_materiel = request.form['nombre_materiel']
        description_materiel = request.form['description_materiel']
        
        add_suggestion(nom_materiel, nombre_materiel, description_materiel)
        return redirect('/suggestion')
    else:
        return redirect('/sign_in')
    
def read_bdd_sugg():
    if 'authentifie' in session and session['authentifie']:
        data = get_all_suggestions()
        return render_template('suggestions.html', data=data)
    else:
        return redirect('/sign_in')
