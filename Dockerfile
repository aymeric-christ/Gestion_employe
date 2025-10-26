# Étape 1 : choisir l'image Python
FROM python:3.13

# Étape 2 : définir le répertoire de travail
WORKDIR /app

# Étape 3 : copier les fichiers
COPY requirements.txt .

# Étape 4 : installer les dépendances
RUN pip install --no-cache-dir -r requirements.txt

# Étape 5 : copier tout le projet
COPY . .

# Étape 6 : collecter les fichiers statiques
RUN python manage.py collectstatic --noinput

# Étape 7 : lancer Gunicorn (serveur Django de prod)
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "gestion_employe.wsgi:application"]
