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
        
#Asignar ruta de INICIO
@app.route('/')
def home():
    try:
        cursor=mysql.connection.cursor()
        cursor.execute("SELECT * FROM tbl_album WHERE state='1'")
        consultaTodo=cursor.fetchall() 
        return render_template('formulario.html', errores={}, albums=consultaTodo)
    
    except Exception as e:
        print('Error al consultar todo: '+e)
        return render_template('formulario.html', errores={}, albums=[])
    
    finally:
        cursor.close()

#Asignar la ruta de detalles
@app.route('/detalle/<int:id>')
def detalle(id):
    try:
        cursor=mysql.connection.cursor()
        cursor.execute('SELECT * FROM tbl_album WHERE id=%s',(id,))
        consultaId= cursor.fetchone() 
        return render_template('consulta.html', album=consultaId)
    
    except Exception as e:
        print('Error al consultar por id: '+e)
        return redirect(url_for('home'))
    
    finally:
        cursor.close()

#Ruta de consulta
@app.route('/consulta')
def consulta():
    return render_template('consulta.html')

#Ruta de VISTA DE ACTUALIZAR
@app.route('/actualizarAlbum', methods=['POST'])
def actualizar():
    errores= {}
    
    #Obtener los datos a insertar V-> es por ser una variable
    Vid= request.form.get('id','').strip()
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
            cursor.execute('UPDATE tbl_album set nombre=%s, artista=%s, anio=%s WHERE id=%s',(Vtitulo,Vartista,Vanio,Vid))
            mysql.connection.commit()
            flash('Album actulizado en la BD')
            return redirect(url_for('home'))
        
        except Exception as e:
            mysql.connection.rollback()
            flash('Algo fallo '+ str(e))
            return redirect(url_for('home'))
            
        finally: 
            cursor.close()
            
    return render_template('fromUpdate.html', album=request.form, errores=errores)

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
    
#Ruta fromUpdate
@app.route('/actualizarAlbum/<int:id>')
def actualiza(id):
        try:
            cursor=mysql.connection.cursor()
            cursor.execute('SELECT * from tbl_album WHERE id = %s', (id,))
            album = cursor.fetchone()
            if album:
                return render_template('fromUpdate.html', album=album)
            else:
                flash('Album no encontrado')
            return redirect(url_for('home'))
        
        except Exception as e:
            print('Error al obtener album:' +e)
            return redirect(url_for('home'))
            
        finally: 
            cursor.close()
            
#Ruta try-Catch
@app.errorhandler(404)
def paginaNoE(e):
    return 'Cuidado: Error de capa 8!!!',404

@app.errorhandler(405)
def metodonoP(e):
    return 'Revisa el metodo de envio de tu ruta (GET o POST)',405

#Ruta al formulario de eliminacion 
@app.route('/eliminarAlbum/<int:id>')
def eliminar(id):
        try:
            cursor=mysql.connection.cursor()
            cursor.execute('SELECT * from tbl_album WHERE id = %s', (id,))
            album = cursor.fetchone()
            return render_template('confirmDel.html', album=album)
        except Exception as e:
            print(f'Error al obtener album: {e}')
            return redirect(url_for('home'))        
        finally: 
            cursor.close()

#Ruta de confirmacion
@app.route('/confirmarDelAlbum/<int:id>', methods=['POST'])
def ConfirmarDel(id):
        try:
            cursor=mysql.connection.cursor()
            cursor.execute("UPDATE tbl_album set state='0' WHERE id = %s", (id,))
            mysql.connection.commit()
            flash('Album eliminado de la BD')
            return redirect(url_for('home'))
        except Exception as e:
            print(f'Error al obtener album: {e}')
            return redirect(url_for('home'))        
        finally: 
            cursor.close()
"""#Ruta con parametros
@app.route('/saludo/<nombre>')
def saludar(nombre):
    return 'Hola,'+nombre+'!!!'"""
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