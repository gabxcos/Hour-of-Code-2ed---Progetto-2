import requests #py -3 -m pip install requests

def ottieni_rubrica():
    url = "https://randomuser.me/api/?results=100"  # questa API usa un parametro ?results=N per generare N contatti random in un JSON
    req = requests.get(url) # effettuiamo la chiamata all'API
    if req.status_code != 200:  # status 200 indica una richiesta HTTP con risposta con successo
        return {}   # se non è 200, ritorniamo un dizionario vuoto
    else:
        # se è 200, richiamando il metodo .json sull'oggetto richiesta, otteniamo il dizionario corrispondente
        diz = req.json()
        # Modifichiamo il dizionario per ottenere una rubrica:
        # - con "enumerate(diz"results"), otteniamo una lista del tipo [(0, contatto0), (1, contatto1), ...]
        # - assegniamo i due valori di ogni coppia a due variabili di iterazione "chiave, valore"
        # - modelliamo ogni campo di "valore" per creare una nuova struttura, più semplice
        rubrica_diz = {
            str(chiave) : # Usiamo come chiave l'indice numerico del contatto enumerato, trasformato in stringa
            {
                "nome": valore["name"]["first"], 
                "cognome": valore["name"]["last"],
                "email": valore["email"],
                "telefono": {
                    "casa": valore["phone"],
                    "cellulare": valore["cell"]
                }
        } for chiave, valore in enumerate(diz["results"])}
        # Ritorniamo la rubrica con la nostra struttura
        return rubrica_diz