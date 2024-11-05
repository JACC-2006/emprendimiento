from flask import Flask, render_template, url_for, request, redirect, flash, session
from werkzeug.security import generate_password_hash, check_password_hash
from functools import wraps
# from flask_sqlalchemy import SQLAlchemy
#
app = Flask(__name__)
app.secret_key = 'tu_clave_secreta'
#
# username = "prueba"
# password = "1234"
# hostname = "localhost"
# database = "pagina"
# driver = "ODBC+Driver+17+for+SQL+Server"
#
# app.config['SQLALCHEMY_DATABASE_URI'] = f"mssql+pyodbc://{username}:{password}@{hostname}/{database}?driver={driver}"
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# db = SQLAlchemy(app)

# class Tarea(db.Model):
#     __tablename__ = 'tarea'
#     id = db.Column(db.Integer, primary_key=True)
#     nombre = db.Column(db.String(100), nullable=False)
#     fecha = db.Column(db.Date, nullable=True)
#     completada = db.Column(db.Boolean, default=False)



usuarios = {
    "estudiante": {
        "password": generate_password_hash("12345"),
        "rol": "estudiante"
    },
    "profesor": {
        "password": generate_password_hash("1234"),
        "rol": "profesor"
    }
}

@app.before_request
def clear_session():
    if request.endpoint == 'login' and 'username' not in session:
        session.clear()

def require_login(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'username' not in session:
            return redirect(url_for('login'))
        return f(*args, **kwargs)

    return decorated_function

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if username in usuarios and check_password_hash(usuarios[username]["password"], password):
            session['username'] = username
            session['rol'] = usuarios[username]["rol"]
            print(f"Usuario '{username}' ha iniciado sesión como {session['rol']}.")
            if session['rol'] == 'estudiante':
                return redirect(url_for('home_estudiante'))
            elif session['rol'] == 'profesor':
                return redirect(url_for('home_profesor'))
        else:
            flash("Credenciales incorrectas")
            return redirect(url_for('login'))

    return render_template('login.html')

@app.route('/home_estudiante')
@require_login
def home_estudiante():
    print("Acceso autorizado a la página principal del estudiante.")
    return render_template('index.html')

@app.route('/home_profesor')
@require_login
def home_profesor():
    return render_template('home_profesor.html')

@app.route('/mis_clases')
def mis_clases():
    return render_template('mis_clases.html')


@app.route('/logout')
@require_login
def logout():
    session.pop('username', None)
    session.pop('rol', None)
    return redirect(url_for('login'))


@app.route('/home')
@require_login
def home():
    print("Acceso autorizado a la página principal.")
    return render_template('index.html')

@app.route('/')
@require_login
def index():
    if 'username' in session:
        return redirect(url_for('home'))
    return redirect(url_for('login'))


@app.route('/clases')
@require_login
def clases():
    return render_template('clases.html')

# @app.route('/tareas')
# @require_login
# def tareas():
#     return render_template('tareas.html')

@app.route('/drive')
@require_login
def drive():
    return render_template('drive.html')

@app.route('/perfil')
@require_login
def perfil():
    return render_template('perfil.html')

# @app.route('/tareas_alumno')
# def tareas_alumno():
#     tareas = Tarea.query.all()
#     return render_template('tareas_alumno.html', tareas=tareas)



# @app.route('/asignar_tarea', methods=['GET', 'POST'])
# def asignar_tarea():
#     if request.method == 'POST':
#         tarea_nombre = request.form['nombre']
#         fecha_str = request.form.get('fecha')
#         nueva_tarea = Tarea(nombre=tarea_nombre, fecha=fecha_str)
#
#         try:
#             db.session.add(nueva_tarea)
#             db.session.commit()
#             flash("Tarea asignada correctamentse.")
#         except Exception as e:
#             db.session.rollback()
#             flash(f"Error al asignar la tarea: {e}")
#
#     return render_template('asignar_tarea.html')


if __name__ == '__main__':
    # app.run(debug=True)
    # with app.app_context():
    #     db.create_all()
    app.run(debug=True)







