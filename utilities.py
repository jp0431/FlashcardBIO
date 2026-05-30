import streamlit as st
import random
import os
def inicializa_dict():
    return {
        "0":  {'ruta': 'IMG/Agaricus sp..jpeg',           'nombre': 'Agaricus sp', "GRUP": "FONGS"},
        "1":  {'ruta': 'IMG/Amanita sp.jpeg',             'nombre': 'Amanita sp', "GRUP": "FONGS"},
        "2":  {'ruta': 'IMG/Aspergillus sp..jpeg',        'nombre': 'Aspergillus sp', "GRUP": "FONGS"},
        "3":  {'ruta': 'IMG/Aspergillus sp.jpeg',         'nombre': 'Aspergillus sp', "GRUP": "FONGS"},
        "4":  {'ruta': 'IMG/Astraeus hygrometricus.jpeg', 'nombre': 'Astraeus hygrometricus', "GRUP": "FONGS"},
        "5":  {'ruta': 'IMG/Cantharellus sp..jpeg',       'nombre': 'Cantharellus sp', "GRUP": "FONGS"},
        "6":  {'ruta': 'IMG/Cyathus sp.jpeg',             'nombre': 'Cyathus sp', "GRUP": "FONGS"},
        "7":  {'ruta': 'IMG/Ganoderma lucidum.jpeg',      'nombre': 'Ganoderma lucidum', "GRUP": "FONGS"},
        "8":  {'ruta': 'IMG/Helvella sp..jpeg',           'nombre': 'Helvella sp', "GRUP": "FONGS"},
        "9":  {'ruta': 'IMG/Hypoxylon fragiforme.jpeg',   'nombre': 'Hypoxylon fragiforme', "GRUP": "FONGS"},
        "10": {'ruta': 'IMG/Lactarius deliciosus.jpeg',   'nombre': 'Lactarius deliciosus', "GRUP": "FONGS"},
        "11": {'ruta': 'IMG/Lactarius sp.jpeg',           'nombre': 'Lactarius sp', "GRUP": "FONGS"},
        "12": {'ruta': 'IMG/Lycoperdon sp..jpeg',         'nombre': 'Lycoperdon sp', "GRUP": "FONGS"},
        "13": {'ruta': 'IMG/Morchella sp..jpeg',          'nombre': 'Morchella sp', "GRUP": "FONGS"},
        "14": {'ruta': 'IMG/Penicillium sp..jpeg',        'nombre': 'Penicillium sp', "GRUP": "FONGS"},
        "15": {'ruta': 'IMG/Penicillium sp.jpeg',         'nombre': 'Penicillium sp', "GRUP": "FONGS"},
        "16": {'ruta': 'IMG/Peziza sp..jpeg',             'nombre': 'Peziza sp', "GRUP": "FONGS"},
        "17": {'ruta': 'IMG/Phragmidium violaceum 1.jpeg','nombre': 'Phragmidium violaceum', "GRUP": "FONGS"},
        "18": {'ruta': 'IMG/Phragmidium violaceum.jpeg',  'nombre': 'Phragmidium violaceum', "GRUP": "FONGS"},
        "19": {'ruta': 'IMG/Phyllactinia sp.jpeg',        'nombre': 'Phyllactinia sp', "GRUP": "FONGS"},
        "20": {'ruta': 'IMG/Plasmopara viticola 1.jpeg',  'nombre': 'Plasmopara viticola', "GRUP": "FONGS"},
        "21": {'ruta': 'IMG/Plasmopara viticola.jpeg',    'nombre': 'Plasmopara viticola', "GRUP": "FONGS"},
        "22": {'ruta': 'IMG/Pleurotus sp.jpeg',           'nombre': 'Pleurotus sp', "GRUP": "FONGS"},
        "23": {'ruta': 'IMG/Puccinia sp.jpeg',            'nombre': 'Puccinia sp', "GRUP": "FONGS"},
        "24": {'ruta': 'IMG/Ramaria sp.jpeg',             'nombre': 'Ramaria sp', "GRUP": "FONGS"},
        "25": {'ruta': 'IMG/Rhizopus sp 1.jpeg',          'nombre': 'Rhizopus sp', "GRUP": "FONGS"},
        "26": {'ruta': 'IMG/Rhizopus sp.jpeg',            'nombre': 'Rhizopus sp', "GRUP": "FONGS"},
        "27": {'ruta': 'IMG/Stereum hirsutum.jpeg',       'nombre': 'Stereum hirsutum', "GRUP": "FONGS"},
        "28": {'ruta': 'IMG/Trametes versicolor.jpeg',    'nombre': 'Trametes versicolor', "GRUP": "FONGS"},
        "29": {'ruta': 'IMG/Xylaria sp.jpeg',             'nombre': 'Xylaria sp', "GRUP": "FONGS"},
        "30":  {'ruta': 'IMG/Acacia sp..jpeg',               'nombre': 'Acacia sp',           'GRUP': ''},
        "31":  {'ruta': 'IMG/Acer campestre.jpeg',            'nombre': 'Acer campestre',        'GRUP': ''},
        "32":  {'ruta': 'IMG/Acer monspessulanum.jpeg',       'nombre': 'Acer monspessulanum',   'GRUP': ''},
        "33":  {'ruta': 'IMG/Acer opalus.jpeg',               'nombre': 'Acer opalus',           'GRUP': ''},
        "34":  {'ruta': 'IMG/Asplenium trichomanes.jpeg',     'nombre': 'Asplenium trichomanes', 'GRUP': ''},
        "35":  {'ruta': 'IMG/Bupleurum fruticosum.jpeg',      'nombre': 'Bupleurum fruticosum',  'GRUP': ''},
        "36":  {'ruta': 'IMG/Ceranium sp.jpeg',               'nombre': 'Ceranium sp',           'GRUP': ''},
        "37":  {'ruta': 'IMG/Cladonia pyxidata.jpeg',         'nombre': 'Cladonia pyxidata',     'GRUP': ''},
        "38":  {'ruta': 'IMG/Cladonia rangiformis.jpeg',      'nombre': 'Cladonia rangiformis',  'GRUP': ''},
        "39":  {'ruta': 'IMG/Cladophora sp.jpeg',             'nombre': 'Cladophora sp',         'GRUP': ''},
        "40":  {'ruta': 'IMG/Codium sp.jpeg',                 'nombre': 'Codium sp',             'GRUP': ''},
        "41":  {'ruta': 'IMG/Collema sp.jpeg',                'nombre': 'Collema sp',            'GRUP': ''},
        "42":  {'ruta': 'IMG/Conocephalum conicum.jpeg',      'nombre': 'Conocephalum conicum',  'GRUP': ''},
        "43":  {'ruta': 'IMG/Corallina sp.jpeg',              'nombre': 'Corallina sp',          'GRUP': ''},
        "44":  {'ruta': 'IMG/Diatomees.jpeg',                 'nombre': 'Diatomees',             'GRUP': ''},
        "45":  {'ruta': 'IMG/Dictyota dichotoma.jpeg',        'nombre': 'Dictyota dichotoma',    'GRUP': ''},
        "46":  {'ruta': 'IMG/Enteromorpha sp.jpeg',           'nombre': 'Enteromorpha sp',       'GRUP': ''},
        "47":  {'ruta': 'IMG/Euglena sp.jpeg',                'nombre': 'Euglena sp',            'GRUP': ''},
        "48":  {'ruta': 'IMG/Frullania dilatata.jpeg',        'nombre': 'Frullania dilatata',    'GRUP': ''},
        "49":  {'ruta': 'IMG/Frullania dilatata1.jpeg',       'nombre': 'Frullania dilatata1',   'GRUP': ''},
        "50":  {'ruta': 'IMG/Jania rubens.jpeg',              'nombre': 'Jania rubens',          'GRUP': ''},
        "51":  {'ruta': 'IMG/Lophocolea bidentata.jpeg',      'nombre': 'Lophocolea bidentata',  'GRUP': ''},
        "52":  {'ruta': 'IMG/Nerium oleander.jpeg',           'nombre': 'Nerium oleander',       'GRUP': ''},
        "53":  {'ruta': 'IMG/Nostoc sp 1.jpeg',               'nombre': 'Nostoc sp',           'GRUP': ''},
        "54":  {'ruta': 'IMG/Nostoc sp.jpeg',                 'nombre': 'Nostoc sp',             'GRUP': ''},
        "55":  {'ruta': 'IMG/Oscillatoria sp.jpeg',           'nombre': 'Oscillatoria sp',       'GRUP': ''},
        "56":  {'ruta': 'IMG/Parmelia sp.jpeg',               'nombre': 'Parmelia sp',           'GRUP': ''},
        "57":  {'ruta': 'IMG/Pediastrum sp.jpeg',             'nombre': 'Pediastrum sp',         'GRUP': ''},
        "58":  {'ruta': 'IMG/Peridinium sp.jpeg',             'nombre': 'Peridinium sp',         'GRUP': ''},
        "59":  {'ruta': 'IMG/Pertusaria amara.jpeg',          'nombre': 'Pertusaria amara',      'GRUP': ''},
        "60":  {'ruta': 'IMG/Pseudevernia furfuracea.jpeg',   'nombre': 'Pseudevernia furfuracea','GRUP': ''},
        "61":  {'ruta': 'IMG/Quercus coccifera.jpeg',         'nombre': 'Quercus coccifera',     'GRUP': ''},
        "62":  {'ruta': 'IMG/Quercus ilex.jpeg',              'nombre': 'Quercus ilex',          'GRUP': ''},
        "63":  {'ruta': 'IMG/Quercus suber.jpeg',             'nombre': 'Quercus suber',         'GRUP': ''},
        "64":  {'ruta': 'IMG/Rhamnus alaternus 1.jpeg',       'nombre': 'Rhamnus alaternus',   'GRUP': ''},
        "65":  {'ruta': 'IMG/Rhamnus alaternus.jpeg',         'nombre': 'Rhamnus alaternus',     'GRUP': ''},
        "66":  {'ruta': 'IMG/Rhamnus lycioides.jpeg',         'nombre': 'Rhamnus lycioides',     'GRUP': ''},
        "67":  {'ruta': 'IMG/Rhizocarpon geographicum.jpeg',  'nombre': 'Rhizocarpon geographicum','GRUP': ''},
        "68":  {'ruta': 'IMG/Rubia peregrina.jpeg',           'nombre': 'Rubia peregrina',       'GRUP': ''},
        "69":  {'ruta': 'IMG/Sambucus nigra.jpeg',            'nombre': 'Sambucus nigra',        'GRUP': ''},
        "70":  {'ruta': 'IMG/Sambucus nigra1.jpeg',           'nombre': 'Sambucus nigra',       'GRUP': ''},
        "71":  {'ruta': 'IMG/Scenedesmus sp.jpeg',            'nombre': 'Scenedesmus sp',        'GRUP': ''},
        "72":  {'ruta': 'IMG/Spyrogira sp.jpeg',              'nombre': 'Spyrogira sp',          'GRUP': ''},
        "73":  {'ruta': 'IMG/Trifolium sp.jpeg',              'nombre': 'Trifolium sp',          'GRUP': ''},
        "74":  {'ruta': 'IMG/Usnea sp.jpeg',                  'nombre': 'Usnea sp',              'GRUP': ''},
        "75":  {'ruta': 'IMG/Xanthoria parietina.jpeg',       'nombre': 'Xanthoria parietina',   'GRUP': ''},
        "76": {'ruta': 'IMG/Cupressus sempervirens.jpeg', 'nombre': 'Cupressus sempervirens', 'GRUP': ''},
        "77": {'ruta': 'IMG/Robinia pseudoacacia.jpeg',   'nombre': 'Robinia pseudoacacia',   'GRUP': ''},

    }
def nova_imatge(dict_,):
    """Escull una imatge nova que no s'hagi vist."""
    disponibles = [i for i in range(len(dict_)) if i not in st.session_state.img_vist]
    if not disponibles:
        st.session_state.img_vist = []
        disponibles = list(range(len(dict_)))
    nou_idx = random.choice(disponibles)
    if len(st.session_state.img_vist) < len(dict_):
        st.session_state.img_vist.append(nou_idx)
        st.session_state.img_idx = nou_idx
        st.session_state.fase = "pregunta"
    else:
        st.session_state.fase = "acabat"
        
def printimg():
    for i, img in  enumerate(os.listdir("IMG/")):
        print(f"Imatge {i}: {img}")
printimg()