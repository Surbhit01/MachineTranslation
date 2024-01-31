from flask import Flask, jsonify, request
from flask_cors import CORS
from translator import translate

app = Flask(__name__)
CORS(app)
@app.route('/', methods=['GET'])
def home():
    if request.method == 'GET':
        data = "Hello world!"

        return jsonify({'data': data})
    

@app.route('/translate', methods=['POST'])
def translate_sentence():
    if request.method == 'POST':
        json_data = request.get_json(force=True)
        if 'data' in json_data:
            en_sentence = json_data['data']
            es_sentence = translate(en_sentence)


    return jsonify({'data': es_sentence})

if __name__ == "__main__":
    app.run(port=5000, debug=True)