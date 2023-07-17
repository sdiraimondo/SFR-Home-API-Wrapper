#!python
import os
import time
from urllib import request
from http.cookiejar import CookieJar
from urllib.parse import urlencode
from urllib.error import HTTPError
from time import time
from homesfr import *

app = Flask(__name__)

# Login
USERNAME = %USER%
PASSWORD = %PASSWORD%
MySystem=HomeSFR(USERNAME, PASSWORD, None, False, True)
MySystem.login()

# Modes utilisables
MODE_OFF = 0
MODE_CUSTOM = 1
MODE_ON = 2

# Types de capteurs
PRESENCE_DETECTOR = 'PIR_DETECTOR'			# https://boutique.home.sfr.fr/detecteur-de-mouvement
MAGNETIC_OPENNING_DETECTOR = 'MAGNETIC'			# https://boutique.home.sfr.fr/detecteur-d-ouverture-de-porte-ou-fenetre
SMOKE_DETECTOR = 'SMOKE'				# https://boutique.home.sfr.fr/detecteur-de-fumee
SIREN = 'SIREN'						# https://boutique.home.sfr.fr/sirene-interieure (et peut-être https://boutique.home.sfr.fr/sirene-exterieure)
REMOTE_CONTROLER = 'REMOTE'				# https://boutique.home.sfr.fr/telecommande
KEYPAD_CONTROLER = 'KEYPAD'				# https://boutique.home.sfr.fr/clavier-de-commande
PRESENCE_CAMERA_DETECTOR = 'PIR_CAMERA'			# https://boutique.home.sfr.fr/camera
TEMPHUM_SENSOR = 'TEMP_HUM'				# https://boutique.home.sfr.fr/thermometre
ONOFF_PLUG = 'ON_OFF_PLUG'				# https://boutique.home.sfr.fr/prise-commandee-connectee-legrand

mode = MySystem.get_mode()
def switch(mode):
    if mode == 0:
        return 'OFF'
    elif mode == 1:
        return 'CUSTOM'
    elif mode == 2:
        return 'ON'
    else:
        abort(404)
