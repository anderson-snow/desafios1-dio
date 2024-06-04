from flask import Flask, render_template, request
import openai

app = Flask(__name__)

# Configure sua chave de API do OpenAI
openai.api_key = 'sua-api-key-por-seguranca-nao-coloquei-a-minha'

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        prompt = request.form['prompt']
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=prompt,
            max_tokens=150
        )
        generated_text = response.choices[0].text.strip()
        return render_template('index.html', prompt=prompt, generated_text=generated_text)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
