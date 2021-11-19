from flask_wtf import FlaskForm
from wtforms import TextField, PasswordField, SubmitField,validators
from wtforms.fields.core import FloatField, SelectField
from wtforms.fields.html5 import DateField, EmailField,IntegerField
from wtforms.fields.simple import TextAreaField
from wtforms.validators import InputRequired, Length, EqualTo, number_range
from wtforms.widgets.core import TextArea

class Login(FlaskForm):
    usr = TextField('Usuario *',validators=[Length(min=5, max=40, message='Longitud fuera de rango'),InputRequired(message='Usuario es requerido')])
    pwd = PasswordField('Clave *',validators=[Length(min=5, max=40, message='Longitud fuera de rango'),InputRequired(message='Clave es requerido')])
    btn = SubmitField('Ingresar')

class Registro(FlaskForm):


    nom = TextField('Nombre *',validators=[Length(min=1, max=100, message='Longitud fuera de rango'),InputRequired(message='Nombre es requerido')])
    ema = EmailField('Email *',validators=[Length(min=3, max=100, message='Longitud fuera de rango'),InputRequired(message='Email es requerido')])
    #usr = TextField('Usuario *',validators=[Length(min=5, max=40, message='Longitud fuera de rango'),InputRequired(message='Usuario es requerido')])
    cla = PasswordField('Clave *')
    cofcla = PasswordField('Confirmar Clave *')
    ver = PasswordField('Verificación *',validators=[Length(min=5, max=40, message='Longitud fuera de rango'),InputRequired(message='Clave es requerido'), EqualTo(cla, message='La clave y su verificación no corresponden')])
    
    btn = SubmitField('Registrar')

    id = TextField('Identificacion *', validators=[Length(min=1, max=30, message='Longitud fuera de rango'),InputRequired(message='Identificacion es requerida')])
    tipo_id = SelectField(u'Tipo de Identificación', choices=[('cc', 'Cedula'), ('pasaporte', 'Pasaporte'),('ce', 'Cedula Extranjeria') ])
    apellidos = TextField('Apellidos *', validators=[Length(min=1, max=100, message='Longitud fuera de rango'),InputRequired(message='Apellidos son requeridos')])
    gen = SelectField(u'Genero', choices=[('M', 'Masculino'), ('F', 'Femenino'),('NR','No registra') ])
    fecha_nac = DateField('Fecha de nacimiento')
    fecha_ingreso = DateField('Fecha de ingreso', format='%m/%d/%Y')
    fin_contrato = DateField('Fin de Contrato', format='%m/%d/%Y')
    tipo_contrato = SelectField(u'Tipo de Contrato', choices=[('termino fijo', 'Termino fijo'), ('indefinido', 'Indefinido'),('prestacion de servicio', 'Prestación de Servicios'),('practicante','Practicante') ])
    cargo = TextField('Cargo *', validators=[Length(min=1, max=20, message='Longitud fuera de rango'),InputRequired(message='cargo es requerido')])
    dependencia =SelectField(u'Dependencia', choices=[('', 'Elige una opción...'), ('administracion', 'Administración'),('operaciones','Operaciones'),('gh','Gestión Humana'),('logistica','Logística'),('contratista','Contratista') ]) 
   
    salario = FloatField('Salario *')
    perfil = SelectField(u'Perfil', choices=[('Cliente', 'Cliente'), ('Admin', 'Administrador') ])
    tel = TextField('telefono *', validators=[Length(min=1, max=100, message='Longitud fuera de rango'),InputRequired(message='Telefono es requerido')])
    dir = TextField('Direccion *', validators=[Length(min=1, max=50, message='Longitud fuera de rango'),InputRequired(message='Direccion es requerida')])
    observacion = TextAreaField()

class fbforma(FlaskForm):
        #ato = TextField('Asunto *', validators = [InputRequired(message='Indique el asunto')])
        fecha = DateField('Fecha *', format='%m/%d/%Y',validators =[InputRequired()])
        cp = IntegerField('Cuidado Personal', validators =[InputRequired()])
        mt = IntegerField('Manejo del tiempo',validators =[InputRequired()])
        tw = IntegerField('Trabajo en equipo',validators =[InputRequired()])
        act = IntegerField('Actitud', validators =[InputRequired()])
        cul = IntegerField('Cultura',validators =[InputRequired()])
        emp = IntegerField('Empatia',validators =[InputRequired()] )
        obs = TextField('Observaciones *', validators=[Length(min=1, max=50, message='Longitud fuera de rango')])
        pun = TextField('Identificación Empleado *')
        
        btn = SubmitField('Registrar')