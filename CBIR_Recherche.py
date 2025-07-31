import csv
import cv2
import os
from CBIR_Distances import *
from extract_features import extraire_glcm, extraire_haralick, extraire_bit

def lire_csv(fichier):
    noms = []
    vecteurs = []
    with open(fichier, 'r') as f:
        lecteur = csv.reader(f)
        for ligne in lecteur:
            noms.append(ligne[0])
            vecteurs.append([float(val) for val in ligne[1:]])
    return noms, vecteurs

def comparer(image_chemin, fichier_descripteur, descripteur="glcm", distance="euclidienne", top_n=5):
    noms, vecteurs = lire_csv(fichier_descripteur)

    image = cv2.imread(image_chemin)
    image = cv2.resize(image, (256, 256))

    if descripteur == "glcm":
        v_req = extraire_glcm(image)
    elif descripteur == "haralick":
        v_req = extraire_haralick(image)
    elif descripteur == "bit":
        v_req = extraire_bit(image)
    else:
        print("Descripteur inconnu")
        return []

    distances = []

    for i in range(len(vecteurs)):
        v_base = vecteurs[i]
        if distance == "euclidienne":
            d = distance_euclidienne(v_req, v_base)
        elif distance == "manhattan":
            d = distance_manhattan(v_req, v_base)
        elif distance == "tchebychev":
            d = distance_tchebychev(v_req, v_base)
        elif distance == "canberra":
            d = distance_canberra(v_req, v_base)
        else:
            print("Distance inconnue")
            return []

        distances.append((noms[i], d))

    distances = sorted(distances, key=lambda x: x[1])

    
    print(f"\nTop {top_n} images similaires à {image_chemin}:\n")
    for i in range(top_n):
        print(f"{i+1}. {distances[i][0]}  ---> Distance: {round(distances[i][1], 2)}")

    return distances[:top_n]  
