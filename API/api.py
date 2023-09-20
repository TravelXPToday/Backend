from flask import Flask, jsonify
from flask_cors import CORS
from routes import bp as routes_bp
import Utils.config as config
from flask import Flask, render_template
# Initialize Flask app
server = Flask(__name__)
CORS(server)
server.register_blueprint(routes_bp)

if __name__ == "__main__":
    server.run(host=config.HOST, port=config.PORT, debug=True)
