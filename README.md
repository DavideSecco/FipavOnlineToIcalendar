# FipavOnlineToIcalendar
Generatore di file .ics per i calendari FIPAV regionali disponibili al sito: https://www.fipavonline.it/home.html

## Setup
E' indispensabile aver installato [python](https://www.python.org/downloads/). 

E' consigliato l'uso di [pip](https://pip.pypa.io/en/stable/installation/) per l'installazione dei moduli aggiuntivi.

Installazione moduli aggiuntivi:

MacOS/Linux:
```shell
python -m pip install -r requirements.txt
```

Windows:
```batch
py -m pip install -r requirements.txt
```

## Utilizzo
Salvare lo script `main.py` e il file `calendario_gare.xlsx` scaricato dal sito fipav nella stessa cartella.

Aprire la riga di comando e scrivere:
```
python main.py
```

Successivamente il programma chiederá se si vuole esportare il calendario solo di una squadra oppure quello completo. Digitare il nome della squadra se si vuole solo il calendario della squadra e premere invio, non scrivere nulla e premere invio se si vuole il calendario del campionato completo.

Il programma crea un file `.ics` nella stessa cartella che poi potrá essere importato su google calendar.


## License
The project is under MIT license and it's in no way affiliated with FIPAV