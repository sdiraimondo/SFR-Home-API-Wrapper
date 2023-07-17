from flask import Flask
import os
from urllib import request
from http.cookiejar import CookieJar
from urllib.parse import urlencode
from urllib.error import HTTPError
from time import time
import homesfr

app = Flask(__name__)

# Login
username = %USER%
password = %PASSWORD%

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

@app.route("/api/hello/")
def hello():
    return "Home by SFR APIR Wrapper"

@app.route('/api/get_alarm_mode/')
def get_mode():
    homesfr.__init__ (username, password, None, False, True)
    if homesfr.login=True:
        mode = homesfr.get_mode()
        return mode
    return (None)  

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True,host='0.0.0.0',port=port)
