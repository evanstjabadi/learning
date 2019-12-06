from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy 
from flask_marshmallow import Marshmallow 
from flask_cors import CORS



# Init app
app = Flask(__name__)
# Database
CORS(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db1.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# Init db
db = SQLAlchemy(app)
# Init ma
ma = Marshmallow(app)

# Product Class/Model
class Person(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  text = db.Column(db.String(200), unique=True)
  #email = db.Column(db.String(200))
  #price = db.Column(db.Float)
  #age = db.Column(db.Integer)

  def __init__(self, text):
    self.text = text
    #self.description = description
    #self.price = price
    #self.qty = qty

  def __repr__(self):
        return '<Person %r>' % self.text

# Product Schema
class PersonSchema(ma.Schema):
  class Meta:
    fields = ('id', 'text')

# Init schema
person_schema = PersonSchema()#strict
persons_schema = PersonSchema(many=True)

# Create a Person
@app.route('/person', methods=['POST'])
def add_person():
  text = request.json['text']
  
  #qty = request.json['qty']

  new_person = Person(text)

  db.session.add(new_person)
  db.session.commit()
  
  return person_schema.jsonify(new_person)

# Get All Products
@app.route('/person', methods=['GET'])
def get_persons():
  all_persons = Person.query.all()
  result = persons_schema.dump(all_persons)
  return jsonify(result)

# Get Single Products
@app.route('/person/<id>', methods=['GET'])
def get_person(id):
  person = Person.query.get(id)
  return person_schema.jsonify(person)

# Update a Product
@app.route('/person/<id>', methods=['PUT'])
def update_person(id):
  person = Person.query.get(id)

  text = request.json['text']
  #qty = request.json['qty']

  person.text = text
  

  #product.description = description
  #product.price = price
  #product.qty = qty

  db.session.commit()

  return person_schema.jsonify(person)

# Delete Product
@app.route('/person/<id>', methods=['DELETE'])
def delete_person(id):
  person = Person.query.get(id)
  db.session.delete(person)
  db.session.commit()

  return person_schema.jsonify(person)

# Run Server
if __name__ == '__main__':
  app.run(debug=True)
