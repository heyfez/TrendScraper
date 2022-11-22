#!/usr/bin/python
# -*- coding: utf-8 -*-
import requests as rq
import json
import logging
import coloredlogs

logger = logging.getLogger(__name__)
logger.propagate = False
coloredlogs.DEFAULT_LOG_FORMAT = '[%(asctime)s.%(msecs)03d] %(name)s %(levelname)s %(message)s'
coloredlogs.install(level='DEBUG', logger=logger)

PROMO_URL = "https://www.trendevice.com/prodotti/apple/iphone/iphone-11-256-gb-red-a/?utm_source=ispazio&utm_medium=pr&utm_campaign=blackweeks"

VAR_GB = {"26": 64, "27": 128, "28": 256}
VAR_COLOR = {"32": "bianco", "33": "nero", "39": "giallo",
             "41": "verde", "44": "red", "103": "viola", "82": "colore-a-sorpresa"}
VAR_GRADE = {"176": "c", "88": "b", "89": "a", "90": "come-nuovo"}


def get_html():
    r = rq.get(PROMO_URL).text
    # Get the stock API
    text_stock = r.split('var quantita_raggruppamenti = ')[
        1].split(';')[0]
    stock = json.loads(text_stock)
    keys = stock.keys()
    for k in keys:
        if len(k.split('-')) == 3:
            quantity = stock[k]['quantita']
            gb, color, condition = k.split('-')
            # Price
            p1 = stock[k]['dati']['prezzo']
            # Promo price (should be 1)
            p2 = stock[k]['dati']['prezzo_promo']
            # Discount (could be more then 0)
            p3 = stock[k]['dati']['preorder_sconto']
            # Don't know which parameter is correct so i used all of them
            if float(p1) < 10 or float(p2) < 10 or float(p3) > 0:
                # Building the product url schema with right parameters for notification
                url = f"https://www.trendevice.com/prodotti/apple/iphone/iphone-11-{VAR_GB[gb]}-gb-{VAR_COLOR[color]}-{VAR_GRADE[condition]}/?utm_source=ispazio&utm_medium=pr&utm_campaign=blackweeks"
                # Colored notification
                logger.warning(url)
                # Colored product info
                logger.warning(f"{quantity} - {p1} - {p2} - {p3}")
                return False
    return True


if __name__ == "__main__":
    while True:
        try:
            if not get_html():
                break
            logger.debug('Nothing found...')
        except Exception as err:
            logger.error(err)
