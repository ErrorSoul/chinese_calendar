from tools import Date



elements = {0:"wood",
                1:"fire",
                2:"earth",
                3:"metal",
                4:"water"}
element_inverse =  {'earth': 2,
                    'fire': 1,
                    'metal': 3,
                    'water': 4,
                    'wood': 0}
earth_to_energy = {"rat": "yang water",
                       "ox" : "yin earth",
                       "tiger":"yang water",
                       "rabbit":"yin wood",
                       "dragon" : "yang earth",
                       "snake":"yin fire",
                       "horse":"yang fire",
                       "sheep":"yin earth",
                       "monkey":"yang metal",
                       "rooster":"yin metal",
                       "dog":"yang earth",
                       "pig":"yin water"}


def y(data):
    di = {}
    el =  data.convert_day()[0].split()[1]
    di["poderjka i vozmojnosti,resursi,obrazovanie"] = elements[(element_inverse[el] - 1)%5]
    di["vlast,obwestvennoe polojenie i slava"] =elements[(element_inverse[el] -2)%5]
    di["intellect,iskusstvo i virazitelnost"]=elements[(element_inverse[el] + 1)%5]
    di["bogatsvo,doxod,cenniyi veshi"] = elements[(element_inverse[el] +2)%5]
    di["druzia,kollegi,opponenti"] =elements[(element_inverse[el])%5]
    return di
def in_energy(data):
    a = [data.convert_year(),data.convert_month(),data.convert_day(),data.convert_hour()]
    f = []
    for c in a:
        f.append(c[0])
        f.append(earth_to_energy[c[1]])
        
    return f

def con(data):
    energy = in_energy(data)
    d = {}
    for c in energy:
        if c.split()[1] not in d:
            d[c.split()[1]] = 1
        else:
            d[c.split()[1]] +=1
    return d

def finish(data):
    conr = con(data)
    en = y(data)
    for key,u in en.items():
        en[key] =conr[en[key]]
    return en 
