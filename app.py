from flask import Flask, render_template, url_for, request,redirect
from flask_bootstrap import Bootstrap
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
Bootstrap(app)


app.config['SECRET_KEY'] = 'b613htY80Xf85Ak47'
DB_URI2 = "mysql+pymysql://root:luxmdm@localhost/eaglesight"
app.config['SQLALCHEMY_DATABASE_URI'] = DB_URI2
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = 'False'

db = SQLAlchemy(app)
loginManager = LoginManager()
loginManager.init_app(app)
loginManager.login_view = 'login'


@app.route('/home')
def home():
    return render_template('home.html')


@app.route('/info')
def devInfo():
    return render_template('devInfo.html')


@app.route('/data')
def devData():
    return render_template('devData.html')


@app.route('/operations')
def devOp():
    return render_template('devOp.html')


@app.route('/configs')
def devConfig():
    return render_template('devConfig.html')


@app.route('/')
@app.route('/login', methods=['GET', 'POST'])
def logout():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    error = False
    if request.method == 'POST':
        username = request.form['username']
        Password = request.form['password']
        rememberMe = request.form.get('remember')
        user = adminTable.query.filter_by(id=username).first()
        if user:
            if user.password == Password:
                login_user(user, remember=rememberMe)
                return redirect(url_for('home'))
            else:
                error = True
                return render_template('logout.html', error=error)
        else:
            error = True
            return render_template('logout.html', error=error)
    return render_template('logout.html')


@app.route('/logout')
def userLogout():
    logout_user()
    return redirect(url_for('logout'))


class adminTable(UserMixin, db.Model):
    __tablename__ = 'admin'
    id = db.Column('username', primary_key=True)
    password = db.Column('passw0rd', nullable=False)

    def __init__(self, username, password):
        self.username = username
        self.password = password


@loginManager.user_loader
def load_user(user_id):
    return adminTable.query.get(str(user_id))

if __name__ == "__main__":
    app.run(debug=True)