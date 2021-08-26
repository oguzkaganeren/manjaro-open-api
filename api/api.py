#!/usr/bin/env python3
import connexion
from PackageManager import Pamac
import json
import datetime

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

def search_pkgs(pkgName: str) -> list:
    pkgs = pmc.search_pkgs(pkgName)
    pkgNames = []
    for x in range(len(pkgs)):
        data = {}
        data['app_id'] = pkgs[x].get_app_id()
        data['app_name'] = pkgs[x].get_app_name()
        data['build_date'] = pkgs[x].get_build_date().format ("%x") 
        data['desc']=pkgs[x].get_desc()
        data['download_size']=pkgs[x].get_download_size()
        data['files']=pkgs[x].get_files()
        data['groups']=pkgs[x].get_groups()
        data['has_signature']=pkgs[x].get_has_signature()
        data['icon']=pkgs[x].get_icon()
        data['id']=pkgs[x].get_id()
        data['license']=pkgs[x].get_license()
        data['long_desc']=pkgs[x].get_long_desc()
        data['makedepends']=pkgs[x].get_makedepends()
        data['name']=pkgs[x].get_name()
        data['optdepends']=pkgs[x].get_optdepends()
        data['optionalfor']=pkgs[x].get_optionalfor()
        data['packager']=pkgs[x].get_packager()
        data['provides']=pkgs[x].get_provides()
        data['repo']=pkgs[x].get_repo()
        data['requiredby']=pkgs[x].get_requiredby()
        data['screenshots']=pkgs[x].get_screenshots()
        data['url']=pkgs[x].get_url()
        data['version']=pkgs[x].get_version()
        pkgNames.append(data)
        
    return pkgNames


if __name__ == '__main__':
    app = connexion.FlaskApp(__name__, port=9090, specification_dir='swagger/')
    app.add_api('manjaro-api.yaml', arguments={'title': 'Hello World Example'})
    app.run()