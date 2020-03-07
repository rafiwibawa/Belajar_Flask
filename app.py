from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return 'Web Programming Unpas !!!!!'

@app.route('/login')
def login():
    return 'login'

if __name__ == '__main__':
    app.run(debug=True)