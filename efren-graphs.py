import pandas as pd

"""df = pd.read_csv('renal.csv', header=None) Para iterar solo con indices"""
df = pd.read_csv('renal.csv')

columns = ['age','bp','sg','al','su','rbc','pc','pcc','ba','bgr','bu','sc','sod','pot','hemo','pcv','wc','rc','htn','dm','cad','appet','pe','ane']

def name_frec(filename, name, ignore=[]):
    file = pd.read_csv(filename)
    frec = {}
    for i in range(1, file[name].size):
        if file[name][i] in ignore:
            continue
        if file[name][i] in frec:
            frec[file[name][i]] = frec[file[name][i]] + 1
        else:
            frec[file[name][i]] = 1
    return frec


def name_frec_check(filename, name, ignore=[]):
    file = pd.read_csv(filename)
    frec_c = {}
    frec_n = {}
    for i in range(1, file[name].size):
        if file['class'][i] == 'ckd':
            if file[name][i] in ignore:
                continue
            if file[name][i] in frec_c:
                frec_c[file[name][i]] = frec_c[file[name][i]] + 1
            else:
                frec_c[file[name][i]] = 1
        else:
            if file[name][i] in ignore:
                continue
            if file[name][i] in frec_n:
                frec_n[file[name][i]] = frec_n[file[name][i]] + 1
            else:
                frec_n[file[name][i]] = 1
    return frec_c, frec_n


"""print(name_frec('renal.csv', 'ba'))
print(name_frec('renal.csv', 'pcc'))
print(name_frec('renal.csv', 'su', ['?']))"""
for name in columns:
    print(name, name_frec_check('renal.csv', name, ['?']))