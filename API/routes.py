from flask import Blueprint, jsonify
from controllers import get_all_journey, get_all_travelers

bp = Blueprint('routes', __name__)

@bp.route('/journey', methods=['GET'])
def journey():
    return jsonify(get_all_journey())

@bp.route('/traveler/all', methods=['GET'])
def travelers():
    return jsonify(get_all_travelers())
