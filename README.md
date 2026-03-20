# AI Téléprompteur avec Contrôle par Main

Application de téléprompteur avec contrôle de défilement par mouvement de main utilisant MediaPipe.

## Deux versions disponibles

### Version Client (recommandée) - `client/`
**Sans serveur, fonctionne directement dans le navigateur !**

1. Ouvrez `client/index.html` dans Chrome/Firefox
2. C'est tout !

```bash
# Ou avec un serveur local (recommandé pour l'accès caméra)
cd client
python -m http.server 8000
# Puis ouvrir http://localhost:8000
```

### Version Serveur (Python) - `app.py`
Nécessite Python et installe des dépendances.

```bash
pip install -r requirements.txt
python app.py
# Puis ouvrir http://localhost:8080
```

## Fonctionnalités

- Saisie de texte avec surlignage (5 couleurs)
- Taille du texte ajustable (24-120px)
- Vitesse de défilement (1-20)
- Contrôle par main (MediaPipe)
- Mode miroir pour teleprompteur physique
- Mode Auto / Manuel
- Prévisualisation caméra avec détection des mains
- Raccourcis clavier (Space, ↑↓, Escape)

## Surlignage

1. Sélectionnez du texte dans l'éditeur
2. Cliquez sur une couleur (jaune, vert, bleu, rose, orange)
3. Cliquez sur X pour retirer le surlignage

## Contrôles par main

| Geste | Action |
|-------|--------|
| Main ouverte | Le texte défile vers le haut |
| Main fermée | Le défilement s'arrête |
| Mouvement vertical | Ajuste la vitesse |

## Technologies

- **Version Client**: HTML5 + MediaPipe Hands (WebAssembly)
- **Version Serveur**: Flask + Flask-SocketIO + MediaPipe Python
