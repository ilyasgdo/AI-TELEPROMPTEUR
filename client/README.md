# AI Téléprompteur - Version Client

Version standalone qui fonctionne **sans serveur** ! Tout fonctionne dans le navigateur.

## Comment utiliser

1. Ouvrez `index.html` directement dans Chrome, Firefox ou Edge
2. C'est tout ! Aucune installation requise.

## Fonctionnalités

- Saisie de texte avec surlignage (5 couleurs)
- Taille et vitesse ajustables
- Contrôle par main (MediaPipe Hands dans le navigateur)
- Mode miroir pour teleprompteur physique
- Mode Auto / Manuel
- Prévisualisation caméra avec détection des mains

## Prérequis

- Navigateur moderne (Chrome 80+, Firefox 75+, Edge 80+)
- Webcam
- Connexion internet (pour charger MediaPipe la première fois)

## Mode hors-ligne

Après la première utilisation, le navigateur met en cache les fichiers MediaPipe. Vous pouvez ensuite utiliser l'application hors-ligne.

## Technologies

- **MediaPipe Hands** - Détection de mains via WebAssembly/WebGL
- **Canvas API** - Dessin des landmarks
- **requestAnimationFrame** - Défilement fluide

## Note

Le fichier doit être servi via HTTP(S) ou localhost pour que l'accès caméra fonctionne. 
Si vous ouvrez directement le fichier (file://), certains navigateurs pourraient bloquer l'accès à la caméra.

Solutions :
- `python -m http.server 8000` puis http://localhost:8000
- Ou utilisez un IDE comme VS Code avec Live Server
