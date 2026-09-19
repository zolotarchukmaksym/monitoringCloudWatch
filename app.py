from flask import Flask
import i_broke_my_app
app = Flask(__name__)

@app.route('/health')
def hello():
    # Якщо в лабораторній замість ${custom_identifier} вказано конкретне значення - впишіть його
    return 'Hello from the environment ar11voam!'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
