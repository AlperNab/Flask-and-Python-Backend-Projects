from flask import render_template, url_for, flash, redirect, request, Blueprint
from HiringCars import db
from HiringCars.models import Customer
from HiringCars.actions.forms import ActionForm, CustomerForm, GetForm

action = Blueprint('actions', __name__)

@action.route("/")
@action.route("/actions", methods=['GET', 'POST'])
def actions():
    form = ActionForm()
    if request.method == 'GET':
        if form.validate_on_submit():
            if request.form.get('add') == 'ADD' or request.form.get('delete') == 'DELETE' or request.form.get('update') == 'UPDATE':
                return redirect(url_for('action.add'))
            elif  request.form.get('get') == 'GET':
                return redirect(url_for('action.get'))
    

    return render_template('actions.html', form=form)


@action.route("/add", methods=['GET', 'POST'])
def add():
    form = CustomerForm()
    if request.method == 'POST':
        if request.form.post('add') == 'ADD':
        #cur =db.connect.cursor()
        #cur.execute("INSERT INTO Customer(firstname ,secondname ,thirdname , carType , dateHired ,dateReturned) VALUES (form.firstname.data, form.secondname.data,form.thirdname.data,form.carType.data, form.dataHired.data, form.dataReturned.data)") 
        #cur.commit()
        #cur.close()
            customer=Customer(firstname=form.firstname.data, secondname=form.secondname.data, thirdname=form.thirdname.data, carType=form.carType.data, dataHired=form.dataHired.data,dataReturned=form.dataReturned.data)
            db.session.add(customer)
            db.session.commit()
            flash(f'Customer for {form.thirdname.data} is added!', 'success')
            return redirect(url_for('action.actions'))

        elif request.form.post('delete') == 'DELETE':
            flash (f'Customer for {form.thirdname.data} is successfully deleted!', 'success')
            return redirect(url_for('action.actions'))

        elif request.form.get('update') == 'UPDATE':
            #cur =db.connect.cursor()
            #cur.execute("INSERT INTO Customer(firstname ,secondname ,thirdname , carType , dateHired ,dateReturned) VALUES (form.firstname.data, form.secondname.data,form.thirdname.data,form.carType.data, form.dataHired.data, form.dataReturned.data)") 
            #cur.commit()
            #cur.close()
            customer=Customer(firstname=form.firstname.data, secondname=form.secondname.data, thirdname=form.thirdname.data, carType=form.carType.data, dataHired=form.dataHired.data,dataReturned=form.dataReturned.data)
            db.session.add(customer)
            db.session.commit()
            flash(f'Customer for {form.thirdname.data} is successfully updated!', 'success')
            return redirect(url_for('users.actions'))

    return render_template('add.html', form=form)
