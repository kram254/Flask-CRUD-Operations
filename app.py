from flask import Flask, render_template, request, redirect
from models import db, CustomerModel

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///customers.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

@app.before_first_request
def create_table():
    db.create_all()

@app.route('/create', methods = ['GET', 'POST'])
def create():
    if request.method == 'GET':
        return render_template('create.html')

    if request.method == 'POST':
        occupation = request.form.getlist('occupations')
        occupations = ",".join(map(str, occupation))
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        email = request.form['email']
        password = request.form['password']
        gender = request.form['gender']
        occupations = occupations
        country = request.form['country']

        customers = CustomerModel(
            first_name= first_name,
            last_name= last_name,
            email= email,
            password= password,
            gender= gender,
            occupations= occupations,
            country= country
        )

        db.session.add(customers)
        db.session.commit()
        return redirect('/')

@app.route('/', methods = ['GET'])
def RetrieveList():
    customers = CustomerModel.query.all()
    return render_template('index.html', customers = customers)

@app.route('/<int:id>/edit', methods = ['GET', 'POST'])
def update(id):
    customer = CustomerModel.query.filter_by(id=id).first()

    if request.method == 'POST':
            db.session.delete(customer)
            db.session.commit()
            if customer:
                occupation = request.form.getlist('occupations')
                occupations = ",".join(map(str, occupation))
                first_name = request.form['first_name']
                last_name = request.form['last_name']
                email = request.form['email']
                password = request.form['password']
                gender = request.form['gender']
                occupations = occupations
                country = request.form['country']


                customer = CustomerModel(
                    first_name=first_name,
                    last_name= last_name,
                    email= email,
                    password=password,
                    gender=gender,
                    occupations=occupations,
                    country=country
                )
        
                db.session.add(customer)
                db.session.commit()
                return redirect('/')
            return f"Customer with id = {id} Does nit exist"

    return render_template('update.html', customer = customer)

@app.route('/<int:id>/delete', methods = ['GET', 'POST'])
def delete(id):
    customers = CustomerModel.query.filter_by(id=id).first()
    if request.method == 'POST':
        if customers:
            db.session.delete(customers)
            db.session.commit()
            return redirect('/')
        abort(404)
    return render_template('delete.html')   

if __name__ == '__main__':
    app.run(debug=True)