from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    return "<h1>Hello, World! Deployed via Jenkins & OpenShift with app source files and Dockerfile in Git Repo 🚀</h1>"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
