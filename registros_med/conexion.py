import sqlite3
from registros_med import ORIGIN_DATA

class Conexion:
    def __init__(self,querySql,params = []):
        self.con = sqlite3.connect(ORIGIN_DATA)
        self.cur = self.con.cursor()
        self.res = self.cur.execute(querySql,params)

class User():
    def __init(self, id, username, password, fullname=""):
        self.id = id
        self.name = name

     