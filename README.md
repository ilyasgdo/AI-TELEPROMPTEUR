# 🎬 AI Téléprompteur avec Contrôle par Main

Application de téléprompteur avec contrôle de défilement par mouvement de main utilisant MediaPipe.

## Fonctionnalités

- ✍️ **Saisie de texte** - Collez ou tapez votre script
- 🎨 **Surlignage** - Surlignez des mots avec 5 couleurs différentes
- 📏 **Taille ajustable** - De 24px à 120px
- ⚡ **Vitesse de défilement** - Contrôlez la vitesse (1-20)
- ✋ **Contrôle par main** - Défilez avec vos mains (MediaPipe)
- 🔄 **Mode miroir** - Texte inversé pour teleprompteur physique
- 🎥 **Prévisualisation caméra** - Voyez la détection de main en temps réel
- ⌨️ **Raccourcis clavier** - Space (pause/play), flèches (vitesse)

## Surlignage

1. Sélectionnez du texte dans l'éditeur
2. Cliquez sur une couleur (jaune, vert, bleu, rose, orange)
3. Le texte sera surligné et affiché en couleur dans le téléprompteur
4. Cliquez sur ✕ pour retirer le surlignage

## Installation

```bash
pip install -r requirements.txt
```

## Utilisation

```bash
python app.py
```

Puis ouvrez http://localhost:8080 dans votre navigateur.

## Contrôles par main

| Geste | Action |
|-------|--------|
| ✋ Main ouverte | Le texte défile vers le haut |
| ✊ Main fermée | Le défilement s'arrête |
| ↕️ Mouvement vertical | Ajuste la vitesse |

## Raccourcis clavier (en mode plein écran)

- `Space` - Play/Pause
- `↑` - Augmenter vitesse
- `↓` - Diminuer vitesse
- `Escape` - Quitter

## Mode miroir

Activez "Texte inversé (miroir)" si vous utilisez un vrai teleprompteur avec un miroir. Le texte apparaîtra à l'endroit quand vous le regarderez à travers le miroir.

## Technologies

- **Backend**: Flask + Flask-SocketIO
- **Frontend**: HTML5, CSS3, JavaScript vanilla
- **Hand Tracking**: MediaPipe Hands
- **Communication temps réel**: WebSocket (Socket.IO)
