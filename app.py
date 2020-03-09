from flask import (Flask, render_template, request, abort,
                    url_for, session, redirect, flash)
app = Flask(__name__)
app.secret_key = 'randostringapapun'

@app.errorhandler(401)
def pag_not_found(e):
    return render_template('401.html'),401

@app.route('/')
def index():
    search = request.args.get('search')
    return render_template('index.html',search=search)

@app.route('/profile/<username>')
def show_profile(username):
    return render_template('profile.html', username=username)

@app.route('/login', methods=['GET','POST'])
def show_login():
    if request.method == 'POST':

        if request.form['password'] == '':
            abort(401)

        session['username'] = request.form['email']
        
        flash('kamu berhasil login', 'success')
        return redirect(url_for('show_profile', username=session['username']))

    if 'username' in session:
        username = session['username']
        return redirect(url_for('show_profile', username=username))

    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('show_login'))

if __name__ == '__main__':
    app.run(debug=True)