from flask_wtf import FlaskForm
from wtforms import DateField,StringField,FloatField,SubmitField
from wtforms.validators import DataRequired,Length,ValidationError
from datetime import date

class MovementsForm(FlaskForm):
    name = StringField('nombre',validators=[DataRequired( message="El nombre es requerido" ),Length(min=4,message="Mas de 3 carácteres por favor")])
    last_name=  StringField('Apellido',validators=[DataRequired( message="El apellido es requerido" ),Length(min=4,message="Mas de 3 carácteres por favor")])
    email=  StringField('email',validators=[DataRequired( message="El email es requerido" ),Length(min=4,message="Mas de 3 carácteres por favor")])
    phone=  FloatField('Teléfono',validators=[DataRequired( message="El teléfono es requerido" ),Length(min=9,message="Mas de 3 carácteres por favor")])
    country=  StringField('Pais',validators=[DataRequired( message="El pais es requerido" ),Length(min=4,message="Mas de 3 carácteres por favor")])
    city=  StringField('Ciudad',validators=[DataRequired( message="El ciudad es requerido" ),Length(min=4,message="Mas de 3 carácteres por favor")])
    age=  DateField('Fecha de nacimiento',validators=[DataRequired( message="La fecha de nacimiento es requerida" ),Length(min=4,message="Mas de 3 carácteres por favor")])
    sex=  StringField('sexo',validators=[DataRequired( message="El apellido es requerido" ),Length(min=4,message="Mas de 3 carácteres por favor")])
    date = DateField('Fecha',validators=[DataRequired( message="La fecha es requerida" )])
    concept = StringField('Concepto',validators=[DataRequired( message="El concepto es requerido" ),Length(min=4,message="Mas de 4 carácteres por favor")])
    quantity = FloatField('Monto',validators=[DataRequired("El monto es requirido, debe ser mayor a 0")])

    submit = SubmitField('Aceptar')


    def validate_date(form,field):
        if field.data > date.today():
            raise ValidationError("Fecha invalida: La fecha introducida es a futuro")