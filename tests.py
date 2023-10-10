
from db import db_utils as dbh


# client-id-ref for debug
clientID1 = "tNKX5o99REXiEK3g6QIs48WR1x82"  # v@gmail.com
clientID2 = "Mj3IEh3NuJNeG8LplPHeTF70FK33"  # s@gmail.com

# Define the data for each item
items_data = {
    "tapioca": {"item_image_url": "https://firebasestorage.googleapis.com/v0/b/intelli-cart.appspot.com/o"
                                  "/vegies_images%2Fvegie_tropiaco.jpg?alt=media&token=2aa31e8f-3ff2-47ec-91e4"
                                  "-5ae29c09d107", "item_name": "Tapioca", "item_qty": "2"},
    "potato": {"item_image_url": "https://firebasestorage.googleapis.com/v0/b/intelli-cart.appspot.com/o"
                                 "/vegies_images%2Fvegie_potato.jpeg?alt=media&token=2dc173e7-7e9e-4a4c-921b"
                                 "-5e99d4ae68a5", "item_name": "Potato", "version": "3"}
}
