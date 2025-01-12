from faker import Faker
from app import db
from models import Harvest, Milling, Quality

faker = Faker('fr_FR')  # Use French locale for Tunisian context

# Tunisian locations (24 governorates)
locations = [
    "Tunis", "Ariana", "Ben Arous", "Manouba", "Nabeul", "Zaghouan", "Bizerte", "Beja", "Jendouba",
    "Kef", "Siliana", "Sousse", "Monastir", "Mahdia", "Kairouan", "Kasserine", "Sidi Bouzid",
    "Gabes", "Medenine", "Tataouine", "Gafsa", "Tozeur", "Kebili", "Sfax"
]

# Olive oil varieties (Tunisian and global)
olive_varieties = [
    "Chemlali", "Chetoui", "Zalmati", "Ouslati", "Sayali", "Arbequina", "Koroneiki",
    "Picual", "Frantoio", "Leccino", "Manzanilla", "Arbosana"
]

# Generate mock data for Harvest
harvest_data = [
    Harvest(
        date=faker.date_between(start_date="-1y", end_date="today"),
        location=faker.random_element(locations),
        variety=faker.random_element(olive_varieties),
        quantity=round(faker.random_number(digits=4) / 10, 1),
        farmer_id=faker.random_int(min=1, max=50)
    )
    for _ in range(50)  # Generate 50 records
]

# Generate mock data for Milling
milling_data = [
    Milling(
        harvest_id=i + 1,
        date=faker.date_between(start_date="-1y", end_date="today"),
        status=faker.random_element(["Completed", "In Progress", "Pending"])
    )
    for i in range(len(harvest_data))
]

# Generate mock data for Quality
quality_data = [
    Quality(
        batch_id=i + 1,
        acidity=round(faker.random_number(digits=1) / 10, 2),
        organoleptic_score=round(faker.random_number(digits=2) / 10, 1),
        inspector_id=faker.random_int(min=100, max=150)
    )
    for i in range(len(milling_data))
]

# Add data to the database
with db.session.begin():
    db.session.add_all(harvest_data)
    db.session.add_all(milling_data)
    db.session.add_all(quality_data)

print("Customized Tunisian mock data (50 records) added successfully!")
