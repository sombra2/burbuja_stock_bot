'''
En este script vamos a intentar crear un bot para el canal de Telegram que esté siempre escuchando a los requests
de los users y que devuelva las cotizaciones de Yahoo Finance a tiempo real
'''


import yfinance as yf
import requests
import urllib.parse #librería necesaria para codificar el mensaje a enviar



# CUERPO DEL SCRIPT








'''Esta función es la encargada de mandar el mensaje al canal. Tanto el token del bot como el chatID corresponden
a un canal de pruebas. Solicita el acceso a @sombra2517 para hacer pruebas
'''
def telegram_bot_sendtext(bot_message):
  bot_token = '1134886701:AAEUvVcyb77iTz_VuTraVkC75oH83O82ik4' # token para el bot de pruebas
  bot_chatID = '-1001123997984' # chatID del canal de pruebas
  send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=markdown&text=' + bot_message
  response = requests.get(send_text)
  return response.json()

