from flask import request, jsonify
from app import app, db
from models import Harvest

# Debugging message to confirm routes are loaded
print("Routes loaded successfully!")

# Root Route
@app.route('/', methods=['GET'])
def home():
    return "Welcome to the Olive Chain API!", 200

# POST /harvest: Add a new harvest record
@app.route('/harvest', methods=['POST'])
def add_harvest():
    print("POST /harvest endpoint called!")  # Debugging log
    data = request.get_json()
    print("Received data:", data)  # Debugging log

    # Validate input
    if not all(key in data for key in ('date', 'location', 'variety', 'quantity', 'farmer_id')):
        print("Missing fields in the request!")  # Debugging log
        return jsonify({'error': 'Missing required fields'}), 400

    # Create a new harvest record
    new_harvest = Harvest(
        date=data['date'],
        location=data['location'],
        variety=data['variety'],
        quantity=data['quantity'],
        farmer_id=data['farmer_id']
    )

    db.session.add(new_harvest)
    db.session.commit()

    print("Harvest record created successfully!")  # Debugging log
    return jsonify({
        'message': 'Harvest record created successfully',
        'harvest': {
            'id': new_harvest.id,
            'date': new_harvest.date,
            'location': new_harvest.location,
            'variety': new_harvest.variety,
            'quantity': new_harvest.quantity,
            'farmer_id': new_harvest.farmer_id
        }
    }), 201

@app.route('/harvest', methods=['GET'])
def get_harvests():
    print("GET /harvest endpoint called!")  # Debugging log
    try:
        # Query all harvest records
        harvests = Harvest.query.all()
        
        # Serialize records into JSON format
        results = [
            {
                "id": harvest.id,
                "date": harvest.date,
                "location": harvest.location,
                "variety": harvest.variety,
                "quantity": harvest.quantity,
                "farmer_id": harvest.farmer_id
            } for harvest in harvests
        ]
        
        print(f"Retrieved {len(results)} harvest records.")  # Debugging log
        return jsonify(results), 200
    except Exception as e:
        print(f"Error retrieving harvests: {e}")  # Debugging log
        return jsonify({"error": "Failed to retrieve harvest records"}), 500


@app.route('/harvest/<int:id>', methods=['GET'])
def get_harvest_by_id(id):
    print(f"GET /harvest/{id} endpoint called!")  # Debugging log
    try:
        # Query the harvest record by ID
        harvest = Harvest.query.get(id)
        if not harvest:
            print(f"No harvest record found with ID: {id}")  # Debugging log
            return jsonify({"error": "Harvest record not found"}), 404

        # Serialize the record into JSON
        result = {
            "id": harvest.id,
            "date": harvest.date,
            "location": harvest.location,
            "variety": harvest.variety,
            "quantity": harvest.quantity,
            "farmer_id": harvest.farmer_id
        }

        print(f"Harvest record found: {result}")  # Debugging log
        return jsonify(result), 200
    except Exception as e:
        print(f"Error retrieving harvest record: {e}")  # Debugging log
        return jsonify({"error": "Failed to retrieve harvest record"}), 500


@app.route('/harvest/<int:id>', methods=['PUT'])
def update_harvest(id):
    print(f"PUT /harvest/{id} endpoint called!")  # Debugging log
    try:
        # Get the harvest record by ID
        harvest = Harvest.query.get(id)
        if not harvest:
            print(f"No harvest record found with ID: {id}")  # Debugging log
            return jsonify({"error": "Harvest record not found"}), 404

        # Get JSON data from the request
        data = request.get_json()

        # Update fields
        harvest.date = data.get('date', harvest.date)
        harvest.location = data.get('location', harvest.location)
        harvest.variety = data.get('variety', harvest.variety)
        harvest.quantity = data.get('quantity', harvest.quantity)
        harvest.farmer_id = data.get('farmer_id', harvest.farmer_id)

        # Commit changes to the database
        db.session.commit()
        print(f"Harvest record updated: {harvest.id}")  # Debugging log

        return jsonify({
            "message": "Harvest record updated successfully",
            "harvest": {
                "id": harvest.id,
                "date": harvest.date,
                "location": harvest.location,
                "variety": harvest.variety,
                "quantity": harvest.quantity,
                "farmer_id": harvest.farmer_id
            }
        }), 200
    except Exception as e:
        print(f"Error updating harvest record: {e}")  # Debugging log
        return jsonify({"error": "Failed to update harvest record"}), 500


@app.route('/harvest/<int:id>', methods=['DELETE'])
def delete_harvest(id):
    print(f"DELETE /harvest/{id} endpoint called!")  # Debugging log
    try:
        # Get the harvest record by ID
        harvest = Harvest.query.get(id)
        if not harvest:
            print(f"No harvest record found with ID: {id}")  # Debugging log
            return jsonify({"error": "Harvest record not found"}), 404

        # Delete the record
        db.session.delete(harvest)
        db.session.commit()
        print(f"Harvest record deleted: {id}")  # Debugging log

        return jsonify({"message": "Harvest record deleted successfully"}), 200
    except Exception as e:
        print(f"Error deleting harvest record: {e}")  # Debugging log
        return jsonify({"error": "Failed to delete harvest record"}), 500


@app.route('/milling', methods=['POST'])
def add_milling():
    print("POST /milling endpoint called!")  # Debugging log
    data = request.get_json()
    print("Received data:", data)  # Debugging log

    # Validate input
    if not all(key in data for key in ('harvest_id', 'date', 'status')):
        print("Missing fields in the request!")  # Debugging log
        return jsonify({'error': 'Missing required fields'}), 400

    # Create a new milling record
    new_milling = Milling(
        harvest_id=data['harvest_id'],
        date=data['date'],
        status=data['status']
    )

    db.session.add(new_milling)
    db.session.commit()

    print("Milling record created successfully!")  # Debugging log
    return jsonify({
        'message': 'Milling record created successfully',
        'milling': {
            'id': new_milling.id,
            'harvest_id': new_milling.harvest_id,
            'date': new_milling.date,
            'status': new_milling.status
        }
    }), 201


@app.route('/milling', methods=['GET'])
def get_milling_records():
    print("GET /milling endpoint called!")  # Debugging log
    try:
        # Query all milling records
        millings = Milling.query.all()
        
        # Serialize records into JSON
        results = [
            {
                "id": milling.id,
                "harvest_id": milling.harvest_id,
                "date": milling.date,
                "status": milling.status
            } for milling in millings
        ]

        print(f"Retrieved {len(results)} milling records.")  # Debugging log
        return jsonify(results), 200
    except Exception as e:
        print(f"Error retrieving milling records: {e}")  # Debugging log
        return jsonify({"error": "Failed to retrieve milling records"}), 500


@app.route('/milling/<int:id>', methods=['GET'])
def get_milling_by_id(id):
    print(f"GET /milling/{id} endpoint called!")  # Debugging log
    try:
        # Query the milling record by ID
        milling = Milling.query.get(id)
        if not milling:
            print(f"No milling record found with ID: {id}")  # Debugging log
            return jsonify({"error": "Milling record not found"}), 404

        # Serialize the record into JSON
        result = {
            "id": milling.id,
            "harvest_id": milling.harvest_id,
            "date": milling.date,
            "status": milling.status
        }

        print(f"Milling record found: {result}")  # Debugging log
        return jsonify(result), 200
    except Exception as e:
        print(f"Error retrieving milling record: {e}")  # Debugging log
        return jsonify({"error": "Failed to retrieve milling record"}), 500


@app.route('/milling/<int:id>', methods=['PUT'])
def update_milling(id):
    print(f"PUT /milling/{id} endpoint called!")  # Debugging log
    try:
        # Get the milling record by ID
        milling = Milling.query.get(id)
        if not milling:
            print(f"No milling record found with ID: {id}")  # Debugging log
            return jsonify({"error": "Milling record not found"}), 404

        # Get JSON data from the request
        data = request.get_json()

        # Update fields
        milling.harvest_id = data.get('harvest_id', milling.harvest_id)
        milling.date = data.get('date', milling.date)
        milling.status = data.get('status', milling.status)

        # Commit changes to the database
        db.session.commit()
        print(f"Milling record updated: {milling.id}")  # Debugging log

        return jsonify({
            "message": "Milling record updated successfully",
            "milling": {
                "id": milling.id,
                "harvest_id": milling.harvest_id,
                "date": milling.date,
                "status": milling.status
            }
        }), 200
    except Exception as e:
        print(f"Error updating milling record: {e}")  # Debugging log
        return jsonify({"error": "Failed to update milling record"}), 500


@app.route('/milling/<int:id>', methods=['DELETE'])
def delete_milling(id):
    print(f"DELETE /milling/{id} endpoint called!")  # Debugging log
    try:
        # Get the milling record by ID
        milling = Milling.query.get(id)
        if not milling:
            print(f"No milling record found with ID: {id}")  # Debugging log
            return jsonify({"error": "Milling record not found"}), 404

        # Delete the record
        db.session.delete(milling)
        db.session.commit()
        print(f"Milling record deleted: {id}")  # Debugging log

        return jsonify({"message": "Milling record deleted successfully"}), 200
    except Exception as e:
        print(f"Error deleting milling record: {e}")  # Debugging log
        return jsonify({"error": "Failed to delete milling record"}), 500


@app.route('/quality', methods=['POST'])
def add_quality():
    print("POST /quality endpoint called!")  # Debugging log
    data = request.get_json()
    print("Received data:", data)  # Debugging log

    # Validate input
    if not all(key in data for key in ('batch_id', 'acidity', 'organoleptic_score', 'inspector_id')):
        print("Missing fields in the request!")  # Debugging log
        return jsonify({'error': 'Missing required fields'}), 400

    # Create a new quality record
    new_quality = Quality(
        batch_id=data['batch_id'],
        acidity=data['acidity'],
        organoleptic_score=data['organoleptic_score'],
        inspector_id=data['inspector_id']
    )

    db.session.add(new_quality)
    db.session.commit()

    print("Quality record created successfully!")  # Debugging log
    return jsonify({
        'message': 'Quality record created successfully',
        'quality': {
            'id': new_quality.id,
            'batch_id': new_quality.batch_id,
            'acidity': new_quality.acidity,
            'organoleptic_score': new_quality.organoleptic_score,
            'inspector_id': new_quality.inspector_id
        }
    }), 201


@app.route('/quality', methods=['GET'])
def get_quality_records():
    print("GET /quality endpoint called!")  # Debugging log
    try:
        # Query all quality records
        qualities = Quality.query.all()

        # Serialize records into JSON
        results = [
            {
                "id": quality.id,
                "batch_id": quality.batch_id,
                "acidity": quality.acidity,
                "organoleptic_score": quality.organoleptic_score,
                "inspector_id": quality.inspector_id
            } for quality in qualities
        ]

        print(f"Retrieved {len(results)} quality records.")  # Debugging log
        return jsonify(results), 200
    except Exception as e:
        print(f"Error retrieving quality records: {e}")  # Debugging log
        return jsonify({"error": "Failed to retrieve quality records"}), 500


@app.route('/quality/<int:id>', methods=['GET'])
def get_quality_by_id(id):
    print(f"GET /quality/{id} endpoint called!")  # Debugging log
    try:
        # Query the quality record by ID
        quality = Quality.query.get(id)
        if not quality:
            print(f"No quality record found with ID: {id}")  # Debugging log
            return jsonify({"error": "Quality record not found"}), 404

        # Serialize the record into JSON
        result = {
            "id": quality.id,
            "batch_id": quality.batch_id,
            "acidity": quality.acidity,
            "organoleptic_score": quality.organoleptic_score,
            "inspector_id": quality.inspector_id
        }

        print(f"Quality record found: {result}")  # Debugging log
        return jsonify(result), 200
    except Exception as e:
        print(f"Error retrieving quality record: {e}")  # Debugging log
        return jsonify({"error": "Failed to retrieve quality record"}), 500


@app.route('/quality/<int:id>', methods=['PUT'])
def update_quality(id):
    print(f"PUT /quality/{id} endpoint called!")  # Debugging log
    try:
        # Get the quality record by ID
        quality = Quality.query.get(id)
        if not quality:
            print(f"No quality record found with ID: {id}")  # Debugging log
            return jsonify({"error": "Quality record not found"}), 404

        # Get JSON data from the request
        data = request.get_json()

        # Update fields
        quality.batch_id = data.get('batch_id', quality.batch_id)
        quality.acidity = data.get('acidity', quality.acidity)
        quality.organoleptic_score = data.get('organoleptic_score', quality.organoleptic_score)
        quality.inspector_id = data.get('inspector_id', quality.inspector_id)

        # Commit changes to the database
        db.session.commit()
        print(f"Quality record updated: {quality.id}")  # Debugging log

        return jsonify({
            "message": "Quality record updated successfully",
            "quality": {
                "id": quality.id,
                "batch_id": quality.batch_id,
                "acidity": quality.acidity,
                "organoleptic_score": quality.organoleptic_score,
                "inspector_id": quality.inspector_id
            }
        }), 200
    except Exception as e:
        print(f"Error updating quality record: {e}")  # Debugging log
        return jsonify({"error": "Failed to update quality record"}), 500


@app.route('/quality/<int:id>', methods=['DELETE'])
def delete_quality(id):
    print(f"DELETE /quality/{id} endpoint called!")  # Debugging log
    try:
        # Get the quality record by ID
        quality = Quality.query.get(id)
        if not quality:
            print(f"No quality record found with ID: {id}")  # Debugging log
            return jsonify({"error": "Quality record not found"}), 404

        # Delete the record
        db.session.delete(quality)
        db.session.commit()
        print(f"Quality record deleted: {id}")  # Debugging log

        return jsonify({"message": "Quality record deleted successfully"}), 200
    except Exception as e:
        print(f"Error deleting quality record: {e}")  # Debugging log
        return jsonify({"error": "Failed to delete quality record"}), 500
