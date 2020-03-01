from collections import OrderedDict
from Libreria import Libreria

#f = open("input/f_libraries_of_the_world.txt", "r")
f = open("input/d_tough_choices.txt", "r")

# Config globale
(libri, totale_librerie , giorni_limite) = f.readline().replace('\n', '').split(' ')
id_libri_scansionati = list()

# Mappatura punteggio libri
punteggiLibri = f.readline().replace('\n', '').split(' ')
punteggioLibriMappa = {}

for id, punteggio in enumerate(punteggiLibri):
    punteggioLibriMappa[id] = int(punteggio)

#punteggioLibriMappa = {
#    25: 100,
#    30: 98,
#    31: 95,
#}

# Ordinamento descrescente
punteggioLibriMappaOrdinato = OrderedDict(reversed(sorted(punteggioLibriMappa.items(), key=lambda x: x[1])))

def getPunteggioByIndex(index):
    return list(punteggioLibriMappaOrdinato.values())[index]

def getPunteggioByID(id):
    return punteggioLibriMappaOrdinato.get(id)

#print(punteggioLibriMappaOrdinato)
#print(getPunteggioByIndex(0))

#print(getPunteggioByID(94192))

# Creamo oggetti libreria
librerie = []

for index, libreria in enumerate(f):
    (numeroLibri, giorni_signup, libri_al_giorno) = libreria.replace('\n', '').split(' ')
    # Creamo catalogo libri
    catalogo_libri = f.readline().replace('\n', '').split(' ')
    #print(catalogo_libri)
    catalogo_libri = list(map(int, catalogo_libri))

    # Ordiniamo il catalogo
    catalogo_libri_ordinato = list(k for k in punteggioLibriMappaOrdinato.keys() if k in catalogo_libri)
    lista_punteggi_libreria = list(punteggioLibriMappaOrdinato[k] for k in punteggioLibriMappaOrdinato.keys() if k in catalogo_libri)
    librerie.append(Libreria(int(index), int(giorni_limite), int(numeroLibri), int(giorni_signup), int(libri_al_giorno), catalogo_libri_ordinato, lista_punteggi_libreria))

# Main loop
simulation_days = 0
librerie_signuppate = {}

#ordino le librerie
librerie.sort(key=lambda x: x.fitness, reverse=True)



for libreria in librerie:
    if simulation_days > int(giorni_limite):
        break
    result = libreria.singup(simulation_days)
    if result is not None:
        simulation_days += result
        libreria.update(id_libri_scansionati)
        librerie_signuppate[libreria.identificatore] = libreria

print("writing output")

# OUTPUT
fOut = open("output/d.txt", "w+")
fOut.write(str(len(librerie_signuppate.items())) + "\n")
for libreria_signuppata in librerie_signuppate.values():
    if len(libreria_signuppata.libri_mandati_privati) > 0:
        print(libreria_signuppata)
        fOut.write(str(libreria_signuppata.identificatore) + " " + str(len(libreria_signuppata.libri_mandati_privati)) + "\n")
        fOut.write(' '.join(libreria_signuppata.libri_mandati_privati) + "\n")

fOut.close()

f.close()