# Hour of Code 2ed - Progetto 2

Progetto di corso #2 ideato per la classe 2021/22 del corso di introduzione alla programmazione "Hour of Code", seconda edizione.

---

## Consegna

L'obiettivo di questo progetto è quello di modificare il file `main.py` per configurare dei comandi per la gestione di una rubrica.

- Il file `ottieni_rubrica.py` utilizza una API online per generare 100 contatti random nella rubrica
- Ogni contatto della rubrica segue una struttura prestabilita:
```
{
    'nome': 'Mario',
    'cognome': 'Rossi',
    'email': 'mario.rossi@example.com',,
    'telefono': 
    {
        'casa': '74712054',
        'cellulare': '41309498'
    }
}
```
- Ogni contatto usa come chiave una stringa che rappresenta un numero intero incrementale (all'inizio da '0' a '99'). È necessario prevedere una gestione dell'incremento dell'id per l'inserimento di nuovi contatti.

Per l'inserimento dei comandi nel file `main.py`:
- nella sezione commentata alla riga 7 bisogna definire tramite `def` delle funzioni a *0 parametri*, che al limite utilizzino `input()` per richiedere all'utente le variabili necessarie per completare il comando.
- nella lista `comandi` presente alla riga 18 bisogna inserire - nell'ordine che si preferisce - i nomi delle suddette funzioni, separati tramite virgole.
- si consiglia di lasciare la funzione `termina` nella lista dei comandi, già definita, e usata per terminare il programma.

Infine, per testare il programma sarà sufficiente avviare il file `main.py`.

```
py -3 main.py
```

**N.B.** è richiesto di aver installato la libreria `requests` per poter svolgere l'esercizio:
```
py -3 -m pip install requests
```

**Update:** questa repository è stata aggiornata con la soluzione guidata mostrata a lezione, la si può trovare sotto la cartella `soluzione`.