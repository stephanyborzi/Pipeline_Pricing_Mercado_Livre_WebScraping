import streamlit as st
import pandas as pd
import sqlite3

def testar_conexao():
    try:
        conn = sqlite3.connect('src/data/quotes.db')
        conn.cursor().execute('SELECT 1')
        conn.close()
        return True
    except sqlite3.Error as e:
        st.error(f"Erro ao conectar ao banco de dados: {e}")
        return False

# Testar a conexão com o banco de dados
if testar_conexao():
    st.success('Conexão com o banco de dados estabelecida com sucesso!')
    conn = sqlite3.connect('src/data/quotes.db')
    df = pd.read_sql_query('SELECT * FROM mercadolivre_items', conn)
    conn.close()

    st.title('Pesquisa de Mercado - Tênis Esportivo Mercado Livre')
    st.subheader('KPIs principais do sistema')
    
    col1, col2, col3 = st.columns(3)
    total_itens = df.shape[0]
    col1.metric(label="Número Total de Itens", value=total_itens)
    unique_brands = df['marca'].nunique()
    col2.metric(label="Número de Marcas Únicas", value=unique_brands)
    avarage_new_price = df['preco_novo'].mean()
    col3.metric(label="Preço Médio Novo (R$)", value=f'{avarage_new_price:.2f}')

    # Marcas mais encontradas até a 10ª página
    st.subheader('Marcas mais encontradas até a 10ª página')
    col1, col2 = st.columns(2)
    top_10_pages_brands = df['marca'].value_counts().sort_values(ascending=False)
    col1.write(top_10_pages_brands)
    col2.bar_chart(top_10_pages_brands)
    
    # Preço médio por marca
    st.subheader('Preço Médio por Marca')
    col1, col2 = st.columns(2)
    df_rating_reviews = df[df['preco_novo'] > 0]
    avarage_price_by_brand = df_rating_reviews.groupby('marca')['preco_novo'].mean().sort_values(ascending=False)
    col1.write(avarage_price_by_brand)
    col2.bar_chart(avarage_price_by_brand)
    
    # Satisfação por marca
    st.subheader('Satisfação por marca')
    col1, col2 = st.columns(2)
    df_reviews = df[df['quantidade_reviews'] > 0]
    satisfation_by_brand = df_reviews.groupby('marca')['quantidade_reviews'].mean().sort_values(ascending=False)
    col1.write(satisfation_by_brand)
    col2.bar_chart(satisfation_by_brand)
else:
    st.error('Falha ao conectar ao banco de dados.')
