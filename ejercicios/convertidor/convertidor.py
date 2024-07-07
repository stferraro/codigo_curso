import requests
from bs4 import BeautifulSoup
import re

def obtener_tasa_cambio():
    url = 'https://www.bcv.org.ve/'
    response = requests.get(url)
    if response.status_code != 200:
        raise Exception('No se pudo obtener la tasa de cambio.')
    soup = BeautifulSoup(response.text, 'html.parser')
    tasa_cambio = soup.find('div', id='dolar').text
    tasa_cambio_text = tasa_cambio.strip()
    match = re.search(r'\d+,\d+', tasa_cambio_text)
    tasa_dolar = float(match.group().replace(',', '.'))
    return tasa_dolar

def convertir_a_usd(bs):
    tasa = obtener_tasa_cambio()
    usd = bs / tasa
    if tasa == 0:
        raise ValueError('No se pudo obtener la tasa de cambio.')
    return usd

def convertir_a_bs(usd):
    tasa = obtener_tasa_cambio()
    bs = usd * tasa
    return bs

def escoger_opcion():
    print('1. Convertir Bs a USD')
    print('2. Convertir USD a Bs')
    opcion = int(input('Ingresa una opción (1 o 2): '))
    return opcion

opcion = escoger_opcion()
if opcion == 1:
    bs = float(input('Ingresa la cantidad en Bs: '))
    usd = convertir_a_usd(bs)
    print(f'{bs} Bs son {usd:.2f} USD')
elif opcion == 2:
    usd = float(input('Ingresa la cantidad en USD: '))
    bs = convertir_a_bs(usd)
    print(f'{usd} USD son {bs:.2f} Bs')
else:
    print('Opcion no valida. Por favor, selecciona una opción (1 o 2).')
