# Pricing Mercado Livre WebScraping

## Visão Geral

Este projeto é uma aplicação desenvolvida com Streamlit para realizar uma pesquisa de mercado de tênis esportivos no Mercado Livre. Ele utiliza web scraping para coletar dados e exibi-los em um painel interativo.

## Estrutura do Projeto

- `app.py` ou `dashboard.py`: Arquivo principal da aplicação Streamlit.
- `src/data/quotes.db`: Banco de dados SQLite contendo os dados coletados.
- `requirements.txt`: Arquivo listando todas as dependências do projeto.
- `run.sh`: Script para iniciar a aplicação.

## Dependências

As seguintes bibliotecas são necessárias para rodar a aplicação:

```plaintext
streamlit
pandas
numpy
matplotlib
sqlite3
altair
git clone https://github.com/stephanyborzi/Pricing_Mercado_Livre_WebScraping.git
cd Pricing_Mercado_Livre_WebScraping
python -m venv venv
source venv/bin/activate  # No Windows: venv\Scripts\activate
pip install -r requirements.txt
streamlit run src/dashboard/dashboard.py
streamlit run src/dashboard/dashboard.py --server.port=8000 --server.address=0.0.0.0
