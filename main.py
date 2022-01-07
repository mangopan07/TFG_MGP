from flask import Flask
from flask import render_template
from flask import Flask , request,redirect, url_for, flash
from flask import render_template
from flask_mysqldb import MySQL

app=Flask(__name__)

#MySQL connection
app.config['MYSQL_HOST']= '127.0.0.1'
app.config['MYSQL_USER']= 'root'
app.config['MYSQL_PASSWORD']= ''
app.config['MYSQL_DB']= 'tfgmgp'
mysql = MySQL(app)

#configuracion
app.secret_key= 'mysecretkey'

@app.route('/')
def index():
    
    return render_template('index.html')


@app.route('/gallery.html')
def gallery():
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM `unidad de obra`')#declaramos consulta #ponemos ` ` para que no haya problemas con los espacios en blanco
    data = cur.fetchall()#almacenamos en data todos los datos
    print(data)
    return render_template('gallery.html', unidades = data)



@app.route('/elementobim.html/<id>')
def elemento_bim(id):
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM `unidad de obra` WHERE id = %s', (id,))#seleccionamos el elemento con su id
    data = cur.fetchall()
    
    return render_template('elemento_bim.html', info_unidad = data[0])

if __name__== '__main__':
    app.run(debug=True, port=8000)
