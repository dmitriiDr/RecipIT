from flask import Flask, request, jsonify, render_template
import requests
import os

app = Flask(__name__)

LLAMA_API_URL = "http://llama3.2_server:11434/api/generate"

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/cookbook')
def cookbook():
    return render_template('cookbook.html')

@app.route('/get_recipe', methods=['POST'])
def get_recipe():
    data = request.json
    ingredients = data.get("ingredients", "")

    if not ingredients:
        return jsonify({"error": "No ingredients provided"}), 400

    payload = {
    "model": "llama3.2",
    "prompt": f"Create a recipe using these ingredients: {ingredients}",
    "max_tokens": 150,
    }

    try:
        # Send request to Llama API
        response = requests.post(LLAMA_API_URL, json=payload)
        response.raise_for_status()  # Raise HTTPError for bad responses
        
        result = response.json()
        recipe = result.get("text", "No recipe generated.")
        return jsonify({"recipe": recipe}), 200
    except requests.exceptions.RequestException as e:
        print("Error communicating with Llama API:", str(e))
        return jsonify({"error": "Failed to generate recipe. Please try again."}), 500

if __name__ == '__main__':
    app.run(debug=True)
