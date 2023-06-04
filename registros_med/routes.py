from registros_med import app
from flask import Flask, render_template, request, redirect, url_for, flash, session
from datetime import date, datetime
from registros_med.models import *
from registros_med.forms import RegistrosForm
import os
from notifypy import Notify
from flask_wtf.csrf import CSRFProtect
from flask_login import LoginManager, login_user, logout_user, login_required
import sqlite3



 
def validateForm(datosFormulario):
    errores=[]#crear lista para guardar errores
    hoy = date.today().isoformat()#capturo la fecha de hoy
    if datosFormulario['usu_name'] =="":
        errores.append("El nombre no puede ir vacio")
    if datosFormulario['usu_lastname'] =="":
        errores.append("El apellido no puede ir vacio")
    if datosFormulario['usu_email'] =="":
        errores.append("El email no puede ir vacio")
    if datosFormulario['usu_phone'] =="":
        errores.append("El telefono no puede ir vacio")
    if datosFormulario['usu_country'] =="":
        errores.append("El Pais no puede ir vacio")
    if datosFormulario['usu_city'] =="":
        errores.append("La ciudad no puede ir vacio")
    if datosFormulario['usu_birthd'] > hoy:
        errores.append("La fecha no es correcta")
    if datosFormulario['usu_sex'] =="":
        errores.append("El genero no puede ir vacio")    
    if datosFormulario['usu_date'] > hoy:
        errores.append("La fecha no puede ser mayor a la actual")
    if datosFormulario['usu_concept'] =="":
        errores.append("El concepto no puede ir vacio")
    if  datosFormulario['usu_quantity'] == "" or float(datosFormulario['usu_quantity']) == 0.0:
        errores.append("El monto debe ser distinto de 0 y de vacio")
    if datosFormulario["usu_foto"] =="":
        errores.append("La imagen no es valida (jpg o png)")
    if datosFormulario["usu_profession"]:
        errores.append("Profesión o actividad no puede ir vacia")
    return errores
#Home e Index
@app.route('/')
def index():    
    return render_template("index.html")

#login
@app.route('/layoyt', methods = ['GET', 'POST'])
def layout():
    session.clear()
    return render_template("login/contenido")




@app.route('/contenido')
def contenido():
    return render_template('login/contenido.html')

@app.route('/prem')
def prem():
       return render_template("/loginpremium/home.html")


@app.route('/standar')
def standar():
    
       return render_template("login/estandar/homeTwo.html")


app.secret_key = 'mysecretkey'



# Ruta de registro
@app.route('/test_upload', methods=['POST'])
def test_upload():
    if request.method == 'POST':
        nombre = request.form['nombre']
        foto = request.files['foto']
        proyecto = app.root_path
        now=datetime.now()
        tiempo=now.strftime("%Y%m%d%H%M%S")
        rename = tiempo + "-" + foto.filename

        #si viene foto entonces guardar en carpeta del sistema
        if foto: 
            ruta_imagen = os.path.join(proyecto,"static/upload", rename)
            foto.save(ruta_imagen)


   


# Ruta de inicio de sesión
@app.route('/login', methods=['GET', 'POST'])
def login():
   

    
    if request.method == 'POST':
        # obtener los datos del formulario
        username = request.form['username']
        password = request.form['password']
       
        # verificar las credenciales en la base de datos      
        selectUsuario = Conexion('SELECT * FROM usuarios WHERE usu_user = ? AND usu_pass = ? ', (username, password))
        usuario = selectUsuario.res.fetchone()
        selectUsuario.con.close()
       
  

        if usuario is not None:              


            session['userid'] = username['userid']
            session['email'] = user 
            # credenciales válidas, redireccionar
            return redirect('/profesionals')
        else:
            # credenciales inválidas
            error = "Credenciales inválidas"
            return render_template('login.html', error=error)

    else:
        return render_template('login.html')

#base de datos

@app.route('/registro')
def registro():
    registros = select_all()
    return render_template("registro.html", data = registros)



@app.route("/new",methods=["GET","POST"])
def create():

    form = RegistrosForm()

    if request.method == "GET":
        return render_template("create.html", dataForm=form)
    else:
       
        
            if request.method == 'POST':
                name = request.form['name']
                lastname = request.form['lastname']
                email = request.form['email']
                phone = request.form['phone']
                country = request.form['country']
                city = request.form['city']
                birthday = request.form['birthday']
                sex = request.form['sex']
                date = request.form['date']
                user = request.form['user']
                password = request.form['password']
                profession = request.form['profession']   
                     
                foto = request.files['foto']
                proyecto = app.root_path
                now=datetime.now()
                tiempo=now.strftime("%Y%m%d%H%M%S")
                rename = tiempo + "-" + foto.filename
                
                #si viene foto entonces guardar en carpeta del sistema
                if foto: 
                    ruta_imagen = os.path.join(proyecto,"static/upload", rename)
                    foto.save(ruta_imagen)

            conectarInsert = Conexion("insert into usuarios(usu_name,usu_lastname,usu_email,usu_phone,usu_country,usu_city,usu_birthd,usu_sex,usu_date,usu_user,usu_pass,usu_foto,usu_profession) values(?,?,?,?,?,?,?,?,?,?,?,?,?)",(name, lastname, email, phone, country, city, birthday, sex, date, user, password, rename, profession))
            conectarInsert.con.commit()#funcion para validar el registro
            conectarInsert.con.close()

            """ insert([form.usu_name.data,
                    form.usu_lastname.data,
                    form.usu_email.data,
                    form.usu_phone.data,
                    form.usu_country.data,
                    form.usu_city.data,
                    form.usu_birthd.data.isoformat(),
                    form.usu_sex.data,
                    form.usu_date.data.isoformat(),
                    form.usu_user.data,
                    form.usu_pass.data,                 
                    
                    form.usu_foto.data,
                    form.usu_profession.data ])"""
            
            flash("Movimiento registrado correactamente!!!")
            return redirect('/login')  
      #  else:
         #   return render_template("create.html",dataForm=form)

@app.route("/delete/<int:id>",methods=["GET","POST"])
def remove(id):
    if request.method == "GET":
        resultado = select_by(id)

        return render_template("delete.html",data=resultado)
    else:
        delete_by(id)
        flash("Movimiento eliminado correctamente !!!")
        return redirect("/registro")
    
@app.route("/update/<int:id>",methods=["GET","POST"])
def update(id):
    form = RegistrosForm()

    if request.method == "GET":
        resultado = select_by(id)
        
        form.usu_name.data = resultado[1]
        form.usu_lastname.data = resultado[2]
        form.usu_email.data = resultado[3]
        form.usu_phone.data = resultado[4]
        form.usu_country.data = resultado[5]
        form.usu_city.data = resultado[6]
        form.usu_birthd.data = datetime.strptime(resultado[7],"%Y-%m-%d")
        form.usu_sex.data = resultado[8]
        form.usu_date.data = datetime.strptime(resultado[9],"%Y-%m-%d")   
        form.usu_user.data = resultado[10]
        form.usu_pass.data = resultado[11]        
        form.usu_foto.data = resultado[12]
        form.usu_profession.data = resultado[13]

        return render_template("update.html",dataForm = form, usu_id = id)
        
    elif request.method == "POST":
        
       
        #if form.validate_on_submit():
          

        #aqui ingresa el post
        update_by(id,[form.usu_name.data,
            form.usu_lastname.data,
            form.usu_email.data,
            form.usu_phone.data,
            form.usu_country.data,
            form.usu_city.data,
            form.usu_birthd.data.isoformat(),
            form.usu_sex.data,
            form.usu_date.data.isoformat(),
            form.usu_user.data,
            form.usu_pass.data,                       
            form.usu_profession.data ])
        flash("Movimiento actualizado correactamente!!!")
        return redirect("/registro")
       
    
    else:
        return render_template("create.html",dataForm=form)



#paginas profesionales

#java
@app.route('/pjava')
def pjava():
    return render_template("personal/pjava.html", name="Josué")

@app.route('/sjava')
def sjava():
    return render_template("personal/sjava.html", name="Josué")

@app.route('/java')
def java():
    return render_template('personal/java.html', title=java)

#swe
@app.route('/pswe')
def pswe():
    return render_template("personal/pswe.html", title="perfil", name="Swelyn")

@app.route('/sswe')
def sswe():
    return render_template("personal/sswe.html",title="perfil", name="Swelyn")


@app.route('/swe')
def swe():
    return render_template('personal/swe.html', title="cv", name="Swelyn")


#josu
@app.route('/pjosu')
def pjosu():
    return render_template('personal/pjosu.html')

@app.route('/sjosu')
def sjosu():
    return render_template('personal/sjosu.html')


@app.route('/josu')
def josu():
    return render_template('personal/josu.html', title=josu)



# Cobro de pacientes
@app.route('/payment')
def payment():
    return render_template('payment/form.html', title="checkout")

# otros
@app.route('/ejemplo', methods=["GET","POST"])
def ejemplo():
    
    conectUpdateBy = Conexion("SELECT  * FROM usuarios WHERE usu_id = 12" )
    conectUpdateBy.con.commit()
    conectUpdateBy.con.close()

    

    
    return render_template('ejemplo.html' )

@app.route('/profesionals')
def home():
    registros = select_all()


    return render_template("profesionals.html", data = registros, title="profesionals" )


@app.route("/about")
def about():
    return render_template("about.html", title="about")

@app.route('/pruebas',methods=["GET","POST"])
def pruebas():
    registros = select_all()
    form = RegistrosForm()

    if request.method == "GET":
        return render_template("profesionals.html",dataForm=form)
    else:
       
        if form.validate_on_submit():
            insert([form.usu_name.data,
                    form.usu_lastname.data,
                    form.usu_email.data,
                    form.usu_phone.data,
                    form.usu_country.data,
                    form.usu_city.data,
                    form.usu_birthd.data.isoformat(),
                    form.usu_sex.data,
                    form.usu_date.data.isoformat(),
                    form.usu_user.data,
                    form.usu_pass.data,                    
                    form.usu_concept.data,
                    form.usu_quantity.data,
                    form.usu_foto.data,
                    form.usu_profession.data ])
            
            
            flash("Movimiento registrado correactamente!!!")
            return redirect('/pruebas')  
        else:
            return render_template("profesionals.html",dataForm=form, data = registros, title="profesionals")

      
@app.route('/user/<int:id>',methods=["GET","POST"])
def user(id):
    resultado = select_by(id)
    #selectUsuario = Conexion('SELECT * FROM usuarios WHERE usu_id = ?', (id))
    #usuario = selectUsuario.res.fetchone()
    #selectUsuario.con.close()


    return render_template("user.html",  datos = resultado ) 

