class Hrana:
    def __init__(self, id, naziv, kolicina, kalorije, proteini, ugljeni_hidrati, masti, obrok):
        self.id = id
        self.naziv = naziv
        self.kolicina = kolicina
        self.kalorije = kalorije
        self.proteini = proteini
        self.ugljeni_hidrati = ugljeni_hidrati
        self.masti = masti
        self.obrok = obrok

    def __str__(self):
        return 'ID: ' + str(self.id)+\
               ' NAZIV: ' + self.naziv+\
                ' KOLICINA: ' + str(self.kolicina)+\
                  ' KALORIJE: ' + str(self.kalorije)+\
                    ' PROTEINI: ' + str(self.proteini)+\
                    ' UGLJENI HIDRATI: ' + str(self.ugljeni_hidrati)+\
                    ' MASTI: ' + str(self.masti)+\
                    ' OBROK: ' + str(self.obrok)