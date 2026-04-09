import os
from flask import Flask, render_template, request, redirect, url_for
from werkzeug.utils import secure_filename 

app = Flask(__name__)

UPLOAD_FOLDER = 'src/static/img'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

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

        arquivo = request.files.get('imagem')
        
        if arquivo:
            # Limpa o nome do arquivo e salva na pasta static/img
            nome_arquivo = secure_filename(arquivo.filename)
            arquivo.save(os.path.join(app.config['UPLOAD_FOLDER'], nome_arquivo))
            caminho_imagem = f'img/{nome_arquivo}'
        else:
            caminho_imagem = 'img/placeholder.jpg' # Caso não envie foto

        nova_peca = {
            'nome': request.form.get('nome'),
            'categoria': request.form.get('categoria'),
            'preco': float(request.form.get('preco')),
            'imagem': caminho_imagem
        }

        pecas.append(nova_peca)
        return redirect(url_for('home'))
    
    return render_template('adicionar.html')









































if __name__ == "__main__":
    app.run(debug=True)