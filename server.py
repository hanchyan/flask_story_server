from flask import Flask, send_from_directory

app = Flask(__name__, static_folder='.')

# Serve index.html
@app.route('/')
def index():
    return send_from_directory('.', 'index.html')

# Serve story.json
@app.route('/story2')
def story():
    return send_from_directory('.', 'story2.json')

# Serve images
@app.route('/images/<path:filename>')
def images(filename):
    return send_from_directory('images', filename)

if __name__ == '__main__':
    app.run(debug=True, port=8000)
