from flask_wtf import FlaskForm
from wtforms import StringField, DateTimeField,SubmitField
from wtforms.validators import DataRequired, Length, ValidationError


class ActionForm (FlaskForm):
	add = SubmitField('Add user data')
	get = SubmitField('Get user data')
	update = SubmitField('Update user data')
	delete = SubmitField('Delete user data')

class CustomerForm(FlaskForm):
	firstname= StringField('firstname',Validators=[DataRequired(),Length(min=3, max=10)])
	secondname= StringField('secondname',Validators=[DataRequired(),Length(min=3, max=10)])
	thirdname= StringField('thirdname',Validators=[DataRequired(),Length(min=3, max=10)])
	carType= StringField('carType',Validators=[DataRequired()])
	dateHired=DateTimeField('dateHired', Validators=[(DataRequired())])
	dateReturned=DateTimeField('dateReturned', Validators=[(DataRequired())])
	add = SubmitField('Add user data')
	update = SubmitField('Update user data')
	delete = SubmitField('Delete user data')


class GetForm(FlaskForm):
	firstname= StringField('firstname',Validators=[DataRequired(),Length(min=3, max=10)])
	secondname= StringField('secondname',Validators=[DataRequired(),Length(min=3, max=10)])
	thirdname= StringField('thirdname',Validators=[DataRequired(),Length(min=3, max=10)]) 	
	get = SubmitField('Get user data')