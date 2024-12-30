Write-Host "=============================="
Write-Host "   Bienvenue sur ColorWise    "
Write-Host "=============================="

# Vérifier si Python est installé
if (-Not (Get-Command python -ErrorAction SilentlyContinue)) {
    Write-Host "Python n'est pas installé. Veuillez l'installer avant de continuer." -ForegroundColor Red
    exit 1
}

# Afficher la version de Python
$pythonVersion = & python --version
Write-Host "Python détecté : $pythonVersion"

# Créer un environnement virtuel
if (-Not (Test-Path "./env")) {
    Write-Host "Création de l'environnement virtuel..."
    python -m venv env
    Write-Host "Environnement virtuel créé avec succès."
} else {
    Write-Host "Environnement virtuel détecté."
}

# Activer l'environnement virtuel
Write-Host "Activation de l'environnement virtuel..."
Set-Location env/Scripts
.\Activate.ps1
Set-Location ../..

# Installer les dépendances
if (Test-Path "./requirements.txt") {
    Write-Host "Installation des dépendances..."
    python -m pip install --upgrade pip
    pip install -r requirements.txt
    Write-Host "Dépendances installées avec succès."
} else {
    Write-Host "Fichier requirements.txt introuvable. Veuillez le vérifier." -ForegroundColor Red
    exit 1
}

# Vérification des fichiers nécessaires
if (-Not (Test-Path "./main.py")) {
    Write-Host "Fichier principal 'main.py' introuvable !" -ForegroundColor Red
    exit 1
}

if (-Not (Test-Path "./resources/logo.png")) {
    Write-Host "Logo manquant dans 'resources/logo.png'. Veuillez vérifier les fichiers." -ForegroundColor Yellow
}

if (-Not (Test-Path "./exemples.txt")) {
    Write-Host "Fichier d'exemples 'exemples.txt' introuvable." -ForegroundColor Yellow
}

# Lancer l'application
Write-Host "Lancement de ColorWise..."
python main.py

# Désactiver l'environnement virtuel après exécution
Write-Host "Désactivation de l'environnement virtuel..."
deactivate
Write-Host "Fin du script. Merci d'avoir utilisé ColorWise."
