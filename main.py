import datetime
import random
import flask
import requests
from flask import Flask, render_template, request, redirect, make_response, url_for, flash, session
import json
from projekat.Hrana import *
from projekat import database as db
from projekat.bmr import *
from datetime import date

app = Flask(__name__)

url = "https://api.spoonacular.com/food/ingredients/"

headers = {
    'Content-Type': "application/json",
    'x-api-key': "ceeec10f4c65493096ee32bc543ce858",
}

# prva stranica za prijavu
@app.route('/')
def index():
    return render_template('prijava.html', greska='')

# forma za prijavu
@app.route('/prijava', methods=['POST', 'GET'])
def prijava():
    if request.method == 'POST':
        korisnicko_ime = request.form['kor_ime']
        lozinka = request.form['loz']
        lst = db.lstKorisnika()
        for i in lst:
            if korisnicko_ime == i[1] and int(lozinka) == i[2]:
                resp = make_response(redirect(url_for('pocetna')))
                resp.set_cookie('id_korisnika', str(i[0]))
                return resp

        return render_template('prijava.html', greska='Greska prilikom unosa!')
    else:
        return render_template('prijava.html', greska='')

# pocetna stranica
@app.route('/pocetna', methods=['POST', 'GET'])
def pocetna():
    lst = db.lstKorisnika()
    bmr = 0
    kor_ime = ''
    id_korisnika = request.cookies.get('id_korisnika')
    for i in lst:
        if int(id_korisnika) == i[0]:
            kor_ime = i[1]
            pol = i[6]
            tezina = i[5]
            visina = i[4]
            datum1 = i[3]
            d = datetime.datetime.strptime(str(datum1), "%Y-%m-%d")
            god = d.year
            bmr = round(BMR(pol, tezina, visina, (date.today().year - god)), 2)

    trenutnoVreme = request.args.get('datum', default=date.today(), type=str)

    unosKal = db.ukupnoUnesenoKalorija(trenutnoVreme, id_korisnika)
    if unosKal == None: unosKal = 0
    unosKal = round(unosKal, 2)

    unosPr = db.ukupnoUnesenoProteina(trenutnoVreme, id_korisnika)
    if unosPr == None: unosPr = 0
    unosPr = round(unosPr, 2)
    ukPr = round(proteini(bmr), 2)

    unosUgHid = db.ukupnoUnesenoUgljenihHidrata(trenutnoVreme, id_korisnika)
    if unosUgHid == None: unosUgHid = 0
    unosUgHid = round(unosUgHid, 2)
    ukUgHid = round(ug_hid(bmr), 2)

    unosMas = db.ukupnoUnesenoMasti(trenutnoVreme, id_korisnika)
    if unosMas == None: unosMas = 0
    unosMas = round(unosMas, 2)
    ukMas = round(masti(bmr), 2)

    dijagram = [ukPr, ukUgHid, ukMas]
    dijagram2 = [unosPr, unosUgHid, unosMas]

    print(dijagram)
    print(dijagram2)

    lstHraneDorucak = db.lstHranePoObroku(id_korisnika, 'dorucak', trenutnoVreme)
    lstHraneRucak = db.lstHranePoObroku(id_korisnika, 'rucak', trenutnoVreme)
    lstHraneVecera = db.lstHranePoObroku(id_korisnika, 'vecera', trenutnoVreme)
    lstHraneUzina = db.lstHranePoObroku(id_korisnika, 'uzina', trenutnoVreme)
    return render_template('pocetna.html', kor_ime=kor_ime, bmr=bmr, unos=unosKal, trenutnoVreme=trenutnoVreme,
                           lstDor=lstHraneDorucak, lstRu=lstHraneRucak, lstVec=lstHraneVecera, lstUz=lstHraneUzina,
                           dijagram=dijagram, dijagram2=dijagram2)

# registracija
@app.route('/registracija', methods=['POST', 'GET'])
def registracija():
    if request.method == 'POST':
        return render_template('prvaPrijava.html', greska='')
    else:
        return render_template('prijava.html', greska='')

# dodavanje novog korisnika
@app.route('/prvaPrijava', methods=['POST', 'GET'])
def prvaPrijava():
    if request.method == 'POST':
        kor_ime = request.form['kor_ime']
        loz = request.form['loz']
        datum_rodjenja = request.form['datum_rodjenja']
        visina = request.form['visina']
        tezina = request.form['tezina']
        pol = request.form['pol']

        lst = db.lstKorisnika()
        for i in lst:
            if kor_ime == i[1]:
                return render_template('prvaPrijava.html', greska='Korisnicko ime zauzeto!')

        db.dodajKorisnika(kor_ime, loz, datum_rodjenja, visina, tezina, pol)

    return redirect(url_for('prijava'))

# unos hrane za pretragu
@app.route('/pretragaHrane', methods=['POST', 'GET'])
def pretragaHrane():
    if request.method == 'POST':
        p = request.form['pretrazi']
        obrok = request.form['obrok']
        datum = request.form['datum']

        return redirect(url_for('hrana', pretraga=p, obrok=obrok, datum=datum))
    else:
        obrok = request.form['obrok']
        datum = request.form['datum']
        return render_template('pretragaHrane.html', obrok=obrok, datum=datum)

@app.route('/dodajHranu', methods=['POST', 'GET'])
def dodajHranu():
    if request.method == 'POST':
        if request.form.get('obrok'):
            obrok = request.form['obrok']
            ob = ''
            if 'dorucak' in obrok: ob = 'dorucak'
            elif 'rucak' in obrok: ob = 'rucak'
            elif 'vecer' in obrok: ob = 'vecera'
            else: ob = 'uzina'
            datum = request.form['datum']
            return render_template('pretragaHrane.html', obrok=ob, datum=datum)
        elif request.form.get('obrisiDorucak'):
            s = request.form.get('obrisiDorucak')
            s = s.split(',')
            id_hrane = s[1]
            id_obrok_hrana = s[2]
            db.obrisiObrok(id_obrok_hrana)
            db.obrisiHranu(id_hrane)
            datum = request.form['datum']
            return redirect(url_for('pocetna', datum=datum))
        elif request.form.get('obrisiRucak'):
            s = request.form.get('obrisiRucak')
            s = s.split(',')
            id_hrane = s[1]
            id_obrok_hrana = s[2]
            db.obrisiObrok(id_obrok_hrana)
            db.obrisiHranu(id_hrane)
            datum = request.form['datum']
            return redirect(url_for('pocetna', datum=datum))
        elif request.form.get('obrisiVeceru'):
            s = request.form.get('obrisiVeceru')
            s = s.split(',')
            id_hrane = s[1]
            id_obrok_hrana = s[2]
            db.obrisiObrok(id_obrok_hrana)
            db.obrisiHranu(id_hrane)
            datum = request.form['datum']
            return redirect(url_for('pocetna', datum=datum))
        elif request.form.get('obrisiUzinu'):
            s = request.form.get('obrisiUzinu')
            s = s.split(',')
            id_hrane = s[1]
            id_obrok_hrana = s[2]
            db.obrisiObrok(id_obrok_hrana)
            db.obrisiHranu(id_hrane)
            datum = request.form['datum']
            return redirect(url_for('pocetna', datum=datum))
    else:
        obrok = request.form['obrok']
        ob = ''
        if 'dorucak' in obrok: ob = 'dorucak'
        elif 'rucak' in obrok: ob = 'rucak'
        elif 'vecer' in obrok: ob = 'vecera'
        else: ob = 'uzina'
        datum = request.form['datum']
        return render_template('pretragaHrane.html', obrok=ob, datum=datum)

# lista zadate hrane
@app.route('/hrana/<pretraga>/<obrok>/<datum>')
def hrana(pretraga, obrok, datum):
    s = requests.request("GET", url + 'search?query=' + pretraga,
                         headers=headers).json()
    lst = list()
    for i in s['results']:
        lst.append(i)
    return render_template('pretragaRezultati.html', lista=lst, obrok=obrok, datum=datum)

@app.route('/provera', methods=['POST', 'GET'])
def provera():
    if request.method == 'POST':
        print('post')
        obrok = request.form['obrok']
        datum = request.form['datum']
        s = request.form['detalji']
        s = s.split(',')
        id = s[1]
        kol = (request.form['kol'+str(s[2])])
        return redirect(url_for('podaci', id=id, kol=kol, obrok=obrok, datum=datum))
    else:
        return render_template('pretragaRezultati.html')

# trazi indeks izabrane hrane API
def nadjiIndeks(s, naziv):
    return next((index for (index, d) in enumerate(s['nutrition']['nutrients']) if d["name"] == naziv), None)

# dataljni podaci o izabranoj hrani
@app.route('/podaci/<id>/<kol>/<obrok>/<datum>')
def podaci(id, kol, obrok, datum):
    s = requests.request("GET", url + id + '/information?amount=' + kol + '&unit=grams',
                         headers=headers).json()
    kalorije = s['nutrition']['nutrients'][nadjiIndeks(s, "Calories")]['amount']
    proteini = s['nutrition']['nutrients'][nadjiIndeks(s, "Protein")]['amount']
    ugljeni_hidrati = s['nutrition']['nutrients'][nadjiIndeks(s, "Carbohydrates")]['amount']
    masti = s['nutrition']['nutrients'][nadjiIndeks(s, "Fat")]['amount']
    ob = ''
    if 'dorucak' in obrok: ob = 'dorucak'
    elif 'rucak' in obrok: ob = 'rucak'
    elif 'vecer' in obrok: ob = 'vecera'
    else: ob = 'uzina'
    h = Hrana(s['id'], s['name'], s['amount'], kalorije, proteini, ugljeni_hidrati, masti, ob)
    return render_template('detalji.html', obrok=h, datum=datum)

# dodavanje hrane i obroka
@app.route('/dodajObrok', methods=['POST', 'GET'])
def dodajObrok():
    id_korisnika = request.cookies.get('id_korisnika')
    if request.method == 'POST':
            naziv = (request.form['naziv'])
            kolicina = (request.form['kolicina'])
            kalorije = (request.form['kalorije'])
            proteini = (request.form['proteini'])
            ugljeni_hidrati = (request.form['ugljeni_hidrati'])
            masti = (request.form['masti'])
            obrok = (request.form['obrok'])
            datum = (request.form['datum'])
            db.dodajHranu(naziv, kolicina, kalorije, proteini, ugljeni_hidrati, masti)
            id_hrane = db.nadjiIdHrane()
            db.dodajObrok(id_korisnika, obrok, id_hrane, datum)
            return render_template('pretragaHrane.html', obrok=obrok, datum=datum)
    else:
        obrok = (request.form['obrok'])
        datum = (request.form['datum'])
        return render_template('pretragaHrane.html', obrok=obrok, datum=datum)

# kraj dodavanja za izabrani obrok u toku dana
@app.route('/zavrsi', methods=['POST', 'GET'])
def zavrsi():
    if request.method == 'POST':
        datum = (request.form['datum'])
        return redirect(url_for('pocetna', datum=[datum]))
    else:
        return render_template('pretragaRezultati.html')

# odjava
@app.route('/odjava', methods=['POST', 'GET'])
def odjava():
    if request.method == 'POST':
        resp = make_response(redirect('/'))
        resp.delete_cookie('id_korisnika')
        return resp
    else:
        return redirect(url_for('pocetna'))

if __name__ == '__main__':
    app.run()
