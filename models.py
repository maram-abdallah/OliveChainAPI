from app import db  # Import the SQLAlchemy instance

# Harvest Model
class Harvest(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.String(100), nullable=False)
    location = db.Column(db.String(100), nullable=False)
    variety = db.Column(db.String(100), nullable=False)
    quantity = db.Column(db.Float, nullable=False)
    farmer_id = db.Column(db.Integer, nullable=False)

# Milling Model
class Milling(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    harvest_id = db.Column(db.Integer, db.ForeignKey('harvest.id'), nullable=False)
    date = db.Column(db.String(100), nullable=False)
    status = db.Column(db.String(50), nullable=False)

# Quality Model
class Quality(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    batch_id = db.Column(db.Integer, db.ForeignKey('milling.id'), nullable=False)
    acidity = db.Column(db.Float, nullable=False)
    organoleptic_score = db.Column(db.Float, nullable=False)
    inspector_id = db.Column(db.Integer, nullable=False)

# Create the tables
if __name__ == '__main__':
    from app import app
    with app.app_context():
        db.create_all()
        print("Database and tables created successfully.")

