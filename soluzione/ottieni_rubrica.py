import requests #py -3 -m pip install requests

def ottieni_rubrica():
    url = "https://randomuser.me/api/?results=100"
    req = requests.get(url)
    if req.status_code != 200:
        return {}
    else:
        diz = req.json()
        rubrica_diz = {
            str(chiave) : 
            {
                "nome": valore["name"]["first"], 
                "cognome": valore["name"]["last"],
                "email": valore["email"],
                "telefono": {
                    "casa": valore["phone"],
                    "cellulare": valore["cell"]
                }
        } for chiave, valore in enumerate(diz["results"])}
        return rubrica_diz
