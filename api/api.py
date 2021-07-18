#!/usr/bin/env python3
import connexion
from PackageManager import Pamac


pmc=Pamac()
        
def get_category_list() -> list:
    return pmc.get_categories()
    
    
def get_repos() -> list:
    return pmc.get_repos()
    
def search_flatpaks(pkgName: str) -> list:
    pkgs = pmc.search_flatpaks(pkgName)
    pkgNames = []
    for x in range(len(pkgs)):
        pkgNames.append(pkgs[x].get_name())
    return pkgNames

def search_snaps(pkgName: str) -> list:
    pkgs = pmc.search_snaps(pkgName)
    pkgNames = []
    for x in range(len(pkgs)):
        pkgNames.append(pkgs[x].get_name())
    return pkgNames

if __name__ == '__main__':
    app = connexion.FlaskApp(__name__, port=9090, specification_dir='swagger/')
    app.add_api('manjaro-api.yaml', arguments={'title': 'Hello World Example'})
    app.run()