from flask import render_template
from flask.helpers import flash
from flask import redirect
from app import app 
from app.forms import LoginForm
from app.models import User
from flask_login import login_user, current_user


@app.route('/')
@app.route('/index')

def index ():
    users = [
        {'id':'sv1','name': 'Phu'},
        {'id':'sv2','name': 'Nguyen'},
        {'id':'sv3','name': 'ABC'},
        {'id':'sv4','name': 'CDE'}
        ]
    return render_template('index.html',title= 'my title', users = users)

@app.route('/login', methods = ['GET','POST'])
def Login():
    #kiem tra user (current_user) da duoc xac thuc hay chua 
    if current_user.is_authenticated:
        return redirect('/index')
    form = LoginForm()
    
    #nguoi dung nhập dữ liệu 
    if form.validate_on_submit():
         #kiểm tra username từ form có trung  vs username trong db 
        user = User.query.filter_by(username=form.username.data,password= form.password.data).first()
        if user is None:
             flash('Invalid username or password ')
             return redirect('/login')

        flash('Login of user {} '.format(form.username.data))
        login_user(user)
        return redirect('/index')
    return render_template('Login.html', title = 'Sign in', form =form)
