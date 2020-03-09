from flask import Flask, render_template, request, url_for, session, redirect
app = Flask(__name__)
app.secret_key = 'randostringapapun'

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
        session['username'] = request.form['email']

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