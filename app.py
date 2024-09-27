from flask import Flask
from controllers.auth_controller import auth_bp
from controllers.main_controller import main_bp
from controllers.reservation_controller import reservation_bp
from controllers.suggestion_controller import suggestion_bp
from controllers.report_controller import report_bp

app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

# Enregistrement des blueprints
app.register_blueprint(auth_bp)
app.register_blueprint(main_bp)
app.register_blueprint(reservation_bp)
app.register_blueprint(suggestion_bp)
app.register_blueprint(report_bp)

if __name__ == '__main__':
    app.run(debug=True)
