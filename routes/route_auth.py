from flask import Flask, url_for, render_template, request, redirect, session, Blueprint
from models.user_model import User
from app import db

app_auth = Blueprint('route_auth', __name__, url_prefix="/auth", template_folder="frontend/templates", static_folder="frontend/static")

@app_auth.route('/login', methods=['GET', 'POST'])
def login():
    """Login Form"""
    if request.method == 'GET':
        return render_template('login.html')
    else:
        name = request.form['username']
        passw = request.form['password']
        # Verificando diretamente no banco de dados se o usuário e a senha são válidos
        data = User.query.filter_by(username=name, password=passw).first()

        if data:
            session['logged_in'] = True
            return redirect(url_for('route_algorithms.index'))  # Redireciona para a página principal
        else:
            # Se login inválido, retorna a página de login com mensagem de erro
            return render_template('login.html', error='Nome de usuário ou senha inválidos')


@app_auth.route('/register', methods=['GET', 'POST'])
def register():
    """Register Form"""
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if User.query.filter_by(username=username).first():
            return "User already exists", 400  # Evitar duplicação de usuários
        new_user = User(username=username, password=password)
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for('login'))
    return render_template('register.html')


@app_auth.route("/logout")
def logout():
    """Logout Form"""
    session['logged_in'] = False
    return redirect(url_for('login'))

