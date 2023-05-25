from registros_med import app
from flask import Flask, render_template, request, redirect, url_for, flash
from datetime import date, datetime
from registros_med.models import *
from registros_med.forms import RegistrosForm

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
    
    return errores

@app.route('/')
def index():    
    return render_template("index.html", title=home)

@app.route('/sswe')
def sswe():
    return render_template("personal/sswe.html")

@app.route('/pswe')
def pswe():
    return render_template("personal/pswe.html", name="Swelyn")

@app.route('/sjava')
def sjava():
    return render_template("personal/sjava.html", name="Josué")

@app.route('/pjava')
def pjava():
    return render_template("personal/pjava.html", name="Josué")




@app.route("/login", methods=['GET', 'POST'])
def login():
  
    return render_template("login.html", title="login")

@app.route('/profesionals')
def home():
    return render_template("profesionals.html", title="profesionals")

@app.route("/about")
def about():
    return render_template("about.html", title="about")

@app.route('/registro')
def registro():
    registros = select_all()
    return render_template("registro.html", data = registros,ingreso=select_ingreso(),egreso= select_egreso())

@app.route('/java')
def java():
    return render_template('personal/java.html', title=java)

@app.route('/swe')
def swe():
    return render_template('personal/swe.html', title=swe)

@app.route('/josu')
def josu():
    return render_template('personal/josu.html', title=josu)

@app.route('/payment')
def payment():
    return render_template('payment/form.html', title="checkout")

@app.route('/psico')
def psico():
    return render_template('psico.html', title=psico)

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
                    form.usu_quantity.data ])
            
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
        form.usu_user.data = resultado[10]
        form.usu_pass.data = resultado[11]
        form.usu_date.data = datetime.strptime(resultado[9],"%Y-%m-%d")
        form.usu_concept.data = resultado[12]
        form.usu_quantity.data = resultado[13]

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
                    form.usu_quantity.data ])
            flash("Movimiento actualizado correactamente!!!")
            return redirect("/registro")
       else:
            return render_template("create.html",dataForm=form)
      




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
