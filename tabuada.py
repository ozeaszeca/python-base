#!/usr/bin/env python
"""Imprime a tabuada do 1 ao 10.
Tabuada do 1
1
2
3
...
--------------
Tabuda do 2
2
4
...
-------------

"""
__version__ = "0.1.0"
__author__ = "Ozeas"

#base = [1,2,3,4,5,6,7,8,9,10]
numeros = list(range(1,11))

# Iterable (percorriveis)

#para cada numero em numeros:
for numero in numeros:
    print(f"Tabuada do :{numero}")
    for outro_numero in numeros:
        print(f'{numero} x {outro_numero} = ',numero * outro_numero)
    print('-----------------')





