from flask import Flask, render_template, request, redirect
#from flask_login import LoginManager, UserMixin
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///newflask.db'
db = SQLAlchemy(app)
#manager = LoginManager(app)


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), nullable=False, unique=True)
    password = db.Column(db.String(100), nullable=False)


#@manager.user_loader
#def load_user(user_id):
#    return Post.get(user_id)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/buy')
def buy():
    return render_template('buy.html')


@app.route('/form', methods=['POST', 'GET'])
def form():
    if request.method == "POST":
        email = request.form['email']
        password = request.form['password']
        post = Post(email=email, password=password)
        try:
            db.session.add(post)
            db.session.commit()
            return redirect('/')
        except:
            return 'ошибка'
    else:
        return render_template('form.html')


@app.route('/help')
def help():
    return render_template('help.html')


@app.route('/reviews')
def reviews():
    return render_template('reviews.html')


if __name__ == '__main__':
    app.run(host="127.0.0.1", port=5000)


# env\Scripts\activate $env:FLASK_APP = "main.py" $env:FLASK_DEBUG=1
