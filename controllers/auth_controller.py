from flask import Blueprint, render_template, request, session, redirect
from models.auth_model import verify_credentials

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/sign_up', methods=['GET'])
def formulaire_client():
    return render_template('signup.html')

@auth_bp.route('/sign_up', methods=['POST'])
def enregistrer_client():
    login = request.form['login']
    password = request.form['password']
    user = verify_credentials(login, password)

    if user:
        session['authentifie'] = True
        session['user_id'] = user[0]
        return redirect('/')
    return redirect('/')

@auth_bp.route('/sign_in', methods=['GET', 'POST'])
def authentification():
    if request.method == 'POST':
        login = request.form['login']
        password = request.form['password']
        user = verify_credentials(login, password)
        if user:
            session['authentifie'] = True
            session['user_id'] = user[0]
            return redirect('/')
        return render_template('signin.html', error=True)
    return render_template('signin.html', error=False)

@auth_bp.route('/sign_out', methods=['GET'])
def deconnexion_utilisateur():
    session['authentifie'] = False
    session['user_id'] = ""
    return redirect('/')
