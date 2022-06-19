from datetime import datetime

import pymysql
conn = pymysql.connect(host="localhost", user="Jelena", password="1234", database="foodtracker")

def lstKorisnika():
    cur = conn.cursor()
    cur.execute('select * from korisnik')
    lst = cur.fetchall()
    return lst

def lstHrane():
    cur = conn.cursor()
    cur.execute('select h.* from hrana')
    lst = cur.fetchall()
    return lst


def lstHranePoObroku(id_korisnika, obrok, datum):
    cur = conn.cursor()
    cur.execute('select * from hrana h, obrok_hrana o where h.id_hrane=o.id_hrane and o.id_korisnika = "%d" and obrok="%s" and datum="%s" ' % (int(id_korisnika), obrok, datum))
    lst = cur.fetchall()
    return lst

def lstObroka():
    cur = conn.cursor()
    cur.execute('select * from obrok_hrana')
    lst = cur.fetchall()
    return lst

def ukupnoUnesenoKalorija(datum, id_korisnika):
    cur = conn.cursor()
    cur.execute('select sum(kalorije) '
                'from obrok_hrana o, hrana h '
                'where h.id_hrane=o.id_hrane and datum = "%s" '
                'and id_korisnika = "%d" ' % (datum, int(id_korisnika)))
    unos = cur.fetchall()[0]
    return unos[0]

def ukupnoUnesenoProteina(datum, id_korisnika):
    cur = conn.cursor()
    cur.execute('select sum(proteini) '
                'from obrok_hrana o, hrana h '
                'where h.id_hrane=o.id_hrane and datum = "%s" '
                'and id_korisnika = "%d" ' % (datum, int(id_korisnika)))
    unos = cur.fetchall()[0]
    return unos[0]

def ukupnoUnesenoMasti(datum, id_korisnika):
    cur = conn.cursor()
    cur.execute('select sum(masti) '
                'from obrok_hrana o, hrana h '
                'where h.id_hrane=o.id_hrane and datum = "%s" '
                'and id_korisnika = "%d" ' % (datum, int(id_korisnika)))
    unos = cur.fetchall()[0]
    return unos[0]

def ukupnoUnesenoUgljenihHidrata(datum, id_korisnika):
    cur = conn.cursor()
    cur.execute('select sum(ugljeni_hidrati) '
                'from obrok_hrana o, hrana h '
                'where h.id_hrane=o.id_hrane and datum = "%s" '
                'and id_korisnika = "%d" ' % (datum, int(id_korisnika)))
    unos = cur.fetchall()[0]
    return unos[0]


def dodajKorisnika(kor_ime, loz, datum, visina, tezina, pol):
    cur = conn.cursor()
    upit = 'INSERT INTO korisnik(korisnicko_ime, lozinka, datum_rodjenja, visina, tezina, pol) ' \
          'VALUES ("%s", "%d", "%s", "%f", "%f", "%s")' % (kor_ime, int(loz), datum, float(visina), float(tezina), pol)
    cur.execute(upit)
    conn.commit()

def dodajHranu(naziv, kolicina, kalorije, proteini, ugljeni_hidrati, masti):
    cur = conn.cursor()
    upit = 'INSERT INTO hrana(naziv_hrane, kolicina, kalorije, proteini, ugljeni_hidrati, masti) ' \
          'VALUES ("%s", "%f", "%f", "%f", "%f", "%s")' % (naziv, float(kolicina), float(kalorije), float(proteini), float(ugljeni_hidrati), masti)
    cur.execute(upit)
    conn.commit()

def dodajObrok(id_korisnika, obrok, id_hrane, datum):
    cur = conn.cursor()
    upit = 'INSERT INTO obrok_hrana(id_korisnika, obrok, id_hrane, datum) ' \
          'VALUES ("%d", "%s", "%d", "%s")' % (int(id_korisnika), (obrok), int(id_hrane), (datum))
    cur.execute(upit)
    conn.commit()

def nadjiIdHrane():
    cur = conn.cursor()
    cur.execute('select max(id_hrane) from hrana')
    id = cur.fetchall()[0]
    return id[0]

def obrisiHranu(id_hrane):
    cur = conn.cursor()
    upit = 'DELETE FROM hrana WHERE id_hrane = "%d" ' % (int(id_hrane))
    cur.execute(upit)
    conn.commit()

def obrisiObrok(id_obroka):
    cur = conn.cursor()
    upit = 'DELETE FROM obrok_hrana WHERE id_obrok_hrana = "%d" ' % (int(id_obroka))
    cur.execute(upit)
    conn.commit()