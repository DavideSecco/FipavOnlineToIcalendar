import pandas as pd
from icalendar import vCalAddress, vText, Calendar, Event
import pytz
import tempfile, os
from datetime import datetime


def main():
    data = pd.read_excel('calendario_gare.xlsx')
    campionato = data.columns[0]

    print("Il nome del file che contiene le partite si deve chhiamare 'calendario_gare.xlsx' e deve essere nella stessa cartella di questo script.")
    print("Possono essere esportati le partite: ")
    print("- di una singola squadra: scrivi ora il nome della squadra e premi invio")
    print("- di tutte le squadre: non scrivere nulla e premi invio")

    squadra = input()

    if squadra != "":
        data = data[data.values == squadra]
    else:
        data = data[data.notnull().all(axis=1)]
        squadra = "Completo"

    if len(data) == 0:
        print("Non sono state trovate gare, probabilmente è stato fatto un errore di battitura. Rilanciare il programma")
        return 0 

    print("Ho trovato " + str(len(data)) + " partite:")
    # print(data)

    cal = Calendar()
    cal.add('prodid', '-//My calendar product//mxm.dk//')
    cal.add('version', '2.0')

    for n in range(len(data.index)):
        result = [x for x in data.iloc[n]]

        event = Event()

        event.add('summary', str(result[6] + " - " + result[7]))
        event['location'] = (result[4] + " " + result[5])
        event.add('dtstart', datetime(int(result[2][-4:]),int(result[2][3:5]),int(result[2][0:2]),int(result[3]),int((result[3]%1)*100),0,tzinfo=pytz.timezone("Europe/Vienna")))
        event.add('dtend', datetime(int(result[2][-4:]),int(result[2][3:5]),int(result[2][0:2]),int(result[3])+2,int((result[3]%1)*100),0,tzinfo=pytz.timezone("Europe/Vienna")))

        cal.add_component(event)

    f = open(str(campionato) + ' - ' + str(squadra) + '.ics', 'wb')
    f.write(cal.to_ical())
    f.close()

    # print(cal.to_ical().decode("utf-8")) \
    print('File "' + str(campionato) + ' - ' + str(squadra) + '.ics"' + ' creato')

if __name__ == "__main__":
    main()