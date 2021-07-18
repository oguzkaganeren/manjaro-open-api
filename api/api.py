#!/usr/bin/env python3
import connexion
from PackageManager import Pamac

def get_category_list() -> list:
    pm=Pamac()
    return pm.get_categories()

if __name__ == '__main__':
    app = connexion.FlaskApp(__name__, port=9090, specification_dir='swagger/')
    app.add_api('manjaro-api.yaml', arguments={'title': 'Hello World Example'})
    app.run()