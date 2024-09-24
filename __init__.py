from flask import Flask, render_template, request, redirect, url_for, session
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
        return redirect(url_for('return_home'))
    
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



@app.route('/')
def ReadBDD():
    if 'authentifie' in session and session['authentifie']:
        conn = sqlite3.connect('database/database.db')
        cursor = conn.cursor()
        cursor.execute('SELECT titre, salle, description FROM signalement WHERE etat = "Ouvert"')
        data = cursor.fetchall()
        conn.close()

        return render_template('home.html', data=data)
    else:
        return redirect('/')

@app.route('/reserve')
def CheckCalendar():
    if 'authentifie' in session and session['authentifie']:
        conn = sqlite3.connect('database/database.db')
        cursor = conn.cursor()
        cursor.execute('SELECT titre, salle, description FROM signalement WHERE etat = "Ouvert"')



    else:
        return redirect('/')       

@app.route('/report', methods=['GET'])
def formulaire_signalement():
    if 'authentifie' in session and session['authentifie']:
        return render_template('report.html')
    else:
        return redirect('/')
    
@app.route('/booking', methods=['GET'])
def formulaire_reservation():
    if 'authentifie' in session and session['authentifie']:
        return render_template('bookings.html')
    else:
        return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)