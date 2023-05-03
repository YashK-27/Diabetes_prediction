from flask import Flask

app = Flask(__name__)

# Register blueprints here
from app.main import bp as main_bp
app.register_blueprint(main_bp)

from app import views