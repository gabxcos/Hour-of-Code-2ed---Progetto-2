# Setup: popola il dizionario "rubrica" con dei valori finti generati online

from ottieni_rubrica import ottieni_rubrica
rubrica = ottieni_rubrica()
prossimo_id = len(rubrica)

#############################################################################
# Definisci qui i tuoi comandi
def aggiungi():
    """Aggiungi contatto"""

    global rubrica, prossimo_id
    nome = input("Nome contatto: ")
    cognome = input("Cognome contatto: ")
    email = input("Email: ")
    num_casa = input("Telefono di casa: ")
    num_cell = input("Cellulare: ")
    nuovo_contatto = {
        "nome": nome,
        "cognome": cognome,
        "email": email,
        "telefono": {
            "casa": num_casa,
            "cellulare": num_cell
        }
    }

    rubrica[str(prossimo_id)] = nuovo_contatto
    prossimo_id += 1
    print(f"Ho aggiunto {nome} {cognome} alla tua rubrica!")


def modifica():
    """Modifica contatto"""

    global rubrica

    id = input("Quale utente vuoi cercare? (Inserisci id): ")
    if id in rubrica:

        contatto = rubrica[id]

        nome = input(f"Nome contatto ({contatto['nome']}): ")
        if nome=="":
            nome = contatto['nome']
        cognome = input(f"Cognome contatto ({contatto['cognome']}): ")
        if cognome=="":
            cognome = contatto['cognome']
        email = input(f"Email ({contatto['email']}): ")
        if email=="":
            email = contatto['email']
        num_casa = input(f"Telefono di casa ({contatto['telefono']['casa']}): ")
        if num_casa=="":
            num_casa = contatto['telefono']['casa']
        num_cell = input(f"Cellulare ({contatto['telefono']['cellulare']}): ")
        if num_cell=="":
            num_cell = contatto['telefono']['cellulare']

        nuovo_contatto = {
            "nome": nome,
            "cognome": cognome,
            "email": email,
            "telefono": {
                "casa": num_casa,
                "cellulare": num_cell
            }
        }

        rubrica[id] = nuovo_contatto
        print(f"Ho modificato {nome} {cognome} nella tua rubrica!")
    else:
        print("Id non valido!")


def ricerca():
    """Cerca contatto"""

    global rubrica

    stringa = input("Chi stai cercando? ").lower()
    lista = []
    for id, contatto in rubrica.items():
        if (stringa in contatto["nome"].lower()) or (stringa in contatto["cognome"].lower()) or (stringa in (contatto["nome"] +" "+ contatto["cognome"]).lower()):
            lista.append((id, contatto))

    if len(lista)>0:
        for id, contatto in lista:
            print(id, ":", contatto["nome"], contatto["cognome"])
    else:
        print("Non ho trovato nessun risultato!")



def termina():
    """Termina programma"""

    global continua
    print("Grazie per avere usato la mia rubrica!")
    continua = False

#############################################################################

comandi = [
    # Aggiungi qui i tuoi comandi
    ricerca,
    aggiungi,
    modifica,
    termina
]

continua = True

while continua:
    print("-"*20)
    print("GESTIONE RUBRICA - Comandi disponibili:\n")
    for indice, comando in enumerate(comandi):
        print(f"[{indice}]", "-", comando.__doc__)
    print("\n"+"-"*20)
    i = input("Quale comando vuoi usare? ")
    try:
        i = int(i)
        if i<0 or i>=len(comandi):
            print("Indice fuori range!\n\n")
            continue
        else:
            print("\n\n")
            comandi[i]()
    except Exception as e:
        print(e)
        continue
