from registros_med.conexion import Conexion
from flask import request
from datetime import date, datetime


def select_all():
    conectar = Conexion("SELECT * from usuarios order by usu_date DESC")
    filas = conectar.res.fetchall() #(1,2023-05-05,sueldo,1600)
    columnas= conectar.res.description #columnas(id,0,0,0,0,0,0)
                                                          
    #objetivo crear una lista de diccionario con filas y columnas
    lista_diccionario=[]
    
    for f in filas:
        diccionario={}
        posicion=0
        for c in columnas:
            diccionario[c[0]] = f[posicion] 
            posicion +=1
        lista_diccionario.append(diccionario)

    conectar.con.close()
    
    return lista_diccionario

def insert(registroForm):
    conectarInsert = Conexion("insert into usuarios(usu_name,usu_lastname,usu_email,usu_phone,usu_country,usu_city,usu_birthd,usu_sex,usu_date,usu_user,usu_pass,usu_foto,usu_profession) values(?,?,?,?,?,?,?,?,?,?,?,?,?)",registroForm)
    conectarInsert.con.commit()#funcion para validar el registro
    conectarInsert.con.close()


def select_by(id):
    conectSelectBy = Conexion(f"select * from usuarios where usu_id={id}")
    resultado = conectSelectBy.res.fetchall()
    conectSelectBy.con.close()
    
    return resultado[0]

def delete_by(id):
    conectDeleteBy = Conexion(f"delete from usuarios where usu_id={id};")
    conectDeleteBy.con.commit()#funcion para validar el registro
    conectDeleteBy.con.close()

def update_by(id,registro):
    conectUpdateBy = Conexion(f"UPDATE usuarios SET usu_name=?,usu_lastname=?,usu_email=?,usu_phone=?,usu_country=?,usu_city=?,usu_birthd=?,usu_sex=?,usu_date=?,usu_user=?,usu_pass=?,usu_profession=? WHERE usu_id={id};",registro)
    conectUpdateBy.con.commit()
    conectUpdateBy.con.close()
"""
def select_ingreso():
    conectIngreso = Conexion("SELECT sum(usu_quantity) from usuarios WHERE usu_quantity > 0")
    resultadoIngreso = conectIngreso.res.fetchall()
    conectIngreso.con.close()

    return resultadoIngreso[0][0]

def select_egreso():
    conectEgreso = Conexion("SELECT sum(usu_quantity) from usuarios WHERE usu_quantity < 0")
    resultadoEgreso = conectEgreso.res.fetchall()
    conectEgreso.con.close()

    return resultadoEgreso[0][0]


def ComprobacionPassword2():
    pass

def fotoPerfil():
    foto=request.form['txtFoto']

    now=datetime.now()
    tiempo=now.strftime('%Y%H%M%S')
    if foto.filename!='':
        nuevoNombreFoto=tiempo+foto.filename
        foto.save('uploas/"+nuevoNombreFoto')
    conectarInsert = Conexion("INSERT INTO usuarios(usu_name,usu_foto) ")

def perfilWeb():
    conectSelectBy = Conexion(f"select * from usuarios where usu_id={id}")
    resultado = conectSelectBy.res.fetchall()
    conectSelectBy.con.close()
    
    return resultado[0]
    """