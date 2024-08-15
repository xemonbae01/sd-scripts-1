from flask import Flask, request, jsonify
from your_model_script import generate_image  # Import your model script

app = Flask(__name__)

@app.route('/generate', methods=['POST'])
def generate():
    data = request.json
    prompt = data.get('prompt')
    image = generate_image(prompt)  # Replace with your model's function
    return jsonify({"image": image})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
