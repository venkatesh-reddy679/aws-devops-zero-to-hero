from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    a=1
    b=2
    c=a+b
    return f"output is {c}"

if __name__ == '__main__':
    app.run()

