from __main__ import fserver
import flask

from db.db_utils import addItem

# client-id-ref for debug
clientID1 = "tNKX5o99REXiEK3g6QIs48WR1x82"  # v@gmail.com
clientID2 = "Mj3IEh3NuJNeG8LplPHeTF70FK3"  # s@gmail.com


@fserver.route('/request/addItemToManualCartDB', methods=['POST'])
def addItemToManualCartDB():
    incoming = flask.request.json
    incoming['item_qty'] = int(incoming.get('item_qty', 1))
    incoming = {str(incoming['item_name']).lower(): incoming}

    addItem.to_manual_cart(clientID1, incoming)
    print(f"\nItem : {incoming}\n")
    return "success"


@fserver.route('/request/addItemToVoiceCartDB', methods=['POST'])
def addItemToVoiceCartDB():
    incoming = flask.request.json
    incoming['item_qty'] = int(incoming.get('item_qty', 1))
    incoming = {str(incoming['item_name']).lower(): incoming}

    addItem.to_voice_cart(clientID1, incoming)
    print(f"\nItem : {incoming}\n")
    return "success"
