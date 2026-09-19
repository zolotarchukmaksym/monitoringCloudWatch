from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    # Якщо в лабораторній замість ${custom_identifier} вказано конкретне значення - впишіть його
    return 'Hello from the environment ${custom_identifier}!'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
