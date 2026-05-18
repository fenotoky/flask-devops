from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello DevOps TP3"

@app.route('/hello/<username>')
def hello_name(username):
    return f'Hello {username}!'

if __name__ == '__main__':
    app.run(host='0.0.0.0')