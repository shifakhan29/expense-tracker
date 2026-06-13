from bcrypt import hashpw, gensalt , checkpw
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager , create_access_token,  jwt_required, get_jwt_identity

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///expenses.db'
app.config['JWT_SECRET_KEY'] = 'shifa-secret-123'
db=SQLAlchemy(app)
jwt=JWTManager(app)

class Expense(db.Model):
    id=db.Column(db.Integer , primary_key=True)
    name=db.Column(db.String(100), nullable=False)
    amount=db.Column(db.Float, nullable=False)

class User(db.Model):           
    id=db.Column(db.Integer, primary_key=True)
    username=db.Column(db.String(100), unique=True , nullable=False)
    password=db.Column(db.String(200), nullable =False)


@app.route('/')
def home():
    return 'Expense Tracker API is running!'


@app.route('/expenses',methods=['GET'])
@jwt_required()
def get_expenses():
    all_expenses=Expense.query.all()
    result=[{"id": e.id, "name": e.name, "amount": e.amount} for e in all_expenses]
    return jsonify(result)

@app.route('/expenses', methods=['POST'])
@jwt_required()
def add_expenses():
    data= request.get_json()
    new_expense=Expense(name=data['name'],amount=data['amount'])
    db.session.add(new_expense)
    db.session.commit()
    return jsonify({"message": "Expense added!","name": data['name'], "amount": data['amount']} )

@app.route('/expenses/<int:id>', methods=['DELETE'])
def delete_expenses(id):
    expense=Expense.query.get(id)
    db.session.delete(expense)
    db.session.commit()
    return jsonify ({"message": "Expense deleted!","name": expense.name, "amount": expense.amount} )

@app.route('/expenses/<int:id>', methods=['PUT'])
def post_expense(id):
    expense=Expense.query.get(id)
    data=request.get_json()
    expense.name=data['name']
    expense.amount=data['amount']
    db.session.commit()
    return jsonify({"message":"Expense changed!", "name":expense.name,"amount": expense.amount})

@app.route('/register', methods=['POST'])
def register():
    data=request.get_json()
    hashed=hashpw(data['password'].encode(),gensalt())
    new_user=User(username=data['username'], password=hashed)
    db.session.add(new_user)
    db.session.commit()
    return jsonify({"message":"Registered!","username": data['username'] })

@app.route('/login', methods=['POST'])
def login():
    data=request.get_json()
    user=User.query.filter_by(username=data['username']).first()
    checked=checkpw(data['password'].encode(), user.password)
    if not checked:
         return jsonify({"message": "Wrong password!"}), 401
    access_token=create_access_token(identity=user.username)
    return jsonify({"message":"logged in!","token": access_token })


with app.app_context():
    db.create_all()
if __name__ == '__main__':
    app.run(debug=True)
    