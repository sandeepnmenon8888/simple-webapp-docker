from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello World"

@app.route('/read_file')
def read_file():
    try:
        with open('/data/testfile.txt', 'r') as file:
            return file.read()
    except FileNotFoundError:
        return "File not found."

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
