from flask import Flask, render_template, request, session, url_for, redirect
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
import sqlite3
import sqlite3 as sql
from werkzeug.security import generate_password_hash, check_password_hash

from markupsafe import Markup

app = Flask(__name__, template_folder='Templates', static_folder='static')
app.secret_key = '%\x93\xd2UJ\xc4\xa5\xbe\x9e\xec\xd2\x98L\x11\x05\x1c\xe0\x90H\x03m\xf1\xb8m'
msg = MIMEMultipart()


@app.route("/")
def index():
    if 'user' in session:
        mensaje = Markup(
            '<span class="navbar-text"><a id="loginButton" onclick="cerrarSesion()">Bienvenido, ' + session[
                'user'] + ' <span class="fas fa-sign-out-alt"></span> Cerrar Sesión</a></span>')
        return render_template('index.html', sessioninfo=mensaje)
    else:
        mensaje = Markup('<span class="navbar-text"><a id="loginButton" onclick="iniciarSesion()"><span class="fas '
                         'fa-sign-in-alt"></span> Iniciar sesión</a></span>')
        return render_template('index.html', sessioninfo=mensaje)


@app.route("/actualizar", methods=['POST'])
def actualizar():
    isvisible = ''
    etiqueta_prog = request.form.get('et-prog')
    etiqueta_webd = request.form.get('et-webd')
    etiqueta_python = request.form.get('et-python')
    titulo = request.form['tituloupdate']
    contenido = request.form['contenidoupdate']
    selectvisible = request.form.get('select')
    if selectvisible == 'value1':
        isvisible = 'S'
    else:
        isvisible = 'N'
    return render_template("pruebaregistro.html", rt_response="actualizar blog", rt_titulo=titulo,
                           rt_contenido=contenido,
                           rt_visible=isvisible, rt_etprog=etiqueta_prog, rt_etwebd=etiqueta_webd,
                           rt_etpython=etiqueta_python)


@app.route("/actualizarblog")
def actualizarblog():
    if 'user' in session:
        mensaje = Markup(
            '<span class="navbar-text"><a id="loginButton" onclick="cerrarSesion()">Bienvenido, ' + session[
                'user'] + ' <span class="fas fa-sign-out-alt"></span> Cerrar Sesión</a></span>')
        return render_template('actualizarblog.html', sessioninfo=mensaje)
    else:
        mensaje = Markup(
            '<div class="alert alert-warning" role="alert">Debes iniciar sesión primero</div>')
        return render_template('login.html', mensaje=mensaje)


@app.route("/buscar")
def buscar():
    if 'user' in session:
        mensaje = Markup(
            '<span class="navbar-text"><a id="loginButton" onclick="cerrarSesion()">Bienvenido, ' + session[
                'user'] + ' <span class="fas fa-sign-out-alt"></span> Cerrar Sesión</a></span>')
        return render_template('buscar.html', sessioninfo=mensaje)
    else:
        mensaje = Markup(
            '<div class="alert alert-warning" role="alert">Debes iniciar sesión primero</div>')
        return render_template('login.html', mensaje=mensaje)


@app.route("/comentarblog")
def comentarblog():
    if 'user' in session:
        mensaje = Markup(
            '<span class="navbar-text"><a id="loginButton" onclick="cerrarSesion()">Bienvenido, ' + session[
                'user'] + ' <span class="fas fa-sign-out-alt"></span> Cerrar Sesión</a></span>')
        return render_template('comentarblog.html', sessioninfo=mensaje)
    else:
        mensaje = Markup(
            '<div class="alert alert-warning" role="alert">Debes iniciar sesión primero</div>')
        return render_template('login.html', mensaje=mensaje)


@app.route("/contenidoblog")
def contenidoblog():
    if 'user' in session:
        mensaje = Markup(
            '<span class="navbar-text"><a id="loginButton" onclick="cerrarSesion()">Bienvenido, ' + session[
                'user'] + ' <span class="fas fa-sign-out-alt"></span> Cerrar Sesión</a></span>')
        return render_template('contenidoblog.html', sessioninfo=mensaje)
    else:
        mensaje = Markup(
            '<div class="alert alert-warning" role="alert">Debes iniciar sesión primero</div>')
        return render_template('login.html', mensaje=mensaje)


@app.route("/eliminarblog")
def eliminarblog():
    if 'user' in session:
        mensaje = Markup(
            '<span class="navbar-text"><a id="loginButton" onclick="cerrarSesion()">Bienvenido, ' + session[
                'user'] + ' <span class="fas fa-sign-out-alt"></span> Cerrar Sesión</a></span>')
        return render_template('eliminarblog.html', sessioninfo=mensaje)
    else:
        mensaje = Markup(
            '<div class="alert alert-warning" role="alert">Debes iniciar sesión primero</div>')
        return render_template('login.html', mensaje=mensaje)


@app.route("/crearblog")
def crearblog():
    if 'user' in session:
        mensaje = Markup(
            '<span class="navbar-text"><a id="loginButton" onclick="cerrarSesion()">Bienvenido, ' + session[
                'user'] + ' <span class="fas fa-sign-out-alt"></span> Cerrar Sesión</a></span>')
        return render_template('newblog.html', sessioninfo=mensaje)
    else:
        mensaje = Markup(
            '<div class="alert alert-warning" role="alert">Debes iniciar sesión primero</div>')
        return render_template('login.html', mensaje=mensaje)


@app.route("/recuperar")
def recuperar():
    return render_template('recuperar.html')


@app.route("/recuperarcontrasena")
def recuperarcontrasena():
    return render_template('recuperarcontrasena.html')


@app.route("/contactus")
def contactus():
    return render_template('contactus.html')


@app.route("/verblog")
def verblog():
    return render_template('verblog.html')


@app.route("/signup")
def signup():
    return render_template('signup.html')


@app.route("/aboutus")
def about():
    return render_template('aboutus.html')


@app.route("/login")
def login():
    return render_template('login.html')


@app.route("/logout")
def logout():
    if 'user' in session:
        session.clear()
        session.pop('user', None)
        return redirect(url_for('login'))
    else:
        return render_template('login.html', mensaje='Debes iniciar primero sesíon')


@app.route("/menuprincipal")
def menuprincipal():
    if 'user' in session:
        mensaje = Markup(
            '<span class="navbar-text"><a id="loginButton" onclick="cerrarSesion()">Bienvenido, ' + session[
                'user'] + ' <span class="fas fa-sign-out-alt"></span> Cerrar Sesión</a></span>')
        return render_template('menuprincipal.html', sessioninfo=mensaje)
    else:
        return render_template('login.html', mensaje='Debes iniciar primero sesíon')


@app.route("/verificarcuenta/<username>", methods=["GET"])
def verificarcuenta(username):
    conexion = sqlite3.connect("SGB_DB.db")
    conexion.execute("update Usuarios set activo = 'Y', fechaActivacion = datetime('now','localtime') where "
                     "usuarioLogin = '" + username + "'")
    conexion.commit()
    conexion.close()
    return render_template('verificarcuenta.html')


@app.route("/newblog", methods=["POST"])
def newblog():
    if 'user' in session:
        usuario = session['user']
        isvisible = ''
        etiqueta_prog = request.form.get('et-prog')
        print(etiqueta_prog)
        etiqueta_webd = request.form.get('et-webd')
        etiqueta_python = request.form.get('et-python')
        titulo = request.form['titulo']
        contenido = request.form['contenidonew']
        selectvisible = request.form.get('select')
        if selectvisible == 'value1':
            isvisible = 'S'
        else:
            isvisible = 'N'

    # Crear conexión a base de datos
    conexion = sqlite3.connect("SGB_DB.db")

    # Crear la sentencia SQL para insertar los datos
    conexion.execute("INSERT INTO Posts (titulo, contenidoPost, fechaPublicacion, esVisible, usuarioLogin"
                     ") VALUES (?, ?,DATETIME('now', 'localtime'), ?, ?)",
                     (titulo, contenido, isvisible, usuario))
    # Ejecuto la sentencia SQL
    conexion.commit()

    objcursor = conexion.cursor()
    objcursor.execute("select max (idPost) from Posts")
    # Recuperar los registros que coincidan con los criterios de búsqueda
    rows = objcursor.fetchall()
    # Contar los registros recuperados

    for i in rows:
        if etiqueta_prog == "programacion":
            conexion.execute(
                "INSERT INTO EtiquetasPost (idEtiqueta, idPost) VALUES (?, ?)", (1, i[0]))
            conexion.commit()
        if etiqueta_webd == "diseno_web":
            conexion.execute(
                "INSERT INTO EtiquetasPost (idEtiqueta, idPost) VALUES (?, ?)", (2, i[0]))
            conexion.commit()
        if etiqueta_python == "python":
            conexion.execute(
                "INSERT INTO EtiquetasPost (idEtiqueta, idPost) VALUES (?, ?)", (3, i[0]))
            conexion.commit()

    # Cierro la conexión
    conexion.close()
    return render_template("pruebaregistro.html", rt_response="nuevo blog", rt_titulo=titulo, rt_contenido=contenido,
                           rt_visible=isvisible, rt_etprog=etiqueta_prog, rt_etwebd=etiqueta_webd,
                           rt_etpython=etiqueta_python)


@app.route("/registro", methods=["POST"])
def registro():
    # Solicitud de datos del formulario
    nom = request.form['nombre']
    usr = request.form['usuario']
    mail = request.form['correo']
    tipousuario = request.form.get('tipousuario')
    pwd = request.form['contrasena']
    valor_hash = generate_password_hash(pwd)

    usr_existe = comprobarduplicidadusuario(usr)
    mail_existe = comprobarduplicidadmail(mail)

    if usr_existe == 'Existe':
        mensaje = Markup(
            '<div class="alert alert-warning" role="alert">El usuario digitado no está disponible</div>')
        return render_template('signup.html', mensaje=mensaje)
    elif mail_existe == 'Existe':
        mensaje = Markup(
            '<div class="alert alert-warning" role="alert">Ya existe una cuenta asociada al correo</div>')
        return render_template('signup.html', mensaje=mensaje)
    else:
        # Crear conexión a base de datos
        conexion = sqlite3.connect("SGB_DB.db")

        # Crear la sentencia SQL para insertar los datos
        conexion.execute(
            "INSERT INTO Usuarios (usuarioLogin, nombreUsuario, email, contrasena, activo, fechaActivacion, "
            "pwrd_hash, idRol) VALUES (?, ?, ?, ?, ?, NULL, ?, ?)",
            (usr, nom, mail, pwd, 0, valor_hash, tipousuario))
        # Ejecuto la sentencia SQL
        conexion.commit()

        # Cierro la conexión
        conexion.close()

        cuerpo_mensaje = "Por favor, acceda al siguiente enlace para poder activar su cuenta \n " \
                         "http://127.0.0.1:5000/verificarcuenta/" + usr
        # Datos para conectarse al correo electrónico de la aplicación
        pswrd = "DevTeam2020$."
        msg['From'] = "blogappprueba@gmail.com"
        msg['To'] = mail
        msg['Subject'] = "Verificación de la cuenta"
        # Se arma el cuerpo del mensaje. Siempre se elige plain
        msg.attach(MIMEText(cuerpo_mensaje, 'plain'))
        # Establecer conexión con el servidor de correos
        mail_srv = smtplib.SMTP('smtp.gmail.com: 587')
        mail_srv.starttls()
        # Autenticación del correo de la aplicación
        mail_srv.login(msg['From'], pswrd)
        # Envío del mensaje mediante el servidor de correo
        mail_srv.sendmail(msg['From'], msg['To'], msg.as_string())
        # Cierro la conexión del servidor de correo
        mail_srv.quit()

        return render_template("pruebaregistro.html", rt_response="verificacion enviada", rt_mail=mail, rt_nombre=nom,
                               rt_usuario=usr, rt_password=pwd, rt_tipousuario=tipousuario)


def comprobarduplicidadusuario(usuario):
    registros = 0
    # Conectar con la base de datos
    conexion = sqlite3.connect("SGB_DB.db")
    conexion.row_factory = sql.Row

    # Crear un cursor de la conexión
    objcursor = conexion.cursor()
    objcursor.execute(
        "select * from Usuarios where usuarioLogin = '" + usuario + "'")

    # Recuperar los registros que coincidan con los criterios de búsqueda
    rows = objcursor.fetchall()

    # Contar los registros recuperados
    for i in rows:
        registros = registros + 1
    if registros > 0:
        return "Existe"
    else:
        return "No existe"


def comprobarduplicidadmail(mail):
    registros = 0
    # Conectar con la base de datos
    conexion = sqlite3.connect("SGB_DB.db")
    conexion.row_factory = sql.Row

    # Crear un cursor de la conexión
    objcursor = conexion.cursor()
    objcursor.execute("select * from Usuarios where email =  '" + mail + "'")

    # Recuperar los registros que coincidan con los criterios de búsqueda
    rows = objcursor.fetchall()

    # Contar los registros recuperados
    for i in rows:
        registros = registros + 1
    if registros > 0:
        return "Existe"
    else:
        return "No existe"


def comprobarhash(usuario, password):
    registros = 0
    # Conectar con la base de datos
    conexion = sqlite3.connect("SGB_DB.db")
    conexion.row_factory = sql.Row

    # Crear un cursor de la conexión
    objcursor = conexion.cursor()
    objcursor.execute(
        "select pwrd_hash from Usuarios where usuarioLogin = ? and contrasena = ? ", (usuario, password))

    # Recuperar los registros que coincidan con los criterios de búsqueda
    rows = objcursor.fetchone()

    # Comparar los hash
    if password and check_password_hash(rows["pwrd_hash"], password):
        return "Exitoso"
    else:
        return "Error"


@app.route("/passrecover", methods=["POST"])
def passrecover():
    # Solicitud de datos del formulario
    usr = request.form['usuario']
    mail = request.form['correo']

    conexion = sqlite3.connect("SGB_DB.db")
    conexion.row_factory = sql.Row

    objcursor = conexion.cursor()
    objcursor.execute(
        "select * from Usuarios where usuarioLogin = ? and email = ?", (usr, mail))
    rows = objcursor.fetchone()
    if rows is not None:
        pswd = rows['contrasena']
        cuerpo_mensaje = "A continuación encontrará la información de su cuenta: \n" \
                         "Usuario de acceso: " + usr + "\n" + "Contraseña:" + pswd
        # Datos para conectarse al correo electrónico de la aplicación
        pswrd = "DevTeam2020$."
        msg['From'] = "blogappprueba@gmail.com"
        msg['To'] = mail
        msg['Subject'] = "Has solicitado recuperar tu contraseña!!"
        # Se arma el cuerpo del mensaje. Siempre se elige plain
        msg.attach(MIMEText(cuerpo_mensaje, 'plain'))
        # Establecer conexión con el servidor de correos
        mail_srv = smtplib.SMTP('smtp.gmail.com: 587')
        mail_srv.starttls()
        # Autenticación del correo de la aplicación
        mail_srv.login(msg['From'], pswrd)
        # Envío del mensaje mediante el servidor de correo
        mail_srv.sendmail(msg['From'], msg['To'], msg.as_string())
        # Cierro la conexión del servidor de correo
        mail_srv.quit()

    return render_template("recuperar.html", rt_mail=mail)


@app.route("/iniciarsesion", methods=["POST"])
def iniciarsesion():
    registros = 0
    mensaje = None
    if request.method == 'POST':
        usr_login = request.form['usuario']
        pwd_login = request.form['contrasena']
        # Conectar con la base de datos
        conexion = sqlite3.connect("SGB_DB.db")
        conexion.row_factory = sql.Row

        # Crear un cursor de la conexión
        objcursor = conexion.cursor()
        objcursor.execute(
            "select * from Usuarios where usuarioLogin = ? and contrasena = ?", (usr_login, pwd_login))

        # Recuperar los registros que coincidan con los criterios de búsqueda
        rows = objcursor.fetchall()

        # Contar los registros recuperados
        for i in rows:
            registros = registros + 1
        if registros > 0:
            res_hash = comprobarhash(usr_login, pwd_login)
            if res_hash == "Error":
                mensaje = Markup(
                    '<div class="alert alert-warning" role="alert">Problemas de autenticación</div>')
                return render_template('login.html', mensaje=mensaje)
            else:
                if rows[0][4] == 'Y':
                    print(registros)
                    session['login'] = True
                    session['user'] = usr_login
                    return redirect(url_for('menuprincipal'))
                else:
                    mensaje = Markup(
                        '<div class="alert alert-warning" role="alert">La cuenta aún no ha sido verificada</div>')
                    return render_template('login.html', mensaje=mensaje)
        else:
            mensaje = Markup(
                '<div class="alert alert-warning" role="alert">Usuario y/o contraseña incorrectos</div>')
            return render_template('login.html', mensaje=mensaje)


if __name__ == '__main__':
    app.run(debug=True)
