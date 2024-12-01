# Utilizando a imagem oficial do Python
FROM python:3.9-slim

# Definindo o diretório de trabalho
WORKDIR /app

# Copiando os arquivos para o contêiner
COPY . .

# Instalando as dependências
RUN pip install -r requirements.txt

# Executando o backend
CMD ["python", "app.py"]
