from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "<h1>Flask app v2 - STABLE</h1><p>Hello from the environment ar11voam!</p>", 200

@app.route('/health')
def health():
    return "OK", 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
