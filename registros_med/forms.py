from flask_wtf import FlaskForm
from wtforms import DateField,StringField,FloatField,SubmitField
from wtforms.validators import DataRequired,Length,ValidationError
from datetime import date

class MovementsForm(FlaskForm):
    date = DateField('Fecha',validators=[DataRequired( message="La fecha es requerida" )])
    concept = StringField('Concepto',validators=[DataRequired( message="El concepto es requerido" ),Length(min=4,message="Mas de 4 carácteres por favor")])
    quantity = FloatField('Monto',validators=[DataRequired("El monto es requirido, debe ser mayor a 0")])

    submit = SubmitField('Aceptar')


    def validate_date(form,field):
        if field.data > date.today():
            raise ValidationError("Fecha invalida: La fecha introducida es a futuro")