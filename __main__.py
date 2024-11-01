from flask import Flask
import os
from flask_cors import CORS

# Wird benötigt um zwischen den einzelnen Dateien navigieren zu können
# Sollte Identisch mit Standardwerten sein, ändert aber in manchen Fällen das Ergebnis
app = Flask(
    __name__, static_url_path="", static_folder="./static", template_folder="./views"
)
# CORS wird benötigt, um eine Kommunikation zwischen den beiden Microservices zu ermöglichen
cors = CORS(app)
app.config["CORS_HEADERS"] = "Content-Type"

# import routes
import routes.test

if __name__ == "__main__":
    # Setzt 127.0.0.1 auf die Liste mit den Proxyausnahmen
    # Localhost sollte nicht über den Proxy gehen, tut es aber im Normalfall
    os.environ["NO_PROXY"] = "127.0.0.1"
    app.run(port=5000, debug=True, use_debugger=False, use_reloader=False)
