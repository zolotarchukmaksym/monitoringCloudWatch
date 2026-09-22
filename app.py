from flask import Flask
import broken_module

app = Flask(__name__)

@app.route('/')
def home():
    return "<h1>Flask app v3 - BROKEN</h1>", 500

@app.route('/health')
def health():
    return "FAIL", 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
