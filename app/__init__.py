from flask import Flask

app=Flask(__name__)



# Registering The BluePrint

from app.main import bp as main_bp
app.register_blueprint(main_bp)





if __name__ == "__main___":
    app.run(debug=True)
