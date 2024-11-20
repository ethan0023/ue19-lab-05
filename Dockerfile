# Utiliser une image officielle de Python
FROM python:3.9-slim

# Définir l'auteur
LABEL authors="VotreNom"

# Définir le répertoire de travail
WORKDIR /app

# Copier les fichiers dans le conteneur
COPY . /app

# Installer les dépendances
RUN pip install --no-cache-dir -r requirements.txt

# Commande pour lancer l'application
CMD ["python", "app.py"]