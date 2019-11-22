import pandas as pd


def revisar(gfr, lista, al):
    if gfr >= 60 :
        if al < 30:
            lista.append(1)
        elif al < 300:
            lista.append(2)
        else:
            lista.append(3)
    elif gfr >= 45:
        if al < 30:
            lista.append(2)
        elif al < 300:
            lista.append(3)
        else:
            lista.append(4)
    elif gfr >= 30:
        if al < 30:
            lista.append(3)
        else:
            lista.append(4)
    elif gfr >= 15:
        if al < 300:
            lista.append(4)
        else:
            lista.append(5)
    else:
        lista.append(5)


def eGFR(sc, k, a, age, sex, race):
    return 141 * (min(sc/k, 1) ** a)\
           * (max(sc/k, 1) ** -1.209)\
           * (0.993**age) * sex * race


male = []
cmale = []
maleB = []
cmaleB = []
female = []
cfemale = []
femaleB = []
cfemaleB = []
ignore = ['?']
file = pd.read_csv('renal.csv')
for i in range(1, file['age'].size):
    if file['age'][i] in ignore:
        continue
    if file['sc'][i] in ignore or file['al'][i] in ignore:
        male.append(-1)
        cmale.append(-1)
        maleB.append(-1)
        cmaleB.append(-1)
        female.append(-1)
        cfemale.append(-1)
        femaleB.append(-1)
        cfemaleB.append(-1)
        continue
    male.append(eGFR(float(file['sc'][i]), 0.9, -0.411, float(file['age'][i]), 1, 1))
    maleB.append(eGFR(float(file['sc'][i]), 0.9, -0.411, float(file['age'][i]), 1, 1.159))
    female.append(eGFR(float(file['sc'][i]), 0.7, -0.329, float(file['age'][i]), 1.018, 1))
    femaleB.append(eGFR(float(file['sc'][i]), 0.7, -0.329, float(file['age'][i]), 1.018, 1.159))
    revisar(male[-1], cmale, float(file['al'][i]))
    revisar(maleB[-1], cmaleB, float(file['al'][i]))
    revisar(female[-1], cfemale, float(file['al'][i]))
    revisar(femaleB[-1], cfemaleB, float(file['al'][i]))
print(cmale)

"""
    Fuente https://www.kidney.org/content/ckd-epi-creatinine-equation-2009
    κ = 0.7 (females) or 0.9 (males)
    α = -0.329 (females) or -0.411 (males)
    sex = 1.018 (females) or 1 (males)
    sex = 1.159 (black) or 1 (no black)
"""

