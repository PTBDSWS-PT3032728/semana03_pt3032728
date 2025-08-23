from flask import Flask, request
from flask_bootstrap import Bootstrap
from flask_moment import Moment 
app = Flask(__name__)
bootstrap = Bootstrap(app)
moment = Moment(app)

@app.route('/')
def index():
    return render_template('index.html', current_time=datetime.utcnow())

@app.route('/user/<nome>')
def user(nome):
    return render_template('user.html', nome = nome)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errohandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500