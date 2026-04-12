# 🚜 AgroPeças - Sistema de Catálogo e Vendas

Este projeto visa resolver a dificuldade de produtores rurais em encontrar e orçar peças para maquinário pesado de forma ágil e remota.

## 🎯 Problema Real
Muitas lojas de peças de trator ainda operam de forma 100% manual ou por telefone, causando demora no atendimento e erros de identificação de peças, o que resulta em máquinas paradas e prejuízo no campo.

## 💡 Proposta de Solução
Uma aplicação web (Flask) que serve como um catálogo digital interativo, onde o cliente pode visualizar as peças disponíveis e especificações técnicas de forma direta.

## 👥 Público-alvo
* Microempreendedores do ramo de autopeças agrícolas.
* Produtores rurais e operadores de maquinário pesado.

## ✨ Funcionalidades Principais
* **Catálogo Digital:** Visualização de peças com fotos, nomes e categorias.
* **Cadastro de Itens:** Interface para adição de novas peças e upload de imagens reais.
* **Filtro de Preços:** Exibição clara de valores para agilizar o orçamento.
* **Interface Responsiva:** Acesso facilitado via dispositivos móveis no campo.

## 🛠 Tecnologias Utilizadas
* **Linguagem:** Python 3.13
* **Framework Web:** Flask
* **Estilo:** Bootstrap 5
* **Testes:** Pytest
* **CI/CD:** GitHub Actions

## 🚀 Como Instalar e Executar
1. **Clone o repositório:**
   `git clone https://github.com/Betoesu/df_tratores_project.git`
2. **Crie o ambiente virtual (venv):**
   `python -m venv venv`
3. **Instale as dependências:**
   `pip install -r requirements.txt`
4. **Execute a aplicação:**
   `python src/app.py`
   *(Acesse em http://127.0.0.1:5000)*

## 🧪 Testes e Qualidade (Lint)
* **Para rodar os testes:** `python -m pytest`
* **Para rodar o lint (análise estática):** `flake8 src`

## 📌 Versão Atual
1.0.0 (Versionamento Semântico)

## 👤 Autor
**Pedro Sarmento** - Estudante de Ciência da Computação
**Repositório Público:** [https://github.com/Betoesu/df_tratores_project](https://github.com/Betoesu/df_tratores_project)

---
### 🛠 Verificação de CI/CD
Acompanhe o status das validações automáticas na aba **Actions** deste repositório.