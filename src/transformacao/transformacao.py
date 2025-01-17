import pandas as pd
import sqlite3
from datetime import datetime

# Leitura do arquivo JSONL
df = pd.read_json('src/data/resultado.jsonl', lines=True)

# Adicionando colunas de origem e data de coleta
df['_source'] = "https://lista.mercadolivre.com.br/tenis-corrida-masculino"
df['_data_coleta'] = datetime.now()

# Exibir todas as colunas no print
pd.options.display.max_columns = None

# Preenchendo valores nulos e convertendo para float
df['preco_antigo_reais'] = df['preco_antigo_reais'].fillna(0).astype(float)
df['preco_antigo_centavos'] = df['preco_antigo_centavos'].fillna(0).astype(float)
df['preco_novo_reais'] = df['preco_novo_reais'].fillna(0).astype(float)
df['preco_novo_centavos'] = df['preco_novo_centavos'].fillna(0).astype(float)

# Garantir que numero_reviews seja string antes de aplicar replace
df['numero_reviews'] = df['numero_reviews'].astype(str).str.replace('[\(\)]', '', regex=True)

# Substituir valores não numéricos por 0 e converter para int
df['numero_reviews'] = pd.to_numeric(df['numero_reviews'], errors='coerce').fillna(0).astype(int)

# Calcular preço completo
df['preco_antigo'] = df['preco_antigo_reais'] + df['preco_antigo_centavos'] / 100
df['preco_novo'] = df['preco_novo_reais'] + df['preco_novo_centavos'] / 100

# Remover colunas desnecessárias
df.drop(columns=['preco_antigo_reais', 'preco_antigo_centavos', 'preco_novo_reais', 'preco_novo_centavos'], inplace=True)

print(df)

# Conectar ao banco de dados SQLite e salvar dados
conn = sqlite3.connect('src/data/quotes.db')
df.to_sql('mercadolivre_items', conn, if_exists='replace', index=False)

conn.close()
