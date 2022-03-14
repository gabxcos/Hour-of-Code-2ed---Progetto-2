import csv

rubrica = None

with open("./rubrica.csv", "r+") as rubrica_file:
    csv_reader = csv.DictReader(rubrica_file)
    rubrica = [row for row in csv_reader]

#############################################################################
# Definizione dei comandi
# N.B. ogni comando possiede un "docstring", una stringa compresa tra """tripli apici""",
# resa disponibile accedendo alla proprietà .__doc__ della funzione.

# Esempio: "aggiungi.__doc__" ci ritorna la documentazione della funzione "aggiungi"

#####
# Funzione AGGIUNGI, per creare un nuovo contatto
def aggiungi():
    """Aggiungi contatto"""

    global rubrica # la keyword "global" indica che useremo variabili dichiarate fuori dalla funzione
    
    # Per ogni campo del contatto, richiediamo l'informazione usando "input"
    nome = input("Nome contatto: ")
    cognome = input("Cognome contatto: ")
    email = input("Email: ")
    num_casa = input("Telefono di casa: ")
    num_cell = input("Cellulare: ")
    # Inseriamo i campi raccolti in un nuovo dizionario, con la struttura dei contatti
    nuovo_contatto = {
        "nome": nome,
        "cognome": cognome,
        "email": email,
        "telefono_casa": num_casa,
        "telefono_cellulare": num_cell
    }

    # Inseriamo il nuovo contatto in fondo alla rubrica
    rubrica.append(nuovo_contatto)

    print(f"Ho aggiunto {nome} {cognome} alla tua rubrica!")

#####
# Funzione MODIFICA, per modificare un contatto esistente
def modifica():
    """Modifica contatto"""

    global rubrica

    # Ipotesi: bisogna già sapere l'id dell'utente da modificare
    id = input("Quale utente vuoi cercare? (Inserisci id): ")

    if id.isdigit():
        id = int(id)
    else:
        print("Inserisci un id valido!")
        return

    # Controlliamo se l'id è nel range della lista della rubrica
    if id>=0 and id<len(rubrica):
        #... e in tal caso, salviamo in una variabile il contatto corrispondente a quell'id
        contatto = rubrica[id]

        # Ripetiamo lo stesso codice della funzione "AGGIUNGI", ma con una modifica:

        nome = input(f"Nome contatto ({contatto['nome']}): ")
        # Se anziché inserire un valore premiamo INVIO, ottenendo una stringa vuota,
        # intendiamo questa azione come voler "mantenere il campo per com'era già",
        # e in tal caso poniamo la stringa uguale a com'era nella variabile "contatto"
        if nome=="":    
            nome = contatto['nome']

        cognome = input(f"Cognome contatto ({contatto['cognome']}): ")
        if cognome=="":
            cognome = contatto['cognome']

        email = input(f"Email ({contatto['email']}): ")
        if email=="":
            email = contatto['email']

        num_casa = input(f"Telefono di casa ({contatto['telefono_casa']}): ")
        if num_casa=="":
            num_casa = contatto['telefono_casa']

        num_cell = input(f"Cellulare ({contatto['telefono_cellulare']}): ")
        if num_cell=="":
            num_cell = contatto['telefono_cellulare']

        nuovo_contatto = {
            "nome": nome,
            "cognome": cognome,
            "email": email,
            "telefono_casa": num_casa,
            "telefono_cellulare": num_cell
        }

        # In questo caso assegniamo il "nuovo_contatto" nella posizione dell'id scelto
        rubrica[id] = nuovo_contatto
        print(f"Ho modificato {nome} {cognome} nella tua rubrica!")
    else:
        # Se l'id non è presente nelle chiavi della rubrica...
        print("Id fuori range!")


#####
# Funzione RICERCA, per conoscere l'id di un contatto dato nome e/o cognome
def ricerca():
    """Cerca contatto"""

    global rubrica

    # La stringa può contenere il nome, il cognome o nome e cognome separati da uno spazio
    stringa = input("Chi stai cercando? ").lower()
    # N.B. perché ".lower()"? Perché conviene sempre porre tutte le stringhe da paragonare per somiglianza
    # in un unico "case": o tutto "uppercase" (maiuscolo) o tutto "lowercase" (minuscolo)

    lista = [] # Teniamo una lista vuota dove metteremo i "match" con la stringa inserita

    # enumerate(rubrica ) ritorna una LISTA di TUPLE di 2 elementi, nella forma [(id1, valore1), (id2, valore2), ...]
    for id, contatto in enumerate(rubrica):
        # Grazie ad Alberto Bella per il consiglio di "any"!
        # La funzione "any" è un "OR ad N-vie", ovvero ritorna True se una qualunque delle sue N condizioni è True
        if any([
            stringa in contatto["nome"].lower(),    # La stringa è nel nome 
            stringa in contatto["cognome"].lower(), # La stringa è nel cognome
            stringa in (contatto["nome"] +" "+ contatto["cognome"]).lower() # La stringa è in "nome cognome"
        ]):
            # Se uno qualunque dei controlli passa, inseriamo la coppia (chiave, valore) nella lista dei match
            lista.append((id, contatto))

    # Se la lista contiene dei match...
    if len(lista)>0:
        # Nuovamente, per ogni coppia (chiave, valore) nella lista dei match, con id=chiave e contatto=valore
        for id, contatto in lista:
            # Stampiamo l'id, che ci servirà per modificare o eliminare il contatto, assieme ad alcune sue info
            print(id, ":", contatto["nome"], contatto["cognome"])
    else:
        # Altrimenti, non ho trovato contatti!
        print("Non ho trovato nessun risultato!")


#####
# Funzione ELIMINA, per eliminare un contatto dalla rubrica
def elimina():
    """Elimina contatto"""

    global rubrica

    # Ipotesi: bisogna già sapere l'id dell'utente da eliminare
    id = input("Quale utente vuoi eliminare? (Inserisci id): ")

    if id.isdigit():
        id = int(id)
    else:
        print("Inserisci un id valido!")
        return

    # Controlliamo se l'id è nel range della lista della rubrica
    if id>=0 and id<len(rubrica):
        #... e in tal caso, salviamo in una variabile il contatto corrispondente a quell'id
        contatto = rubrica[id]

        print(f'Elimino {contatto["nome"]} {contatto["cognome"]}...')

        del rubrica[id]

    else:
        # Se l'id non è presente nel range...
        print("Id fuori range!")


#####
# Funzione TERMINA, chiude il programma
def termina():
    """Termina programma"""

    global continua # Da questa variabile dipende il loop principale del programma
    print("Grazie per avere usato la mia rubrica!")

    with open("./rubrica.csv", "w") as rubrica_file:
        csv_writer = csv.DictWriter(rubrica_file, ['nome', 'cognome', 'email', 'telefono_casa', 'telefono_cellulare'])
        csv_writer.writeheader()
        csv_writer.writerows(rubrica)

    continua = False    # Settando "continua" a False interrompiamo il loop del programma

#############################################################################

# Lista di tutti i comandi utilizzabili del programma
comandi = [
    # Aggiungi qui i tuoi comandi
    ricerca,
    aggiungi,
    modifica,
    elimina,
    termina
]

continua = True # Fintanto che è True, il programma continuerà a chiederci nuove operazioni sulla rubrica

while continua:
    print("-"*20)
    print("GESTIONE RUBRICA - Comandi disponibili:\n")

    # La funzione "enumerate" trasforma ogni elemento "comando" in una coppia (indice, comando), dove
    # "indice" rappresenta l'indice numerico di quel comando nell'array (da 0 a len(comandi)-1)
    for indice, comando in enumerate(comandi):
        print(f"[{indice}]", "-", comando.__doc__) # Per ogni comando stampiamo la guida, nella forma: [0] - Nome comando
    print("\n"+"-"*20)


    i = input("Quale comando vuoi usare? ") # Chiediamo il numero corrispondente al comando da eseguire
    try:
        i = int(i)  # Proviamo a convertire la stringa "i" nel numero intero corrispondente
    except:
        # Se otteniamo un errore, vuol dire che l'utente non ha immesso una stringa convertibile ad intero
        print("Non è stato inserito un numero!\n\n")
        continue # Ricominciamo il loop

    if i<0 or i>=len(comandi): # Possiamo accettare solo numeri da 0 a len(comandi)-1
        print("Indice fuori range!\n\n")
        continue    # Ricominciamo il loop
    
    else:
        # Se arriviamo qui, eseguiamo il comando di indice i
        print("\n\n")
        comandi[i]() # equivalente di "nome_comando_i_esimo()"