# Usando uma imagem base do Python
FROM python:3.9-slim

# Setando o diretório de trabalho dentro do container
WORKDIR /app

# Copiando os arquivos necessários do projeto para o container
COPY . /app

# Instalando as dependências do projeto
RUN pip install --no-cache-dir -r requirements.txt

# Comando para rodar o script Python (apod_viewer.py)
CMD ["python", "apod_viewer.py"]
