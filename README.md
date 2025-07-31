
# Projet IA2 - Recherche d’Images par Contenu (CBIR)

## Objectif du Projet

Ce projet consiste à implémenter un système CBIR (Content-Based Image Retrieval) qui permet de retrouver les images les plus similaires à une image requête en se basant sur des descripteurs de texture. Il a été réalisé dans le cadre du cours IA2 à l’Institut Teccart.

## Technologies Utilisées

- Python 3.12
- OpenCV
- Mahotas
- scikit-image
- Streamlit

## Structure du Projet

```
projet-2/
│
├── app_cbir_streamlit.py
├── CBIR_Distances.py
├── CBIR_Recherche.py
├── extract_features.py
├── requete.jpg
├── requirements.txt
├── README.md
│
└── dataset/
    ├── images/
    │   ├── lena.png
    │   ├── nature.jpg
    │   ├── ...
    │
    ├── bit.csv
    ├── glcm.csv
    └── haralick.csv

```

## Fonctionnalités Principales

- Upload d'une image requête via Streamlit
- Choix du descripteur (GLCM, Haralick, Bit)
- Choix de la mesure de distance (Euclidienne, Manhattan, Tchebychev, Canberra)
- Affichage des **Top N images** les plus similaires avec leurs distances
- Extraction automatique des caractéristiques de toutes les images dans `dataset/images` et sauvegarde au format `.csv`

## Étapes pour Exécuter le Projet

1. Installer les bibliothèques nécessaires :
   ```bash
   pip install opencv-python-headless mahotas scikit-image streamlit
   ```

2. Lancer l’extraction des descripteurs :
   ```bash
   python extract_features.py
   ```

3. Démarrer l’interface Streamlit :
   ```bash
   streamlit run app_cbir_streamlit.py
   ```

4. Utiliser l’interface :
   - Sélectionner une image
   - Choisir un descripteur
   - Choisir une distance
   - Choisir le nombre de résultats à afficher
   - Lancer la recherche

## Réalisé par

Nom de l’étudiant : Salaheddine Fikri 
Cours : Vision Artificielle et Reconnaissance de Formes (IA-2)  
Session : Été 2025  
Établissement : Institut Teccart
