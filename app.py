from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://olive_user:yourpassword@localhost/olive_chain_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Import routes AFTER initializing `app` and `db`
import routes

if __name__ == '__main__':
    print("Starting Flask app...")
    print("Listing all registered routes:")
    for rule in app.url_map.iter_rules():
        print(f"Endpoint: {rule.endpoint}, Route: {rule}")
    app.run(debug=True, port=8000)




    

