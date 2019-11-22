import pandas as pd

bp = []
dm = []
htn = []
clas = []
male = []
cmale = []
maleB = []
cmaleB = []
female = []
cfemale = []
femaleB = []
cfemaleB = []
ignore = ['?']
skip = ['age', 'sc', 'al', 'bp', 'dm', 'htn']
htnP = 0
htnF = 0
dmP = 0
dmF = 0
bpP = [0, 0, 0, 0]
bpF = [0, 0, 0, 0]
gfrHBP = [0, 0, 0, 0, 0]
gfrHBF = [0, 0, 0, 0, 0]
gfrHNP = [0, 0, 0, 0, 0]
gfrHNF = [0, 0, 0, 0, 0]
gfrMBP = [0, 0, 0, 0, 0]
gfrMBF = [0, 0, 0, 0, 0]
gfrMNP = [0, 0, 0, 0, 0]
gfrMNF = [0, 0, 0, 0, 0]


"""
sexo 0 = hombre, 1 = mujer
raza 0 = no afrodescendiente, 1 = afrodescendiente 
"""


def probabilidad(gfrV, sexo, raza, bpV, dmV, htnV):
    prob = 1.0
    if sexo == 0:
        if raza == 0:
            prob *= (1.0-gfrHBP[gfrV])
        else:
            prob *= (1.0 - gfrHNP[gfrV])
    else:
        if raza == 0:
            prob *= (1.0-gfrMBP[gfrV])
        else:
            prob *= (1.0 - gfrMNP[gfrV])
    print(prob)
    prob *= (1.0 - bpP[bpV])
    print(bpP[bpV], prob)
    if dmV == 1:
        prob *= (1.0 - 1.0)
    else:
        prob *= (1.0 - dmP)
    print(dmP, prob)
    if htnV == 1:
        prob *= (1.0 - 1.0)
    else:
        prob *= (1.0 - htnP)
    print(htnP, prob)
    return 1.0 - prob


def sum(lista):
    suma = 0
    for i in range(len(lista)):
        suma += lista[i]
    return suma


def porcentaje(frec, prob, val, res):
    for i in range(len(val)):
        frec[val[i]] += 1
        if res[i] == 1:
            prob[val[i]] += 1
    for i in range(len(prob)):
        prob[i] /= frec[i]


def revisar(gfr, lista, al):
    if gfr >= 60:
        if al < 30:
            lista.append(0)
        elif al < 300:
            lista.append(1)
        else:
            lista.append(2)
    elif gfr >= 45:
        if al < 30:
            lista.append(1)
        elif al < 300:
            lista.append(2)
        else:
            lista.append(3)
    elif gfr >= 30:
        if al < 30:
            lista.append(2)
        else:
            lista.append(3)
    elif gfr >= 15:
        if al < 300:
            lista.append(3)
        else:
            lista.append(4)
    else:
        lista.append(4)


def eGFR(sc, k, a, age, sex, race):
    return 141 * (min(sc/k, 1) ** a)\
           * (max(sc/k, 1) ** -1.209)\
           * (0.993**age) * sex * race


file = pd.read_csv('renal.csv')
for i in range(1, file['age'].size):
    _continue = False
    for sname in skip:
        if file[sname][i] in ignore:
            _continue = True
    if _continue:
        continue
    male.append(eGFR(float(file['sc'][i]), 0.9, -0.411, float(file['age'][i]), 1, 1))
    maleB.append(eGFR(float(file['sc'][i]), 0.9, -0.411, float(file['age'][i]), 1, 1.159))
    female.append(eGFR(float(file['sc'][i]), 0.7, -0.329, float(file['age'][i]), 1.018, 1))
    femaleB.append(eGFR(float(file['sc'][i]), 0.7, -0.329, float(file['age'][i]), 1.018, 1.159))
    revisar(male[-1], cmale, float(file['al'][i]))
    revisar(maleB[-1], cmaleB, float(file['al'][i]))
    revisar(female[-1], cfemale, float(file['al'][i]))
    revisar(femaleB[-1], cfemaleB, float(file['al'][i]))
    if float(file['bp'][i]) > 90:
        bp.append(3)
    elif float(file['bp'][i]) > 80:
        bp.append(2)
    elif float(file['bp'][i]) > 60:
        bp.append(1)
    else:
        bp.append(0)
    if file['dm'][i] == 'yes':
        dm.append(1)
    else:
        dm.append(0)
    if file['htn'][i] == 'yes':
        htn.append(1)
    else:
        htn.append(0)
    if file['class'][i] == 'ckd':
        clas.append(1)
    else:
        clas.append(0)
for i in range(len(htn)):
    if htn[i] == 0:
        htnF += 1
        if clas[i] == 1:
            htnP += 1
    if dm[i] == 0:
        dmF += 1
        if clas[i] == 1:
            dmP += 1
    bpF[bp[i]] += 1
    if clas[i] == 1:
        bpP[bp[i]] += 1
porcentaje(gfrHBF, gfrHBP, cmale, clas)
porcentaje(gfrHNF, gfrHNP, cmaleB, clas)
porcentaje(gfrMBF, gfrMBP, cfemale, clas)
porcentaje(gfrMNF, gfrMNP, cfemaleB, clas)
htnP /= htnF
dmP /= dmF
for i in range(len(bpP)):
    bpP[i] /= bpF[i]
"""
print("hombres no afrodescendientes")
for i in range(len(clas)):
    print(i, clas[i], probabilidad(cmale[i], 0, 0, bp[i], dm[i], htn[i]))
print("hombres afrodescendientes")
for i in range(len(clas)):
    print(i, clas[i], probabilidad(cmaleB[i], 0, 1, bp[i], dm[i], htn[i]))
print("mujeres no afrodescendientes")
for i in range(len(clas)):
    print(i, clas[i], probabilidad(cfemale[i], 1, 0, bp[i], dm[i], htn[i]))
print("mujeres afrodescendientes")
for i in range(len(clas)):
    print(i, clas[i], probabilidad(cfemaleB[i], 1, 1, bp[i], dm[i], htn[i]))
"""
print(gfrMBP, bpP, dmP, htnP)
print(probabilidad(0, 1, 0, 0, 0, 0))

"""
    Fuente https://www.kidney.org/content/ckd-epi-creatinine-equation-2009
    κ = 0.7 (females) or 0.9 (males)
    α = -0.329 (females) or -0.411 (males)
    sex = 1.018 (females) or 1 (males)
    sex = 1.159 (black) or 1 (no black)
"""

