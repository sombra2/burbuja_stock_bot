'''
En este script vamos a intentar crear un bot para el canal de Telegram que esté siempre escuchando a los requests
de los users y que devuelva las cotizaciones de Yahoo Finance a tiempo real
'''


import yfinance as yf
import requests
import urllib.parse # librería necesaria para codificar el mensaje a enviar
