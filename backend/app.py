from flask import Flask, request, jsonify
from flask_cors import CORS
import os
from algorithms.pattern_search import detect_sensitive_info

app = Flask(__name__)
CORS(app)

UPLOAD_FOLDER = 'uploads'
RESULTS_FOLDER = 'results'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(RESULTS_FOLDER, exist_ok=True)

@app.route('/upload', methods=['POST'])
def upload_file():
    file = request.files.get('file')
    if not file:
        return jsonify({'error': 'No file uploaded'}), 400
    filepath = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(filepath)
    return jsonify({'message': 'File uploaded successfully', 'path': filepath})

@app.route('/analyze', methods=['POST'])
def analyze_file():
    data = request.get_json()
    text = data.get('content', '')
    results = detect_sensitive_info(text)
    return jsonify({'results': results})

@app.route('/results', methods=['GET'])
def get_results():
    sample_results = {'emails': 2, 'passwords': 1, 'api_keys': 0, 'tokens': 3}
    return jsonify(sample_results)

if __name__ == '__main__':
    app.run(debug=True)
