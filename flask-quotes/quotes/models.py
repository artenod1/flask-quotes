from datetime import datetime
from quotes import db 

class Quote(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    quote = db.Column(db.String(400), nullable=False)
    quote_origin = db.Column(db.String(50), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    def __repr__(self):
        return f"Quote('{self.quote[:20]}...', '{self.quote_origin}', '{self.date_posted}')"