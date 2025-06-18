# Dockerfile para github-readme-downloader
FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Comando padrão: roda o script principal
ENTRYPOINT ["python", "baixar_readmes.py"]
