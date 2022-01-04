from quotes import db 

# create db
db.create_all()

# add row to db
from quotes import Quote 
quote_1 = Quote(
    quote='Sometimes the things that may or may not be true are the things a man needs to believe in the most. That people are basically good; that honor, courage, and virtue mean everything; that money and power mean nothing; that good always triumphs over evil.', 
    quote_origin='Second Hand Lions - Hub')

db.session.add(quote_1)
db.session.commit()


# query db 

# query all rows
Quote.query.all()

# query first row
Quote.query.first()

# query with filter
Quote.query.filter_by(id=1).all()

# query by id
Quote.query.get(1)

# drop db tables
db.drop_all()