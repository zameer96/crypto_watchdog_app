from app import db
from sqlalchemy.orm import relationship

class Price(db.Model):
    __tablename__ = 'price'

    id = db.Column(db.Integer, primary_key=True)
    crypto_id = db.Column(db.Integer, db.ForeignKey('cryptocurrency.id'), nullable=False)
    price_usd = db.Column(db.DECIMAL(20, 2))
    price_cad = db.Column(db.DECIMAL(20, 2))
    last_updated_at = db.Column(db.BIGINT)
    last_updated_at_datetime = db.Column(db.TIMESTAMP)

    cryptocurrency = relationship("Cryptocurrency", back_populates="prices")