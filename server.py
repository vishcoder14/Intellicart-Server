from flask import Flask

fserver = Flask(__name__)

from rules import delivery_app_routes, order_app_routes

# main
if __name__ == '__main__':
    fserver.run(debug=True)
