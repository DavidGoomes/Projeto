from flask import render_template, url_for, redirect
from Projeto import app, database, bcrypt
from flask_login import login_required, login_user, logout_user, current_user
from Projeto.models import Usuario
from Projeto.forms import FormLogin, FormCriarConta

@app.route("/", methods=["GET", "POST"])
def homepage():
    formLogin = FormLogin()
    if formLogin.validate_on_submit():
        return redirect(url_for('perfil'))
    return render_template('home.html', form=formLogin)


@app.route('/criar-conta', methods=["GET", "POST"])
def criarconta():
    formcriarconta = FormCriarConta()
    if formcriarconta.validate_on_submit():
        senha = bcrypt.generate_password_hash(formcriarconta.senha.data)
        usuario = Usuario(username=formcriarconta.username.data, email=formcriarconta.email.data, senha=senha)

        database.session.add(usuario)
        database.session.commit()
        login_user(usuario, remember=True)
        return redirect(url_for('perfil', usuario=usuario.username))
    return render_template('criarconta.html', form=formcriarconta)


@app.route('/user/<username>')
def user_profile(username):
    return render_template('user.html', username=username)


@app.route('/post/<int:post_id>')
def post_detail(post_id):
    return render_template('post.html', post_id=post_id)


@app.route('/Tarefa')
@login_required
def perfil():
    return render_template('user.html', usuario=Usuario)
