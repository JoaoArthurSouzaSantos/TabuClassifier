# Usar uma imagem base Python
FROM python:3.9-slim

# Definir o diretório de trabalho dentro do container
WORKDIR /app

# Instalar as dependências do sistema
RUN apt-get update && apt-get install -y \
    build-essential \
    libssl-dev \
    libffi-dev \
    default-libmysqlclient-dev \
    && rm -rf /var/lib/apt/lists/*

# Copiar os arquivos de dependências para o container
COPY requirements.txt requirements.txt

# Instalar as dependências Python
RUN pip install --no-cache-dir -r requirements.txt

# Copiar todo o código do projeto para o diretório de trabalho do container
COPY . .

# Expor a porta 5000 para o Flask
EXPOSE 5000

# Comando para rodar a aplicação Flask
CMD ["python", "app.py"]
