from registros_med import app
from flask import Flask, render_template, request, redirect, url_for, flash
from datetime import date, datetime
from registros_med.models import *
from registros_med.forms import RegistrosForm
import os


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
    return render_template("index.html", title=home)

#login



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
            ruta_imagen = os.path.join(proyecto,"upload", rename)
            foto.save(ruta_imagen)


    return tiempo

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        # Obtener los datos del formulario
        nombre = request.form['nombre']
        apellido = request.form['apellido']
        email = request.form['email']
        telefono = request.form['telefono']
        password = request.form['password']
        confirm_password = request.form['confirm_password']
        
        # Verificar que los campos no estén vacíos
        if nombre and apellido and email and telefono and password and confirm_password:
            # Verificar la longitud mínima de la contraseña
            if len(password) >= 6:
                # Verificar si las contraseñas coinciden
                if password == confirm_password:
                    # Aquí puedes realizar el proceso de registro del usuario
                    # por ejemplo, guardar los datos en una base de datos
                    
                    # Redireccionar a la página de inicio de sesión
                    return redirect('/login')
                else:
                    error = 'Las contraseñas no coinciden'
            else:
                error = 'La contraseña debe tener al menos 6 caracteres'
        else:
            error = 'Por favor, completa todos los campos'
            
        return render_template('register.html', error=error)
    else:
        return render_template('register.html')

# Ruta de inicio de sesión
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Obtener los datos del formulario
        
        print(request.form['username'])
        print(request.form['password'])
        return render_template("login.html")
    
        
        # Aquí puedes realizar el proceso de inicio de sesión
        # por ejemplo, verificar las credenciales en una base de datos
        
        # Redireccionar a la página de bienvenida
        #return redirect('/welcome')
    else:
        return render_template('login.html')

# Ruta de bienvenida
@app.route('/welcome')
def welcome():
    return render_template('registro.html')

#base de datos

@app.route('/registro')
def registro():
    registros = select_all()
    return render_template("registro.html", data = registros,ingreso=select_ingreso(),egreso= select_egreso())




@app.route("/new",methods=["GET","POST"])
def create():

    form = RegistrosForm()

    if request.method == "GET":
        return render_template("create.html",dataForm=form)
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
            return redirect('/registro')  
        else:
            return render_template("create.html",dataForm=form)

@app.route("/delete/<int:id>",methods=["GET","POST"])
def remove(id):
    if request.method == "GET":
        resultado = select_by(id)

        return render_template("delete.html",data=resultado)
    else:
        delete_by(id)
        flash("Movimiento eliminado correctamente !!!")
        return redirect("/registro","/psico")
    
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
        form.usu_user.data = resultado[10]
        form.usu_pass.data = resultado[11]
        form.usu_date.data = datetime.strptime(resultado[9],"%Y-%m-%d")
        form.usu_concept.data = resultado[12]
        form.usu_quantity.data = resultado[13]
        form.usu_foto.data = resultado[14]
        form.usu_profession.data = resultado[15]

        return render_template("update.html",dataForm = form, idform = id)
    else:
       
       if form.validate_on_submit():
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
                    form.usu_concept.data,
                    form.usu_quantity.data,
                    form.usu_foto.data,
                    form.usu_profession.data ])
            flash("Movimiento actualizado correactamente!!!")
            return redirect("/registro", "/psico")
       else:
            return render_template("create.html",dataForm=form)


# Cuentas de profesionales 
@app.route('/prof')
def prof():
    return render_template('profesionals/prof.html')

@app.route('/create_prof')
def create_prof():
    return render_template('/profesionals/create_prof.html')

@app.route('/delete_prof')
def delete_prof():
    return render_template('profesionals/delete_prof.html')

@app.route('/update_prof')
def update_prof():
    return render_template('profesionals/update_prof.html')


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


@app.route('/profesionals')
def home():
    registros = select_all()

    return render_template("profesionals.html", data = registros, title="profesionals")

@app.route('/psico')
def psico():
    return render_template('psico.html', title=psico)

@app.route("/about")
def about():
    return render_template("about.html", title="about")

@app.route('/pruebas',methods=["GET","POST"])
def pruebas():
    registros = select_all()
    form = RegistrosForm()

    if request.method == "GET":
        return render_template("pruebas.html",dataForm=form)
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
            return render_template("pruebas.html",dataForm=form, data = registros, title="profesionals")

      




#@app.route('/')
#def index():
   # return redirect(url_for('login'))

#@app.route("/login", methods=['GET', 'POST'])
#def login():
   # if request.method =='POST':
   #     print(request.form['username'])
   #     print(request.form['password'])
  #  else:
   #     return render_template("login")
    




#@app.route("/delete")
#def delete():
  #  return render_template("delete.html")

#@app.route("/update")
#def update():
   # return render_template("update.html")
