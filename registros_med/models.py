from registros_med.conexion import Conexion

def select_all():
    conectar = Conexion("SELECT * from usuariospeck order by usu_date DESC")
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
    conectarInsert = Conexion("insert into usuariospeck(usu_name,usu_lastname,usu_email,usu_phone,usu_country,usu_city,usu_birthd,usu_sex,usu_date,usu_user,usu_pass,usu_concept,usu_quantity) values(?,?,?,?,?,?,?,?,?,?,?,?,?)",registroForm)
    conectarInsert.con.commit()#funcion para validar el registro
    conectarInsert.con.close()


def select_by(id):
    conectSelectBy = Conexion(f"select * from usuariospeck where usu_id={id}")
    resultado = conectSelectBy.res.fetchall()
    conectSelectBy.con.close()

    return resultado[0]

def delete_by(id):
    conectDeleteBy = Conexion(f"delete from usuariospeck where usu_id={id};")
    conectDeleteBy.con.commit()#funcion para validar el registro
    conectDeleteBy.con.close()

def update_by(id,registro):
    conectUpdateBy = Conexion(f"UPDATE usuariospeck SET usu_name=?,usu_lastname=?,usu_email=?,usu_phone=?,usu_country=?,usu_city=?,usu_birthd=?,usu_sex=?,usu_user=?,usu_pass=?,usu_date=?,usu_concept=?,usu_quantity=? WHERE usu_id={id};",registro)
    conectUpdateBy.con.commit()
    conectUpdateBy.con.close()

def select_ingreso():
    conectIngreso = Conexion("SELECT sum(usu_quantity) from usuariospeck WHERE usu_quantity > 0")
    resultadoIngreso = conectIngreso.res.fetchall()
    conectIngreso.con.close()

    return resultadoIngreso[0][0]

def select_egreso():
    conectEgreso = Conexion("SELECT sum(usu_quantity) from usuariospeck WHERE usu_quantity < 0")
    resultadoEgreso = conectEgreso.res.fetchall()
    conectEgreso.con.close()

    return resultadoEgreso[0][0]

def ComprobacionPassword2():
    pass