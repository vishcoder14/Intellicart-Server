from db import architecture as arch


# put items: map @manualCartProductData db reference
def to_manual_cart(client_id, incoming_items):
    try:
        arch.get_manualCartProductData_ref(str(client_id)).update(incoming_items)
        print(f"update success @{client_id}.manualCartProductData")
        return True
    except Exception as e:
        print(f"Exception occurred {e} !")
        return False


# put items: map @voiceCartProductData db reference
def to_voice_cart(client_id, incoming_items):
    try:
        arch.get_voiceCartProductData_ref(str(client_id)).update(incoming_items)
        print(f"update success @{client_id}.voiceCartProductData")
        return True
    except Exception as e:
        print(f"Exception occurred {e} !")
        return False


# put items: map @orderByVoiceData db reference
def to_order_by_voice(client_id, incoming_items):
    try:
        arch.get_orderByVoiceData_ref(str(client_id)).update(incoming_items)
        print(f"update success @{client_id}.orderByVoiceData")
        return True
    except Exception as e:
        print(f"Exception occurred {e} !")
        return False


def set_client_as_inactive_partner(ref_date, client_id):
    try:
        arch.get_inactivePartners_ref(ref_date).update(str(client_id))
        print(f"update success @{ref_date}.inactivePartners.{client_id}")
        return True
    except Exception as e:
        print(f"Exception occurred {e} !")
        return False
