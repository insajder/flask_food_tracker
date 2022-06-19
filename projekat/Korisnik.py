class Korisnik:
    def __init__(self, id, kor_ime, loz, datum_rodjenja, visina, tezina, zadata_tezina):
        self.id = id
        self.kor_ime = kor_ime
        self.loz = loz
        self.datum_rodjenja = datum_rodjenja
        self.visina = visina
        self.tezina = tezina
        self.zadata_tezina = zadata_tezina

    def __str__(self):
        return self.id+', '+self.kor_ime