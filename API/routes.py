from flask import Blueprint, jsonify
from controllers import get_journey


bp = Blueprint('routes', __name__)

@bp.route('/journey', methods=['GET'])
def journey():
    return jsonify(get_journey())
