import flask_wtf
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo, Length, ValidationError
from Projeto.models import Usuario

class FormLogin(FlaskForm):
    email = StringField("E-mail", validators=[DataRequired(),Email()])
    username = StringField("Nome Do Usuário", validators=[DataRequired()])
    senha = PasswordField("Senha", validators=[DataRequired()])
    confirmacao_senha = PasswordField("Confirme a Senha", validators=[DataRequired(), EqualTo(senha)])
    botao_confirmacao = SubmitField("Fazer Login")

class FormCriarConta(FlaskForm):
    email = StringField("E-mail", validators=[DataRequired(),Email()])
    username = StringField("Nome Do Usuário", validators=[DataRequired()])
    senha = PasswordField("Senha", validators=[DataRequired(), Length(6,15)])
    confirmacao_senha = PasswordField("Confirme a Senha", validators=[DataRequired(), EqualTo(senha)])
    botao_confirmacao = SubmitField("Criar Conta")

def validate_email(self, email):
    usuario = Usuario.query.filter_by(email=email.data).first()
    if usuario:
        raise ValidationError("Email já Cadastrado. Faça login para Continuar.")
