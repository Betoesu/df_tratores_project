from flask import Flask, render_template

app = Flask(__name__)

pecas = [
    {'nome': 'Mangueira Hidráulica', 'categoria': 'Mangueiras', 'preco': 150.00},
    {'nome': 'Rolamento de Esfera', 'categoria': 'Rolamentos', 'preco': 85.50},
    {'nome': 'Correia Industrial', 'categoria': 'Correias', 'preco': 45.00}
]

@app.route('/')
def home():
    # Isso vai procurar um arquivo chamado index.html dentro da pasta templates
    return render_template('index.html', loja="DF Tratores", produtos=pecas)

if __name__ == "__main__":
    app.run(debug=True)