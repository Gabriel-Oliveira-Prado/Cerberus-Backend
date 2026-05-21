import os
import sys
import bcrypt
from dotenv import load_dotenv
import jsonify
from flask import Flask, flash, jsonify, redirect, render_template, request, app
from flask import session as flask_session
from flask_bcrypt import check_password_hash, generate_password_hash
from ..routes import model

load_dotenv()


app = Flask(__name__)
app.secret_key = os.getenv("FLASK_SECRET_KEY")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        infologin= request.get_json()
        mailuser = infologin.get("email")
        password = infologin.get("password")
        # Aqui você deve implementar a lógica para verificar o email e senha no banco de dados
        User = model.User.query.filter_by(email=mailuser).first()
        if User and check_password_hash(User.senha, password):
            flask_session["user_email"] = User.email  # Armazena o email do usuário na sessão
            return jsonify({"message": "Login bem-sucedido!"}), 200 #adicionar o redirect para a página de conectar com o banco de dados

    return jsonify({"message": "Credenciais inválidas!"}), 401

@app.route("/logout", methods=["POST"])
def logout():
    flask_session.pop("user_email", None)  # Remove o email do usuário da sessão
    return jsonify({"message": "Logout bem-sucedido!"}), 200 #adicionar o redirect para a página de login ou home após o logout, se necessário

@app.route("/register", methods=["POST"])
def register():
    inforegister = request.get_json()
    nome = inforegister.get("nome")
    mailuser = inforegister.get("email")
    password = inforegister.get("password")

    # Verifica se o email já existe no banco de dados
    if model.User.query.filter_by(email=mailuser).first():
        return jsonify({"message": "Email já registrado!"}), 400

    # Cria um novo usuário e salva no banco de dados
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')  # Hash da senha
    new_user = model.User(nome=nome, email=mailuser, senha=hashed_password)
    model.db.session.add(new_user)
    model.db.session.commit()

    return jsonify({"message": "Registro bem-sucedido!"}), 201 #adicionar o redirect para a página de login ou home após o registro, se necessário