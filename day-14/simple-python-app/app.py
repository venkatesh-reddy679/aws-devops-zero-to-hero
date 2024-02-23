from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
<<<<<<< HEAD
    return 'Hello, world! venky'
=======
    return 'Hello, world! venkateswara reddy!'
>>>>>>> 45c75e3bb89541d56f3494b89614da23bcdd7a3f


if __name__ == '__main__':
    app.run()

