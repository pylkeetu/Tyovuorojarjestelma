from flask import Flask
from flask_wtf import CSRFProtect
import config
from datetime import datetime, timezone, timedelta

from routes.auth import auth_bp
from routes.shifts import shifts_bp

app = Flask(__name__)
app.secret_key = config.secret_key

csrf = CSRFProtect(app)

app.register_blueprint(auth_bp)
app.register_blueprint(shifts_bp)

def localtime(value):
    if value is None:
        return ""

    if isinstance(value, str):
        value = datetime.fromisoformat(value)

    finland = timezone(timedelta(hours=3))

    return value.replace(tzinfo=timezone.utc).astimezone(finland).strftime("%d.%m.%Y %H:%M")


app.jinja_env.filters["localtime"] = localtime

if __name__ == "__main__":
    app.run(debug=True)