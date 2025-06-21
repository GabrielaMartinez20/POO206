from flask import Flask,jsonify, render_template, request, url_for, flash, redirect #importaciones
from flask_mysqldb import MySQL 
import MySQLdb

app= Flask(__name__)   

app.config['MYSQL_HOST']="localhost"
app.config['MYSQL_USER']="root"
app.config['MYSQL_PASSWORD']="12345"
app.config['MYSQL_DB']="dbflask"
#app.config['MYSQL_PORT']=3306 //USAR SOLO EN CAMBIO DE PUERTO
app.secret_key='mysecretkey' #NO recomendado si es un proyecto serio

mysql=MySQL(app)

#Ruta para probar la conexion a MYSQL
@app.route('/DBCheck')
def DB_check():
    try:
        cursor=mysql.connection.cursor()
        cursor.execute('Select 1')
        return jsonify( {'status':'ok','message':'Conectado con exito'} ),200
    except MySQLdb.MySQLError as e:
        return jsonify( {'status':'error','message':str(e)} ),500
        
#Asignar ruta simple
@app.route('/')
def home():
    return render_template('formulario.html')

#Ruta de consulta
@app.route('/consulta')
def consulta():
    return render_template('consulta.html')

#Ruta para guardar
@app.route('/guardarAlbum',methods=['POST'])
def guardar():
    #declarar un diccionario/lista de errores de validaciones
    errores= {}
    
    #Obtener los datos a insertar V-> es por ser una variable
    Vtitulo= request.form.get('txtTitulo','').strip()
    Vartista= request.form.get('txtArtista','').strip()
    Vanio= request.form.get('txtAnio','').strip()
    
    if not Vtitulo:
        errores['txtTitulo']='Nombre del album Obligatorio'
    if not Vartista:
        errores['txtArtista']='Artista es Obligatorio'
    if not Vanio:
        errores['txtAnio']='Año Obligatorio'
    elif not Vanio.isdigit() or int(Vanio)<1800 or int(Vanio)>2100:
        errores['txtAnio']='Ingresa un año valido'
       
    #Si no hai errores    
    if not errores:
    #Intentamos ejecutar el insert
        try:
            cursor=mysql.connection.cursor()
            cursor.execute('insert into tbl_album(nombre,artista,anio) values(%s,%s,%s)',(Vtitulo,Vartista,Vanio))
            mysql.connection.commit()
            flash('Album se guardo correctamente en BD')
            return redirect(url_for('home'))
        
        except Exception as e:
            mysql.connection.rollback()
            flash('Algo fallo'+ str(e))
            return redirect(url_for('home'))
            
        finally: 
            cursor.close()
            
    return render_template('formulario.html',errores=errores)
    #return render_template('consulta.html')

"""#Ruta con parametros
@app.route('/saludo/<nombre>')
def saludar(nombre):
    return 'Hola,'+nombre+'!!!'"""

#Ruta try-Catch
@app.errorhandler(404)
def paginaNoE(e):
    return 'Cuidado: Error de capa 8!!!',404

@app.errorhandler(405)
def metodonoP(e):
    return 'Revisa el metodo de envio de tu ruta (GET o POST)',405

"""#Ruta boble
@app.route('/usuario')
@app.route('/usuaria')
def dobleroute():
    return 'Soy el mismo recurso del servidor'

#Ruta POST 
@app.route('/formulario',methods=['POST'])
def formulario():
    return 'Soy un formulario'"""

#Asignacion de puerto
if __name__ == '__main__':
    app.run(port=3000,debug=True)