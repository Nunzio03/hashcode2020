import statistics


class Libreria:

    def __init__(self, identificatore, giorni_massimi, num_books, giorni_per_registrarsi, books_per_day, catalogo_libri, lista_punteggi):

        # settings
        self.num_books = num_books
        self.giorni_per_registrarsi = giorni_per_registrarsi
        self.book_per_day = books_per_day
        self.catalogo_libri = catalogo_libri

        self.identificatore = identificatore
        self.giorni_massimi = giorni_massimi

        self.fitness = (self.giorni_massimi - self.giorni_per_registrarsi) * self.book_per_day * len(catalogo_libri) * statistics.mean(lista_punteggi)

        # process

        self.libri_mandati_privati = []
        self.day_counter = 0

    def singup(self, day):
        self.day_counter = self.giorni_per_registrarsi + day

        if self.giorni_massimi - self.day_counter > 0:
            return self.giorni_per_registrarsi
        else:
            return None

    def update(self, libri_scansionati_globali):
        iterator = 0
        libcounter = 0

        while self.day_counter < self.giorni_massimi and iterator < len(self.catalogo_libri):
            if not (self.catalogo_libri[iterator] in libri_scansionati_globali):
                libri_scansionati_globali.append(self.catalogo_libri[iterator])
                self.libri_mandati_privati.append(str(self.catalogo_libri[iterator]))
                libcounter += 1
            iterator += 1
            if libcounter > self.book_per_day:
                libcounter = 0
                self.day_counter += 1
        print("updating", self)

    def compute_fitness(self, libri_scansionati_globali):
        pass