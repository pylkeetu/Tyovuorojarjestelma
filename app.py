from flask import Flask
import config

from routes.auth import auth_bp
from routes.shifts import shifts_bp

app = Flask(__name__)
app.secret_key = config.secret_key

app.register_blueprint(auth_bp)
app.register_blueprint(shifts_bp)

if __name__ == "__main__":
    app.run(debug=True)