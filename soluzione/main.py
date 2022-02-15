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

        rubrica[id] = nuovo_contatto
        print(f"Ho modificato {nome} {cognome} nella tua rubrica!")
    else:
        print("Id non valido!")


def termina():
    """Termina programma"""

    global continua
    print("Grazie per avere usato la mia rubrica!")
    continua = False

#############################################################################

comandi = [
    # Aggiungi qui i tuoi comandi
    aggiungi,
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
    except:
        print("Non è stato inserito un numero!\n\n")
        continue
