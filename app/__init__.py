from flask import Flask

app = Flask(__name__)

# Register blueprints here
from app.main import bp as main_bp
app.register_blueprint(main_bp)


@app.route('/test/')
def test_page():
    return '<h1>Testing the Flask Application Factory Pattern</h1>'


if __name__=="__main__":
    app.run(debug=True)