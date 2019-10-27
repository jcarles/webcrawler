## Descripció
Aquest programa extreu informació sobre avistaments de suposats OVNIS als USA de la base de dades de la web nuforc.org
Aquesta pràctica s'ha realitzat sota el context de l'assignatura Tipologia i cicle de vida de les dades, del Màster en Ciència de Dades de la UOC. S'apliquen tècniques de web scraping per extreure dades mitjançant Python de la web nuforc.org i generar un dataset.

## Membres de l'equip

Aquesta activitat ha estat realitzada de manera individual per **Joan Carles Badia Purroy**.

## Fitxers del codi font

* download.py : Funció per a descarregar el codi html d'una url donada
* crawl_url.py : funció per a extreure de la pàgina principal, els links a les url on hi ha la informació i baixar cadascuna de les pàgines web i cridar al callback que les interpreti .
* ScrapeCallback.py : Conté la classe que es crida quan s'ha extret els anteriors links i que, mitjançant lxml cerca dins de la taula html, les dades. Tot seguit les guarda en arrays i les va volcant en un fitxer .csv . El fitxer també conté el punt d'entrada principal main (per executar tot el procés) 
