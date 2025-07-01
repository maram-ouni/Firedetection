
🔥 Firedetection
Étapes pour exécuter le projet
1-Cloner le dépôt :
Ouvrez votre terminal (CMD ou PowerShell) et exécutez les commandes suivantes :

git clone https://github.com/maram-ouni/Firedetection.git
cd Firedetection
code .

2-Configurer l’environnement virtuel :
Dans le terminal intégré de VS Code, exécutez les commandes suivantes :
python -m venv venv
.\venv\Scripts\Activate
pip install -r requirements.txt


3-Modifier les chemins :
Dans le fichier test.py, mettez à jour :

le chemin de la vidéo d'entrée,

le chemin du fichier best.pt (modèle entraîné).

4-Exécuter le modèle :
Lancez la détection avec la commande suivante :
python3 "chemin_complet_du_fichier"\test.py
