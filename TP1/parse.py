def load_csv(filename):
    bd = []
    file = open(filename,'r')
    lines = file.readlines()
    lines = lines[1:]
    for line in lines:
        entry = {}
        campos = line.split(",")
        entry['_id'] = campos[0]
        entry['index'] = campos[1]
        entry['dataEMD'] = campos[2]
        entry['nome/primeiro'] = campos[3]
        entry['nome/último'] = campos[4]
        entry['idade'] = campos[5]
        entry['género'] = campos[6]
        entry['morada'] = campos[7]
        entry['modalidade'] = campos[8]
        entry['clube'] = campos[9]
        entry['email'] = campos[10]
        entry['federado'] = campos[11]
        entry['resultado'] = campos[12].replace('\n', '')
        bd.append(entry)
    return bd

def list_mod(bd):
    modalidades = []
    for entry in bd:
        mod = entry['modalidade']
        if mod not in modalidades:
            modalidades.append(mod)
    modalidades.sort()
    return modalidades

def check_apt(bd):
    entries = len(bd)
    t = 0
    f = 0
    for entry in bd:
        if entry['resultado'] == 'true':
            t+=1
        else:
            f+=1
    
    return "Aptos:" + str(t/entries * 100) + "%      " "Inaptos:" + str(f/entries *100) + "%"

def min_age(bd):
    min = int(bd[0]['idade'])
    
    for entry in bd:
        if int(entry['idade']) < min:
            min = int(entry['idade'])
    return min
            
def max_age(bd):
    max = int(bd[0]['idade'])
    
    for entry in bd:
        if int(entry['idade']) > max:
            max = int(entry['idade'])
    return max

def interval(menor):
    i = 0
    s = i+5
    
    while s <= menor:
        i+=5
        s+=5
    return i

def distr(bd):
    menor = min_age(bd)
    maior = max_age(bd)
    
    min_interval = interval(menor)
    max_interval = interval(maior)
    
    dict = {}
    
    while min_interval <= max_interval:
        dict[min_interval] = 0
        min_interval += 5
    
    for entry in bd:
        for key in dict:
            if int(entry['idade']) in range(key,key+5):
                dict[key] = dict[key] + 1
    return dict    

bd = load_csv("emd.csv")
lista_modalidades = list_mod(bd)
aptos_inaptos = check_apt(bd)
distr_etaria = (distr(bd))

print(lista_modalidades)
print(aptos_inaptos)
distrs = ""
for key in distr_etaria:
    distrs += f"[{key}-{key+4}]: {distr_etaria[key]}      "
print(distrs)