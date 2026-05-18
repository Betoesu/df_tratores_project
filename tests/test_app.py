import pytest
from src.app import app
from unittest.mock import patch

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

def test_carrinho_page_status_code(client):
    """Testa se a página do carrinho carrega via GET"""
    resposta = client.get('/carrinho')
    assert resposta.status_code == 200

def test_carrinho_consulta_cep_sucesso(client):
    """Teste de Integração: Valida a busca de CEP com resposta simulada (Mock)"""
    dados_retorno_api = {
        "cep": "72110-600",
        "logradouro": "QNE 16",
        "bairro": "Taguatinga Norte",
        "localidade": "Taguatinga",
        "uf": "DF"
    }
    
    # Simulamos a resposta do ViaCEP sem gastar internet
    with patch('src.app.requests.get') as mock_get:
        mock_get.return_value.json.return_value = dados_retorno_api
        mock_get.return_value.status_code = 200
        
        dados = {'cep': '72110600'}
        resposta = client.post('/carrinho', data=dados)
        
        assert resposta.status_code == 200
        assert b"taguatinga" in resposta.data.lower()
        assert b"qne 16" in resposta.data.lower()

def test_carrinho_consulta_cep_invalido(client):
    """Teste de Integração: Valida o tratamento de erro para CEP inexistente com Mock"""
    with patch('src.app.requests.get') as mock_get:
        mock_get.return_value.json.return_value = {"erro": "true"}
        mock_get.return_value.status_code = 200
        
        dados = {'cep': '00000000'}
        resposta = client.post('/carrinho', data=dados)
        
        assert resposta.status_code == 200
        assert b"cep" in resposta.data.lower() and b"localizado" in resposta.data.lower()