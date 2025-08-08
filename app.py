from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    data = request.get_json() or {}
    system_prompt = data.get('system_prompt', '')
    user_prompt = data.get('user_prompt', '')
    text_blocks = data.get('text_blocks', '')

    response_text = f"System: {system_prompt}\nUser: {user_prompt}\nTexts: {text_blocks}\n\n[Dummy agent response]"
    return jsonify({'output': response_text})

if __name__ == '__main__':
    app.run(debug=True)
