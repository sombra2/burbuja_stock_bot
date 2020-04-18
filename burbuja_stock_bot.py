'''
En este script vamos a intentar crear un bot para el canal de Telegram que esté siempre escuchando a los requests
de los users y que devuelva las cotizaciones de Yahoo Finance a tiempo real
'''

import yfinance as yf
import requests
import os
import urllib.parse #librería necesaria para codificar el mensaje a enviar

cwd = os.path.dirname(os.path.realpath(__file__))
version = '1.0'


# CUERPO DEL SCRIPT








'''Esta función es la encargada de mandar el mensaje al canal. Tanto el token del bot como el chatID corresponden
a un canal de pruebas. Solicita el acceso a @sombra2517 para hacer pruebas
'''
with open(cwd + '/token_info.txt', 'r') as f:
  f = f.readlines()

def telegram_bot_sendtext(bot_message):
  bot_token = f[0].strip() # token para el bot de pruebas
  bot_chatID = f[1].strip() # chatID del canal de pruebas
  send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=markdown&text=' + bot_message
  response = requests.get(send_text)
  return response.json()

telegram_bot_sendtext('prueba desde pycharm')

