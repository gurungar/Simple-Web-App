from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm

app = Flask(__name__)

app.config['SECRET_KEY'] = '5d07e92d6a3608729cb6a801fc621765e9198e60c9cb190ab0865cbfbbbbb52e'

posts = [
    {
        'author': "Arjun Gurung",
        'title': 'blog Post 1',
        'content': 'First Post Content',
        'date posted': 'February 15, 2019'
    },
    {
        'author': 'Jane Doe',
        'title': 'blog Post 2',
        'content': 'Second Post Content',
        'date posted': 'February 16, 2019'
    }

]
@app.route("/")
@app.route("/home/")
def home():
    return render_template("home.html", posts=posts)


@app.route("/about/")
def about():
    return render_template("about.html", title='About')


@app.route("/register/", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)



@app.route("/login/", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash(f'You have been logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check username and password', 'danger')
    return render_template('login.html', title='Login', form=form)


'''
Test the register and login pages without any format
'''

@app.route("/registerwithoutlayout/", methods=['GET', 'POST'])
def registerWithout():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('test.html', title='Register-test', form=form)


@app.route("/testlogin/", methods=['GET', 'POST'])
def testLogin():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash(f'You have been logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check username and password', 'danger')
    return render_template('testlogin.html', title='Login-test', form=form)

if __name__ == "__main__":
    app.run(debug=True)
