from flask import Flask, render_template, request, redirect, url_for, session, jsonify
import sqlite3
from datetime import datetime

app = Flask(__name__)                                                                                                                  
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'  # Clé secrète pour les sessions

# Fonction pour créer une clé "authentifie" dans la session utilisateur
def est_authentifie():
    return session.get('authentifie')


@app.route('/sign_up', methods=['GET'])
def formulaire_client():
    return render_template('signup.html')

@app.route('/sign_up', methods=['POST'])
def enregistrer_client():
    login = request.form['login']
    password = request.form['password']

    conn = sqlite3.connect('database/database.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO user (login, password) VALUES (?, ?)', (login, password))
    conn.commit()
    conn.close()
    user = verify_credentials(login, password)
    if user:
        session['authentifie'] = True
        session['user_id'] = user[0] 
        return redirect('/')
    return redirect('/')

@app.route('/sign_in', methods=['GET', 'POST'])
def authentification():
    if request.method == 'POST':
        login = request.form['login']
        password = request.form['password']
        user = verify_credentials(login, password)
        if user:
            session['authentifie'] = True
            session['user_id'] = user[0] 
            return redirect('/')
        else:
            return render_template('signin.html', error=True)
    return render_template('signin.html', error=False)

@app.route('/sign_out', methods=['GET'])
def deconnexion_utilisateur():
    session['authentifie'] = False
    session['user_id'] = "" 
    return redirect('/')

  

def verify_credentials(username, password):
    conn = sqlite3.connect('database/database.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM user WHERE login = ? AND password = ?', (username, password,))
    user = cursor.fetchone()
    conn.close()
    return user

def add_suggestion(title, quantity, description):
    conn = sqlite3.connect('database/database.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO suggestions (titre, quantite, description) VALUES (?,?,?)', (title, quantity, description))
    result = cursor.fetchone()
    print(result)
    conn.close()
    return result

# Route de l'accueil, qui redirige vers la page de connexion si on est pas connecté, et qui affiche l'accueil avec les derniers tickets ouverts sinon
@app.route('/')
def ReadBDD():
    if 'authentifie' in session and session['authentifie']:
        conn = sqlite3.connect('database/database.db')
        cursor = conn.cursor()
        cursor.execute('SELECT titre, salle, description, etat FROM signalement')
        data = cursor.fetchall()
        conn.close()

        return render_template('home.html', data=data)
    else:
        return redirect('/sign_in')


# ----------------------------- RESERVATION -----------------------------

# Route de la page du calendrier, qui affiche le matériel disponible aujourd'hui
@app.route('/reservation')
def reservation():
    if 'authentifie' in session and session['authentifie']:
        conn = sqlite3.connect('database/database.db')
        cursor = conn.cursor()
        today = datetime.now().strftime('%Y-%m-%d')
        query = '''
        SELECT m.nom, m.stock - IFNULL(COUNT(r.id_materiel), 0) AS disponible
        FROM materiel m
        LEFT JOIN reservation r ON m.id = r.id_materiel
        AND r.date_emprunt = ?
        GROUP BY m.id
        '''
        cursor.execute(query, (today,))
        available_materials = cursor.fetchall()
        conn.close()

        return render_template('reservation.html', available_materials=available_materials)
    else:
        return redirect('/')

# Route du composant page calendrier, qui affiche le matériel disponible le jour selectionné
@app.route('/reserve_materials')
def reserve_materials():
    if 'authentifie' in session and session['authentifie']:
        # la date passée via AJAX 
        selected_date = request.args.get('date', datetime.now().strftime('%Y-%m-%d'))
        conn = sqlite3.connect('database/database.db')
        cursor = conn.cursor()
        query = '''
        SELECT m.nom, m.stock - IFNULL(COUNT(r.id_materiel), 0) AS disponible
        FROM materiel m
        LEFT JOIN reservation r ON m.id = r.id_materiel
        AND r.date_emprunt = ?
        GROUP BY m.id
        '''
        cursor.execute(query, (selected_date,))
        available_materials = cursor.fetchall()
        conn.close()
        return render_template('material_availability.html', available_materials=available_materials)
    else:
        return redirect('/')


@app.route('/confirm_reservation', methods=['POST'])
def confirm_reservation():
    if 'authentifie' in session and session['authentifie']:
        data = request.get_json()
        date_emprunt = data.get('date_emprunt')
        user_id = session.get('user_id')
        materials = data.get('materials')

        if not date_emprunt or not user_id or not materials:
            return jsonify({"success": False, "message": "Données manquantes."}), 400

        conn = sqlite3.connect('database/database.db')
        cursor = conn.cursor()
        
        for material in materials:
            cursor.execute('''
                INSERT INTO reservation (date_emprunt, debut_emprunt_heure, fin_emprunt_heure, id_user, id_materiel)
                VALUES (?, ?, ?, ?, (SELECT id FROM materiel WHERE nom = ?))
            ''', (date_emprunt, 9, 18, user_id, material))

        conn.commit()
        conn.close()
        
        return jsonify({"success": True, 'redirect': '/reservation'})
    else:
        return jsonify({"success": False, "message": "Utilisateur non authentifié."}), 401



# ----------------------------- SIGNALEMENT -----------------------------
# Route de la page du signalement
@app.route('/report', methods=['GET'])
def formulaire_signalement():
    if 'authentifie' in session and session['authentifie']:
        return render_template('report.html')
    else:
        return redirect('/')

# ----------------------------- SUGGESTION -----------------------------
# Route de la page de suggestion
@app.route('/suggestion', methods=['GET'])
def formulaire_suggestion():
    if 'authentifie' in session and session['authentifie']:
        return render_template('suggestions.html')
    else:
        return redirect('/')


# ----------------------------- DASHBOARD -----------------------------
@app.route('/dashboard')
def dashboard():
    if 'authentifie' in session and session['authentifie']:
        return render_template('dashboard.html')
    else:
        return redirect('/')





if __name__ == '__main__':
    app.run(debug=True)