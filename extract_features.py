import cv2
import mahotas
import numpy as np
import os
import csv
from skimage.feature import graycomatrix, graycoprops

def extraire_glcm(img):
    r = []
    for i in range(3):
        ch = cv2.normalize(img[:, :, i], None, 0, 255, cv2.NORM_MINMAX).astype('uint8')
        g = graycomatrix(ch, distances=[1], angles=[0], levels=256, symmetric=True, normed=True)
        r.extend([
            graycoprops(g, 'contrast')[0, 0],
            graycoprops(g, 'homogeneity')[0, 0],
            graycoprops(g, 'energy')[0, 0],
            graycoprops(g, 'correlation')[0, 0]
        ])
    return r

def extraire_haralick(img):
    r = []
    for i in range(3):
        ch = img[:, :, i]
        h = mahotas.features.haralick(ch)
        for j in range(h.shape[1]):
            r.append(sum(h[:, j]) / h.shape[0])
    return r

def extraire_bit(img):
    r = []
    for i in range(3):
        ch = img[:, :, i]
        r.extend(mahotas.features.lbp(ch, radius=2, points=8))
    return r

def enregistrer_csv(fichier, donnees, noms):
    with open(fichier, 'w', newline='') as f:
        w = csv.writer(f)
        for i in range(len(donnees)):
            w.writerow([noms[i]] + donnees[i])

def traitement_dossier(dossier):
    g, h, b, noms = [], [], [], []
    for nom in os.listdir(dossier):
        if nom.lower().endswith(('.jpg', '.jpeg', '.png')):
            img = cv2.resize(cv2.imread(os.path.join(dossier, nom)), (256, 256))
            g.append(extraire_glcm(img))
            h.append(extraire_haralick(img))
            b.append(extraire_bit(img))
            noms.append(nom)
    enregistrer_csv("glcm.csv", g, noms)
    enregistrer_csv("haralick.csv", h, noms)
    enregistrer_csv("bit.csv", b, noms)

traitement_dossier("dataset/images")
