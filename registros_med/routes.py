from registros_med import app
from flask import Flask, render_template, request, redirect, url_for
from datetime import date, datetime
from registros_med.models import *
from registros_med.forms import MovementsForm

def validateForm(datosFormulario):
    errores=[]#crear lista para guardar errores
    hoy = date.today().isoformat()#capturo la fecha de hoy
    if datosFormulario['date'] > hoy:
        errores.append("La fecha no puede ser mayor a la actual")
    if datosFormulario['concept'] =="":
        errores.append("El concepto no puede ir vacio")
    if  datosFormulario['quantity'] == "" or float(datosFormulario['quantity']) == 0.0:
        errores.append("El monto debe ser distinto de 0 y de vacio")
    
    return errores

@app.route('/')
def index():
    
    return render_template("index.html")


@app.route("/login")
def login():
    return render_template('login.html')

@app.route('/home')
def home():
    return render_template("home.html")

@app.route("/about")
def about():
    return render_template("about.html", title="about")

@app.route('/registro')
def info():
    registros = select_all()

    return render_template("registro.html", data = registros,ingreso=select_ingreso(),egreso= select_egreso())


@app.route("/new",methods=["GET","POST"])
def create():

    form = MovementsForm()

    if request.method == "GET":
        return render_template("create.html",dataForm=form)
    else:
       
        if form.validate_on_submit():
            insert([form.date.data.isoformat(),
                    form.concept.data,
                    form.quantity.data ])
            
            flash("Movimiento registrado correactamente!!!")
            return redirect('/')  
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
        return redirect("/")
    
@app.route("/update/<int:id>",methods=["GET","POST"])
def update(id):
    form = MovementsForm()

    if request.method == "GET":
        resultado = select_by(id)
        
        form.date.data = datetime.strptime(resultado[1],"%Y-%m-%d")
        form.concept.data = resultado[2]
        form.quantity.data = resultado[3]

        return render_template("update.html",dataForm = form, idform = id)
    else:
       
       if form.validate_on_submit():
             #aqui ingresa el post
            update_by(id,[form.date.data.isoformat(),
                            form.concept.data,
                            form.quantity.data])
            flash("Movimiento actualizado correactamente!!!")
            return redirect("/")
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
