from flask import request, jsonify
from app import app, db
from models import Harvest

# Home Route
@app.route('/', methods=['GET'])
def home():
    print("Home route called!")  # Debugging log
    return "Welcome to the Olive Chain API!", 200

# Example POST /harvest route
@app.route('/harvest', methods=['POST'])
def add_harvest():
    print("POST /harvest endpoint called!")
    data = request.get_json()
    if not all(key in data for key in ('date', 'location', 'variety', 'quantity', 'farmer_id')):
        return jsonify({'error': 'Missing required fields'}), 400
    new_harvest = Harvest(**data)
    db.session.add(new_harvest)
    db.session.commit()
    return jsonify({'message': 'Harvest record created successfully', 'harvest': data}), 201


