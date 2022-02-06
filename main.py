# Setup: popola il dizionario "rubrica" con dei valori finti generati online

from ottieni_rubrica import ottieni_rubrica
rubrica = ottieni_rubrica()

#############################################################################
# Definisci qui i tuoi comandi

def termina():
    """Termina programma"""

    global continua
    print("Grazie per avere usato la mia rubrica!")
    continua = False

#############################################################################

comandi = [
    # Aggiungi qui i tuoi comandi
    
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
