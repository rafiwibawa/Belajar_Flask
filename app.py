from flask import Flask, render_template, request
app = Flask(__name__)

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
        return 'Email kamu Adalah '+ request.form['email']

    return render_template('login.html')

if __name__ == '__main__':
    app.run(debug=True)