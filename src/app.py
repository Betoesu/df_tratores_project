import os
from flask import Flask, render_template, request, redirect, url_for
from werkzeug.utils import secure_filename 
import requests


app = Flask(__name__)

@app.template_filter('moeda')
def formato_moeda(valor):
    """Filtro personalizado para formatar floats no padrão R$ 0,00"""
    try:
        return f"R$ {float(valor):.2f}".replace('.', ',')
    except (ValueError, TypeError):
        return f"R$ {valor}"

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
    return render_template('home.html', loja="DF Tratores", produtos=pecas)


@app.route('/adicionar', methods=['GET', 'POST'])
def adicionar_peca():
    if request.method == 'POST':
        arquivo = request.files.get('imagem')
        
        if arquivo:
            nome_arquivo = secure_filename(arquivo.filename)
            arquivo.save(os.path.join(app.config['UPLOAD_FOLDER'], nome_arquivo))
            caminho_imagem = f'img/{nome_arquivo}'
        else:
            caminho_imagem = 'img/placeholder.jpg'

        # TRATAMENTO DE ERRO: Garante que o preço seja um número válido
        raw_preco = request.form.get('preco')
        try:
            preco_final = float(raw_preco) if raw_preco else 0.0
        except ValueError:
            preco_final = 0.0

        nova_peca = {
            'nome': request.form.get('nome'),
            'categoria': request.form.get('categoria'),
            'preco': preco_final,
            'imagem': caminho_imagem
        }

        pecas.append(nova_peca)
        return redirect(url_for('home'))
    
    return render_template('adicionar.html')

@app.route('/carrinho', methods=['GET', 'POST'])
def carrinho():
    # 🚨 AS LINHAS SALVADORAS: Elas DEVEM começar valendo None
    endereco = None
    erro = None
    
    # Busca a primeira peça do catálogo para exibir na tela
    peca_selecionada = pecas[0] if pecas else None

    if request.method == 'POST':
        cep_usuario = request.form.get('cep')
        cep_limpo = cep_usuario.replace("-", "").strip()

        if len(cep_limpo) != 8 or not cep_limpo.isdigit():
            erro = "Por favor, digite um CEP válido com 8 números."
        else:
            try:
                url = f"https://viacep.com.br/ws/{cep_limpo}/json/"
                resposta = requests.get(url, timeout=5)
                dados_api = resposta.json()

                if 'erro' in dados_api:
                    erro = "CEP não localizado em nossa base de dados agrícola."
                else:
                    endereco = dados_api # Aqui ela ganha o valor da API se der certo

            except requests.exceptions.RequestException:
                erro = "Não foi possível conectar ao serviço de frete. Tente novamente."

    # Quando chegar aqui no GET, endereco valerá None (e o Jinja vai entender e esconder o bloco)
    return render_template('carrinho.html', peca=peca_selecionada, endereco=endereco, erro=erro)
    


if __name__ == '__main__':
    import os
    # O Render injeta a porta correta nesta variável de ambiente chamada PORT
    porta = int(os.environ.get("PORT", 5000))
    
    # host='0.0.0.0' abre as portas para a internet do Render receber as visitas
    app.run(host='0.0.0.0', port=porta)