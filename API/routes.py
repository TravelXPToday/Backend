from flask import Blueprint, jsonify, request
from flask import Flask, render_template
from controllers import (
    get_all_journeys, get_all_travelers,
    create_journey, create_traveler,
    update_journey, update_traveler,
    delete_journey, delete_traveler
)

bp = Blueprint('routes', __name__)

@bp.route('/')
def mermaid_diagram():
    return render_template('index.html')

@bp.route('/journey/all', methods=['GET'])
def journey():
    return jsonify(get_all_journeys())

@bp.route('/journey', methods=['POST'])
def add_journey():
    data = request.json
    create_journey(data)
    return jsonify({"message": "Journey added successfully!"})

@bp.route('/journey', methods=['PUT'])
def modify_journey():
    criteria = request.args.to_dict() 
    updates = request.json
    update_journey(criteria, updates)
    return jsonify({"message": "Journey updated successfully!"})

@bp.route('/journey', methods=['DELETE'])
def remove_journey():
    criteria = request.args.to_dict()  
    delete_journey(criteria)
    return jsonify({"message": "Journey deleted successfully!"})

@bp.route('/traveler/all', methods=['GET'])
def travelers():
    return jsonify(get_all_travelers())

@bp.route('/traveler', methods=['POST'])
def add_traveler():
    data = request.json
    create_traveler(data)
    return jsonify({"message": "Traveler added successfully!"})

@bp.route('/traveler', methods=['PUT'])
def modify_traveler():
    criteria = request.args.to_dict() 
    updates = request.json
    update_traveler(criteria, updates)
    return jsonify({"message": "Traveler updated successfully!"})

@bp.route('/traveler', methods=['DELETE'])
def remove_traveler():
    criteria = request.args.to_dict()  
    delete_traveler(criteria)
    return jsonify({"message": "Traveler deleted successfully!"})
