from flask import Blueprint, render_template, request, session, jsonify, redirect
from datetime import datetime
from models.reservation_model import get_available_materials, confirm_reservation_db

reservation_bp = Blueprint('reservation', __name__)

@reservation_bp.route('/reservation')
def reservation():
    if 'authentifie' in session and session['authentifie']:
        today = datetime.now().strftime('%Y-%m-%d')
        available_materials = get_available_materials(today)
        return render_template('reservation.html', available_materials=available_materials)
    else:
        return redirect('/')

@reservation_bp.route('/reserve_materials')
def reserve_materials():
    if 'authentifie' in session and session['authentifie']:
        selected_date = request.args.get('date', datetime.now().strftime('%Y-%m-%d'))
        available_materials = get_available_materials(selected_date)
        return render_template('material_availability.html', available_materials=available_materials)
    else:
        return redirect('/')

@reservation_bp.route('/confirm_reservation', methods=['POST'])
def confirm_reservation():
    if 'authentifie' in session and session['authentifie']:
        data = request.get_json()
        result = confirm_reservation_db(data, session.get('user_id'))
        return jsonify(result)
    else:
        return jsonify({"success": False, "message": "Utilisateur non authentifié."}), 401
