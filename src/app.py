from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

pecas = [
    {   
        'nome': 'Mangueira Hidráulica',
        'categoria': 'Mangueiras',
        'preco': 150.00,
        'imagem': 'img/mangueira.jpg',
    },

    {
        'nome': 'Rolamento de Esfera',
        'categoria': 'Rolamentos',
        'preco': 85.50,
        'imagem': 'img/rolamento.jpg'
    },
    
    {
        'nome': 'Correia Industrial',
        'categoria': 'Correias',
        'preco': 45.00,
        'imagem': 'img/correia.jpg',
    }
]

@app.route('/')
def home():
    # Isso vai procurar um arquivo chamado index.html dentro da pasta templates
    return render_template('index.html', loja="DF Tratores", produtos=pecas)


@app.route('/adicionar', methods=['GET', 'POST'])
def adicionar_peca():
    if request.method == 'POST':
        
        nova_peca = {
            'nome': request.form.get('nome'),
            'categoria': request.form.get('categoria'),
            'preco': float(request.form.get('preco')),
            'imagem': 'img/placeholder.jpg' # Por enquanto deixamos um padrão
        }

        pecas.append(nova_peca)

        return redirect(url_for('home'))
    return render_template('adicionar.html')









































if __name__ == "__main__":
    app.run(debug=True)