'''
En este script vamos a intentar crear un bot para el canal de Telegram que esté siempre escuchando a los requests
de los users y que devuelva las cotizaciones de Yahoo Finance a tiempo real
'''

import yfinance as yf
import requests
from telegram.ext import Updater
import os
from typing import Dict
import json
import urllib.parse  # librería necesaria para codificar el mensaje a enviar
import constants

version = '1.0'

# CUERPO DEL SCRIPT


'''Esta función es la encargada de mandar el mensaje al canal. Tanto el token del bot como el chatID corresponden
a un canal de pruebas. Solicita el acceso a @sombra2517 para hacer pruebas
'''
with open(os.path.join(constants.CREDENTIALS_FOLDER, constants.TELEGRAM_CREDENTIALS_FILE), 'r') as f:
    credentials: Dict[str, str] = json.load(f)


def telegram_bot_sendtext(bot_message):
    bot_token = credentials[constants.BOT_TOKEN]  # token para el bot de pruebas
    bot_chat_id = credentials[constants.TELEGRAM_CHAT_ID]  # chatID del canal de pruebas
    send_text = f'https://api.telegram.org/bot{bot_token}/sendMessage?chat_id={bot_chat_id}&parse_mode=markdown&text={bot_message}'
    response = requests.get(send_text)
    return response.json()


telegram_bot_sendtext("pruebas pruebas")
