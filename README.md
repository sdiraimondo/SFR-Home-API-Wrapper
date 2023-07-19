# API Wrapper pour SFR Home
Il s'agit d'une API basé sur Flask et reposant sur une bibliothèque de @Almtesh permettant d'accéder au système Home by SFR (https://github.com/Almtesh/homesfr/)
Le code de la bibliothèque s'appuie sur les appels fait sur le [site](https://home.sfr.fr) identifiés par rétro-ingénérie.

# Comment l'installer ?
## Prérequis 
* Docker-ce
* Identifiants SFR Home

## Procédure
* git clone https://github.com/sdiraimondo/SFR-Home-API-Wrapper
* cd ./SFR-Home-API-Wrapper
* docker build -t sfr-home-api:latest
* docker run -d -p 5000:5000 sfr-home-api:latest

## Fonctionnalités supportées
* Etat de l'alarme ('/api/get_alarm_mode/')
* WIP, d'autres fonctionnalités à venir (état des capteurs notamment)

# Licence
Voir la [licence](LICENSE) pour plus de détails.
