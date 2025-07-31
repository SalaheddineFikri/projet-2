import streamlit as st
import cv2
from CBIR_Recherche import comparer


def login():
    st.title("Connexion")
    user = st.text_input("Nom d'utilisateur")
    mdp = st.text_input("Mot de passe", type="password")
    if user == "admin" and mdp == "1234":
        return True
    else:
        if user != "" or mdp != "":
            st.warning("Accès refusé")
        return False

if not login():
    st.stop()


st.title("Recherche d’Images par Contenu (CBIR)")
st.markdown("Projet IA2 - Étudiant: Ton Nom")

uploaded = st.file_uploader("Choisir une image", type=["jpg", "png", "jpeg"])
descripteur = st.selectbox("Choisir le descripteur", ["glcm", "haralick", "bit"])
distance = st.selectbox("Choisir la distance", ["euclidienne", "manhattan", "tchebychev", "canberra"])
top_n = st.slider("Nombre d'images similaires à afficher", 1, 10, 5)

if uploaded:
    with open("requete.jpg", "wb") as f:
        f.write(uploaded.read())

    img = cv2.imread("requete.jpg")
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    st.image(img, caption="Image requête", use_column_width=True)

    if st.button("Lancer la recherche"):
        st.write("Résultats :")
        resultats = comparer("requete.jpg", f"{descripteur}.csv", descripteur=descripteur, distance=distance, top_n=top_n)
        for i, (nom, d) in enumerate(resultats):
            st.write(f"{i+1}. {nom} — Distance : {round(d, 2)}")
