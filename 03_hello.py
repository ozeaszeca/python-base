#!/usr/bin/env python3
"""Hello World Multi Línguas.

Dependendo da lingua configurada no ambienteo programa exibe a mensagem correspondente.

Como usar:

verificar a linguagem do computador no terminal:
    ➜ env | grep LANG
    LANG=en_US.UTF-8
    LANGUAGE=en_US

Tenha a variável LANG devidamente configurada ex:
    export LANG=pt_BR

Execução:

    python3 03_hello.py
    ou
    ./03_hello.py


"""
__version__ = "0.0.1"
__author__ = "Ozeas Montenegro"
__license__ = "Unlicense"
# Dundet __

import os

current_language = os.getenv("LANG", "en_US")[:5]

#current_language = "en_US"
#current_language = "it_IT"
# snake case padrão comum do python

msg = "Hello, World!"

if current_language == "pt_BR":
    msg = "Olá, Mundo!"
elif current_language == "it_IT":
    msg = "Ciao, Mondo!"
elif current_language == "fr_FR":
     msg = "Bonjour Monde!"
elif current_language == "es_SP":
     msg = "Hola, Mundo!"

print(msg)

