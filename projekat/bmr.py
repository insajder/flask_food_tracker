
def BMR(pol, tezina, visina, godine):
    if pol == 'zensko':
        return ((10 * tezina) + (6.25 * visina) - (5 * godine) - 161)
    else:
        return ((10 * tezina) + (6.25 * visina) - (5 * godine) + 5)

def proteini(kal):
    Pk = (kal * 30) / 100
    Pg = Pk / 4
    return Pg

def masti(kal):
    Mk = (kal * 30) / 100
    Mg = Mk / 9
    return Mg

def ug_hid(kal):
    Uk = (kal * 55) / 100
    Ug = Uk / 4
    return Ug