from flask import Flask
from flask import render_template, url_for, request,jsonify

app = Flask(__name__)

# Register blueprints here
from app.main import bp as main_bp
app.register_blueprint(main_bp)

from app import views