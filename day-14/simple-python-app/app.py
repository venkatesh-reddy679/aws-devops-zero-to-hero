from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    a=1
    b=2
    c=a+b
    return f"output is {c}"
@app.route('/testme')
def hello():
    return "heyy this is a test api for triggering the aws codepipeline"
if __name__ == '__main__':
    app.run()

