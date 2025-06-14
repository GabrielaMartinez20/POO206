from flask import Flask,jsonify #importaciones
from flask_mysqldb import MySQL 
import MySQLdb

app= Flask(__name__)   

app.config['MYSQL_HOST']="localhost"
app.config['MYSQL_USER']="root"
app.config['MYSQL_PASSWORD']="12345"
app.config['MYSQL_DB']="dbflask"
#app.config['MYSQL_PORT']=3306 //USAR SOLO EN CAMBIO DE PUERTO

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
    return 'Hola Mundo FLASK'

#Ruta con parametros
@app.route('/saludo/<nombre>')
def saludar(nombre):
    return 'Hola,'+nombre+'!!!'

#Ruta try-Catch
@app.errorhandler(404)
def paginaNoE(e):
    return 'Cuidado: Error de capa 8!!!',404

@app.errorhandler(405)
def metodonoP(e):
    return 'Revisa el metodo de envio de tu ruta (GET o POST)',405

#Ruta boble
@app.route('/usuario')
@app.route('/usuaria')
def dobleroute():
    return 'Soy el mismo recurso del servidor'

#Ruta POST 
@app.route('/formulario',methods=['POST'])
def formulario():
    return 'Soy un formulario'


#Asignacion de puerto
if __name__ == '__main__':
    app.run(port=3000,debug=True)