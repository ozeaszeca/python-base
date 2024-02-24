#!/usr/bin/env python
"""Imprime a tabuada do 1 ao 10.
---Tabuada do 1---

    1 x 1 = 1
    2 x 1 = 2
    3 x 1 = 3
...
##################
---Tabuda do 2---

    2 x 1 = 2
    2 x 2 = 4
...
##################

"""
__version__ = "0.1.1"
__author__ = "Ozeas"

#base = [1,2,3,4,5,6,7,8,9,10]
numeros = list(range(1,11))

# Iterable (percorriveis)

template = ""

#para cada numero em numeros:
for numero in numeros:
    template += "{:-^19}".format(f"Tabuada do {numero}") + '\n\n'
    
    for outro_numero in numeros:
        template += "{:^18}".format(f"{numero} x {outro_numero} = {numero * outro_numero}") + '\n'
        
    template += f'{19  * "#"} \n'


print(template)
