from flask import Flask
from db.mongodb import init_db
from auth.auth import auth_bp
from resources.resources import resources_bp

app = Flask(__name__)

# Inicializa o banco de dados
init_db(app)

# Registra blueprints
app.register_blueprint(auth_bp, url_prefix='/auth')
app.register_blueprint(resources_bp, url_prefix='/resources')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
