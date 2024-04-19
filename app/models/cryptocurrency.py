from app import db

class Cryptocurrency(db.Model):
    __tablename__ = 'cryptocurrency'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    short_name = db.Column(db.String(20), nullable=False)
    image_url = db.Column(db.String(255))
    description = db.Column(db.Text)

    # Define the relationship with the Price model
    prices = db.relationship("Price", back_populates="cryptocurrency")