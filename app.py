import requests
r = requests.get('https://v2.jokeapi.dev/joke/programming?format=json')
if r.status_code == 200:
    fichier_json = r.json()
    if fichier_json["type"] == "single":
        print("Blague :", fichier_json["joke"])  # Clé "joke"
    elif fichier_json["type"] == "twopart":
        print("Blague :", fichier_json["setup"])
        print("Réponse :", fichier_json["delivery"])
else:
    print("Erreur lors de la requête à l'API. code de statut :", r.status_code)