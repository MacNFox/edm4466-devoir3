#coding utf-8
import requests, csv
from bs4 import BeautifulSoup
fichier = "procesverbaux.csv"


# Je désire recueillir tous les liens vers les documents PDF des procès verbaux de 2019
# disponibles sur le site de la municipalité de Saint-Léon-le-Grand.
entetes = {
    "User-Agent":"David Masse, etudiant journalisme UQAM, 438/ 837-9870"
}

url = "https://municipalite.saint-leon-le-grand.qc.ca/documents/proces-verbaux.html"
url2 = "https://municipalite.saint-leon-le-grand.qc.ca/"
contenu = requests.get(url, headers = entetes)
page = BeautifulSoup(contenu.text, "html.parser")

liste = []
# Verifier si tout fonctionne avec un seul lien
for pv in page.find("div", class_="contenu").find_next("p").find_all("a") :
        urlpv = pv.get("href")
        urltest = url2+str(urlpv)
        if "proces-verbaux" in url2:
            PV = url2
            PVfinal=PV.split(",")
            liste.append(PVfinal)

print(urltest)
# oui :-D
# je fais une boucle pour afficher tous générer tous mes liens 2019.
for urlpv1 in url2:
    print(url2+str(urlpv))

night=open(fichier, "a")
dark=csv.writer(night)
dark.writerow(liste)

# Pourtant, j'imprime tous les mêmes liens. Je n'arrive pas à faire changer la fin
# de mon lien pour qu'il change. De plus, rien ne s'écrit dans mon fichier CSV. 