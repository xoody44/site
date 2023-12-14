from flask import Flask, render_template, request, redirect
from flask_login import LoginManager, UserMixin
from flask_sqlalchemy import SQLAlchemy
import redis
from buy_message import send_message, get_email
from config import DB_NAME

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
db = SQLAlchemy(app)
manager = LoginManager(app)


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), nullable=False, unique=True)
    password = db.Column(db.String(100), nullable=False)


# with app.app_context():
#    mail = db.session.execute(db.select(email)).scalars()


@manager.user_loader
def load_user(user_id):
    return Post.get(user_id)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/buy')
def buy():
    return render_template('buy.html')


@app.route('/calc')
def calc():
    return render_template('calc.html')


@app.route('/help')
def other_help_info():
    return render_template('help.html')


@app.route('/reviews')
def reviews():
    return render_template('reviews.html')


@app.route('/form', methods=['POST', 'GET'])
def form():
    if request.method == "POST":
        email: str = request.form['email']
        password: str = request.form['password']
        post = Post(email=email, password=password)
        try:
            db.session.add(post)
            db.session.commit()
            send_message(recipient=get_email(), message="test")
            # with redis.Redis() as client:
            #     client.set("email", str(email))
            #     recipient = str(client.get("email"))
            #     message = "test"
            #     send_message(recipient=recipient, message=message)
            #     client.flushdb()
            return redirect('/')
        except Exception as _ex:
            return f'ошибка, с.м. ниже\n{_ex}'
    else:
        return render_template('form.html')


if __name__ == '__main__':
    app.run(host="127.0.0.1", port=5000)

# env\Scripts\activate $env:FLASK_APP = "main.py" $env:FLASK_DEBUG=1
