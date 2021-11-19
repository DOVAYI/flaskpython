import sqlite3
URL_DB = 'Lala.db'

def seleccion(sql) -> list:
    """ Ejecuta una consulta de selección sobre la base de datos """
    try:
        with sqlite3.connect(URL_DB) as con:
            cur = con.cursor()
            res = cur.execute(sql).fetchall()
    except sqlite3.Error as er:
        print('SQLite error: %s' % (' '.join(er.args)))
        print("Exception class is: ", er.__class__)
    return res

def accion(sql, datos) -> int:
    """ Ejecuta una consulta de acción sobre la base de datos """
    try:
        with sqlite3.connect(URL_DB) as con:
            cur = con.cursor()
            res = cur.execute(sql, datos).rowcount
            if res!=0:
                con.commit()
            else:
                res=0
    except sqlite3.Error as er:
        print('SQLite error: %s' % (' '.join(er.args)))
        print("Exception class is: ", er.__class__)
    return res
