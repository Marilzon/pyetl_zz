# Imagem e versão.
FROM python:3.10-slim

# Diretório de trabalho do container.
WORKDIR /app

# Copia o requirements.txt local para o diretório de trabalho do container.
COPY requirements.txt requirements.txt

# Instala as dependências Python gravadas em requirements.txt.
RUN pip3 install -r requirements.txt

# Copia todos o conteúdos locais para o diretório de trabalhodo container.
COPY . .

# Define a variável de ambiente para inicialização da aplicação.
ENV FLASK_APP=src/main.py

# Comando a ser executado quando o container for iniciado.
CMD ["python3", "-m", "flask", "run", "--host=0.0.0.0"]
