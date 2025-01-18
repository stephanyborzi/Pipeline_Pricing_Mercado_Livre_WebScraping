import pandas as pd
import sqlite3
from datetime import datetime

def testar_conexao():
    try:
        conn = sqlite3.connect('src/data/quotes.db')
        conn.cursor().execute('SELECT 1')
        conn.close()
        print("Conexão com o banco de dados estabelecida com sucesso!")
        return True
    except sqlite3.Error as e:
        print(f"Falha ao conectar ao banco de dados: {e}")
        return False

# Testar a conexão com o banco de dados
if testar_conexao():
    df = pd.read_json('src/data/resultado.jsonl', lines=True)

    df['_source'] = "https://lista.mercadolivre.com.br/tenis-corrida-masculino"
    df['_data_coleta'] = datetime.now()

    pd.options.display.max_columns = None

    df['preco_antigo_reais'] = df['preco_antigo_reais'].fillna(0).astype(float)
    df['preco_antigo_centavos'] = df['preco_antigo_centavos'].fillna(0).astype(float)
    df['preco_novo_reais'] = df['preco_novo_reais'].fillna(0).astype(float)
    df['preco_novo_centavos'] = df['preco_novo_centavos'].fillna(0).astype(float)

    df['numero_reviews'] = df['numero_reviews'].astype(str).str.replace('[\(\)]', '', regex=True)
    df['numero_reviews'] = pd.to_numeric(df['numero_reviews'], errors='coerce').fillna(0).astype(int)

    df['preco_antigo'] = df['preco_antigo_reais'] + df['preco_antigo_centavos'] / 100
    df['preco_novo'] = df['preco_novo_reais'] + df['preco_novo_centavos'] / 100

    df.drop(columns=['preco_antigo_reais', 'preco_antigo_centavos', 'preco_novo_reais', 'preco_novo_centavos'], inplace=True)

    print(df)

    conn = sqlite3.connect('src/data/quotes.db')
    df.to_sql('mercadolivre_items', conn, if_exists='replace', index=False)
    conn.close()
else:
    print("Não foi possível conectar ao banco de dados. Verifique sua configuração.")
