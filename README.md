# Projeto: Estudo de Pricing - Venda de Tênis Masculinos no Mercado Livre

## 📄 Descrição
Este projeto realiza um **estudo de pricing** com foco em tênis masculinos anunciados no Mercado Livre. O objetivo é coletar, processar e armazenar informações sobre os produtos, como preços antigos, preços atuais e número de avaliações, para possibilitar uma análise detalhada e visualização desses dados em uma aplicação hospedada no **Azure Web App**.

---

## 📊 Objetivos do Projeto
1. **Coleta de Dados**: Extrair informações de preços e detalhes dos produtos diretamente do Mercado Livre.
2. **Processamento**: Realizar:
   - Tratamento de dados faltantes.
   - Cálculo de preços completos a partir de reais e centavos.
   - Conversão e limpeza de número de avaliações.
3. **Armazenamento**:
   - Salvar os dados processados em um banco de dados SQLite (`quotes.db`).
4. **Visualização**:
   - Implantar a aplicação Python em um **Azure Web App**, disponibilizando os resultados processados para consulta.

---

## 🚀 Tecnologias Utilizadas

### Linguagens e Ferramentas
- **Python 3.10**
- **SQLite**: Banco de dados local para armazenamento dos resultados processados.

### Bibliotecas Python
- `pandas`: Manipulação e transformação de dados.
- `sqlite3`: Conexão com o banco de dados local.
- `datetime`: Registro de data e hora da coleta dos dados.

### DevOps
- **GitHub Actions**: Para automação do pipeline de build e deploy.
- **Azure Web Apps**: Hospedagem da aplicação.

---

## 🔨 Estrutura do Projeto

```plaintext
src/
├── data/
│   ├── resultado.jsonl  # Dados extraídos do Mercado Livre em formato JSON Lines
│   ├── resultado.csv    # Dados processados em formato CSV
│   └── quotes.db        # Banco de dados SQLite com os dados finais
├── app.py               # Aplicação principal (código Python)
├── requirements.txt     # Dependências do projeto
.github/
├── workflows/
│   └── main.yml         # Pipeline CI/CD para build e deploy
README.md                # Documentação do projeto
```

---

## 🚜 Pipeline CI/CD

O projeto utiliza um **workflow do GitHub Actions** para realizar o build e deploy automáticos.

### Principais Etapas
1. **Build**:
   - Configura o ambiente Python.
   - Instala as dependências especificadas em `requirements.txt`.
   - Compacta os arquivos do projeto para criação de um artefato de deploy.

2. **Deploy**:
   - Faz login no Azure utilizando as credenciais armazenadas como segredos no repositório.
   - Publica a aplicação no Azure Web App.

---

## 🔍 Resultados Esperados
Com a implantação do projeto, os seguintes resultados são esperados:

1. **Análise de Preços**:
   - Visualizar os preços antigos e atuais de tênis masculinos no Mercado Livre.
   - Identificar padrões e descontos nos produtos.

2. **Monitoramento**:
   - Oferecer dados centralizados e processados para futuras análises ou estudos.

3. **Acessibilidade**:
   - Disponibilizar uma interface web que permite o acesso direto aos dados processados.

---

## 💡 Como Configurar o Projeto Localmente

### **Requisitos**
- Python 3.10 ou superior
- Pip

### **Passos**
1. Clone o repositório:
   ```bash
   git clone https://github.com/seuusuario/seuprojeto.git
   ```

2. Navegue até o diretório do projeto:
   ```bash
   cd seuprojeto
   ```

3. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

4. Configure o ambiente:
   - Certifique-se de que os arquivos **`resultado.jsonl`**, **`resultado.csv`** e **`quotes.db`** estejam presentes no diretório `src/data`.

5. Execute a aplicação:
   ```bash
   python app.py
   ```

---

## 🏢 Contribuição
Fique à vontade para abrir issues ou pull requests caso deseje contribuir com melhorias ao projeto.

---

## ✨ Autor
**[Seu Nome]**  
- LinkedIn: [SeuPerfil](https://linkedin.com/in/seuperfil)
- GitHub: [SeuUsuario](https://github.com/seuusuario)


python -m venv venv
source venv/bin/activate  # No Windows: venv\Scripts\activate
pip install -r requirements.txt
streamlit run src/dashboard/dashboard.py
streamlit run src/dashboard/dashboard.py --server.port=8000 --server.address=0.0.0.0
