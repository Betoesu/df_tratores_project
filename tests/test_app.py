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