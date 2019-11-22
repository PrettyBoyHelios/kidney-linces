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


def in_ex(cP, gfrV, bpV, dmV, htnV):
    cant = 0
    if gfrV is not None:
        cant += 1
    if bpV is not None:
        cant += 1
    if dmV is not None:
        cant += 1
    if htnV is not None:
        cant += 1
    casos = 0
    casosDeseados = 0
    for i in range(len(bp)):
        match = 0
        if gfrV is not None:
            if cP[i] == gfrV:
                match += 1
        if bpV is not None:
            if bp[i] == bpV:
                match += 1
        if dmV is not None:
            if dm[i] == dmV:
                match += 1
        if htnV is not None:
            if htn[i] == htnV:
                match += 1
        if match == cant:
            casos += 1
            if clas[i] == 1:
                casosDeseados += 1
    return casosDeseados/casos


def probabilidad(cP, gfrP, gfrV, bpV, dmV, htnV):
    if bpP[bpV] == 1.0 or dmV == 1.0 or htnV == 1.0 or gfrP[gfrV] == 1.0:
        return 1.0
    prob = 0.0
    prob += gfrP[gfrV]
    prob += bpP[bpV]
    prob += dmP
    prob += htnP
    prob -= in_ex(cP, gfrV, bpV, None, None)
    prob -= in_ex(cP, gfrV, None, dmV, None)
    prob -= in_ex(cP, gfrV, None, None, htnV)
    prob -= in_ex(cP, None, bpV, dmV, None)
    prob -= in_ex(cP, None, bpV, None, htnV)
    prob -= in_ex(cP, None, None, dmV, htnV)
    prob += in_ex(cP, gfrV, bpV, dmV, None)
    prob += in_ex(cP, gfrV, bpV, None, htnV)
    prob += in_ex(cP, gfrV, None, dmV, htnV)
    prob += in_ex(cP, None, bpV, dmV, htnV)
    prob -= in_ex(cP, gfrV, bpV, dmV, htnV)
    return prob


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


file = pd.read_csv('datasets/renal.csv')
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

print("hombres no afrodescendientes")
casosDeseados = 0
for i in range(len(clas)):
    x = probabilidad(cmale, gfrHBP, clas[i], bp[i], dm[i], htn[i])
    if x > 0.8:
        if clas[i] == 1:
            casosDeseados += 1
    else:
        if clas[i] == 0:
            casosDeseados += 1
print(casosDeseados/len(clas))
print("hombres afrodescendientes")
casosDeseados = 0
for i in range(len(clas)):
    x = probabilidad(cmaleB, gfrHNP, clas[i], bp[i], dm[i], htn[i])
    if x > 0.8:
        if clas[i] == 1:
            casosDeseados += 1
    else:
        if clas[i] == 0:
            casosDeseados += 1
print(casosDeseados/len(clas))
print("mujeres no afrodescendientes")
casosDeseados = 0
for i in range(len(clas)):
    x = probabilidad(cfemale, gfrMBP, clas[i], bp[i], dm[i], htn[i])
    if x > 0.8:
        if clas[i] == 1:
            casosDeseados += 1
    else:
        if clas[i] == 0:
            casosDeseados += 1
print(casosDeseados/len(clas))
print("mujeres afrodescendientes")
casosDeseados = 0
for i in range(len(clas)):
    x = probabilidad(cfemaleB, gfrMNP, clas[i], bp[i], dm[i], htn[i])
    if x > 0.8:
        if clas[i] == 1:
            casosDeseados += 1
    else:
        if clas[i] == 0:
            casosDeseados += 1
print(casosDeseados/len(clas))

"""
    Fuente https://www.kidney.org/content/ckd-epi-creatinine-equation-2009
    κ = 0.7 (females) or 0.9 (males)
    α = -0.329 (females) or -0.411 (males)
    sex = 1.018 (females) or 1 (males)
    sex = 1.159 (black) or 1 (no black)
"""

