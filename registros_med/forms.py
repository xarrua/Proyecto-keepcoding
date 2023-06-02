from flask_wtf import FlaskForm
from wtforms import DateField,StringField,FloatField,SubmitField
from wtforms.validators import DataRequired,Length,ValidationError
from datetime import date

class RegistrosForm(FlaskForm):
    usu_name = StringField('Nombre',validators=[DataRequired( message="El nombre es requerido" ),Length(min=4,message="Mas de 3 carácteres por favor")])
    usu_lastname=  StringField('Apellido',validators=[DataRequired( message="El apellido es requerido" ),Length(min=4,message="Mas de 3 carácteres por favor")])
    usu_email=  StringField('email',validators=[DataRequired( message="El email es requerido" ),Length(min=4,message="Mas de 3 carácteres por favor")])
    usu_phone=  StringField('Teléfono',validators=[DataRequired( message="El teléfono es requerido" ),Length(min=9,message="Mas de 3 carácteres por favor")])
    usu_country=  StringField('Pais',validators=[DataRequired( message="El pais es requerido" ),Length(min=4,message="Mas de 3 carácteres por favor")])
    usu_city=  StringField('Ciudad',validators=[DataRequired( message="El ciudad es requerido" ),Length(min=4,message="Mas de 3 carácteres por favor")])
    usu_birthd=  DateField('Fecha de nacimiento',validators=[DataRequired( message="La fecha de nacimiento es requerida" )])
    usu_sex= StringField('sexo',validators=[DataRequired( message="El sexo es requerido" )])
    usu_date = DateField('Fecha',validators=[DataRequired( message="La fecha es requerida" )])
    usu_user = StringField('Usuario',validators=[DataRequired( message="El usuario es requerido" ),Length(min=4,message="Mas de 3 carácteres por favor")])
    usu_pass = StringField('Contraseña',validators=[DataRequired( message="La contraseña es requerido" ),Length(min=4,message="Mas de 3 carácteres por favor")])
    
    usu_foto = StringField('foto', validators=[DataRequired( message="Imagen no valida, revise formato (jpg o png) y que no sea muy grande")])
    usu_profession = StringField('Profesión', validators=[DataRequired(message="Profesion o actividad es requerida")])
    
    
    submit = SubmitField('Aceptar')


    def validate_date(form,field):
        if field.data > date.today():
            raise ValidationError("Fecha invalida: La fecha introducida es a futuro")

    def ComprobacionPassword():
        usu_pass = StringField
        repetPass = StringField
        if usu_pass == repetPass:
            return usu_pass
        else:
            return "Las contraseñas no coinciden, vuelva a introducirlas"
        
   