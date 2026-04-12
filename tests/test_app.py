import pytest
from src.app import app

@pytest.fixture
def client():
    # Configura o Flask para modo de teste
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_home_status_code(client):
    """Testa se a página inicial carrega corretamente"""
    resposta = client.get('/')
    # assert verifica se uma condição é verdadeira. 200 significa "OK"
    assert resposta.status_code == 200

def test_home_content(client):
    """Testa se o nome da loja aparece na home (sem importar maiúsculas/minúsculas)"""
    resposta = client.get('/')
    assert b"df tratores" in resposta.data.lower()

def test_adicionar_page_status_code(client):
    """Testa se a página de adicionar está acessível"""
    resposta = client.get('/adicionar')
    assert resposta.status_code == 200

def test_cadastrar_peca_sucesso(client):
    """Testa o cadastro de uma nova peça (Caminho Feliz)"""
    dados = {
        'nome': 'Filtro de Ar',
        'categoria': 'Motores',
        'preco': '120.50'
    }
    resposta = client.post('/adicionar', data=dados, follow_redirects=True)
    assert resposta.status_code == 200
    # Ajustado para minúsculas para bater com o .lower()
    assert b"filtro de ar" in resposta.data.lower()

def test_cadastrar_peca_invalida(client):
    """Testa se o sistema lida com campos vazios (Entrada Inválida)"""
    dados_incompletos = {
        'nome': '', # Nome vazio
        'categoria': 'Motores',
        'preco': '' # Preço vazio
    }
    resposta = client.post('/adicionar', data=dados_incompletos)
    
    # O HTML tem 'required', mas o teste simula um envio direto.
    # Se o seu código Python não trata o erro, ele pode dar 500.
    # Um resultado aceitável aqui é o status 200 (recarregar a página) ou 400.
    assert resposta.status_code != 500