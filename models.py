from app import db  # Import db from app.py

# Harvest Model
class Harvest(db.Model):
    __tablename__ = 'harvest'
    __table_args__ = {'extend_existing': True}  # Allow extending table definition

    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.String(100), nullable=False)
    location = db.Column(db.String(100), nullable=False)
    variety = db.Column(db.String(100), nullable=False)
    quantity = db.Column(db.Float, nullable=False)
    farmer_id = db.Column(db.Integer, nullable=False)

# Milling Model
class Milling(db.Model):
    __tablename__ = 'milling'
    __table_args__ = {'extend_existing': True}

    id = db.Column(db.Integer, primary_key=True)
    harvest_id = db.Column(db.Integer, db.ForeignKey('harvest.id'), nullable=False)
    date = db.Column(db.String(100), nullable=False)
    status = db.Column(db.String(50), nullable=False)

# Quality Model
class Quality(db.Model):
    __tablename__ = 'quality'
    __table_args__ = {'extend_existing': True}

    id = db.Column(db.Integer, primary_key=True)
    batch_id = db.Column(db.Integer, db.ForeignKey('milling.id'), nullable=False)
    acidity = db.Column(db.Float, nullable=False)
    organoleptic_score = db.Column(db.Float, nullable=False)
    inspector_id = db.Column(db.Integer, nullable=False)

# Drop existing tables and recreate them
if __name__ == '__main__':
    from app import app
    with app.app_context():  # Set the application context
        db.drop_all()  # Drop all tables (if they exist)
        db.create_all()  # Create new tables
        print("Database and tables created successfully.")
