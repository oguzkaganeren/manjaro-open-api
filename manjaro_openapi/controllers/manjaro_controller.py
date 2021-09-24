#!/usr/bin/env python3
import connexion
from jose import JWTError, jwt
from werkzeug.exceptions import Unauthorized
from Manjaro.SDK.PackageManager import Pamac
import json
import datetime
import time
from swagger_ui_bundle import swagger_ui_3_path

JWT_ISSUER = 'com.zalando.connexion'
JWT_SECRET = 'change_this'
JWT_LIFETIME_SECONDS = 99999999999
JWT_ALGORITHM = 'HS256'


def generate_token(userId):
    timestamp = _current_timestamp()
    payload = {
        "iss": JWT_ISSUER,
        "iat": int(timestamp),
        "exp": int(timestamp + JWT_LIFETIME_SECONDS),
        "sub": str(userId),
    }

    return jwt.encode(payload, JWT_SECRET, algorithm=JWT_ALGORITHM)

def decode_token(token):
    try:
        return jwt.decode(token, JWT_SECRET, algorithms=[JWT_ALGORITHM])
    except JWTError as e:
        raise Unauthorized from e

def _current_timestamp() -> int:
    return int(time.time())

pmc=Pamac()
        
def get_category_list() -> list:
    return pmc.get_categories()
    
    
def get_repos() -> list:
    return pmc.get_repos()

def get_pkgs(repoName:str,pageNumber:float) -> list:
    pkgs = pmc.get_pkgs(repoName,pageNumber)
    pkgListRt = []
    for x in range(len(pkgs)):
        pkgListRt.append(get_package_details_json(pkgs[x]))
    return pkgListRt

def get_pkgs_flatpaks(pageNumber:float)->list:
    pkgs = pmc.get_pkgs_flatpaks(pageNumber)
    pkgListRt = []
    for x in range(len(pkgs)):
        pkgListRt.append(get_package_details_json(pkgs[x]))
    return pkgListRt

def get_pkgs_snaps(pageNumber:float)->list:
    pkgs = pmc.get_pkgs_snaps(pageNumber)
    pkgListRt = []
    for x in range(len(pkgs)):
        pkgListRt.append(get_package_details_json(pkgs[x]))
    return pkgListRt
    
def search_flatpaks(pkgName: str) -> list:
    pkgs = pmc.search_flatpaks(pkgName)
    pkgListRt = []
    for x in range(len(pkgs)):
        pkgListRt.append(get_package_details_json(pkgs[x]))
    return pkgListRt

def search_snaps(pkgName: str) -> list:
    pkgs = pmc.search_snaps(pkgName)
    pkgListRt = []
    for x in range(len(pkgs)):
        pkgListRt.append(get_package_details_json(pkgs[x]))
    return pkgListRt

def search_pkgs(pkgName: str) -> list:
    pkgs = pmc.search_pkgs(pkgName)
    pkgListRt = []
    for x in range(len(pkgs)):
        pkgListRt.append(get_package_details_json(pkgs[x]))
    return pkgListRt

def get_package_details_json(pkg) -> str:
    data = {}
    data['app_id'] = pkg.get_app_id()
    data['app_name'] = pkg.get_app_name()
    data['desc']=pkg.get_desc()
    data['download_size']=pkg.get_download_size()
    if type(pkg).__name__ != "PamacSnapPackageLinked":
        data['files']=pkg.get_files()
        data['groups']=pkg.get_groups()
        data['has_signature']=pkg.get_has_signature()
        data['build_date'] = pkg.get_build_date().format ("%x") 
        data['makedepends']=pkg.get_makedepends()
        data['optdepends']=pkg.get_optdepends()
        data['optionalfor']=pkg.get_optionalfor()
        data['packager']=pkg.get_packager()
        data['provides']=pkg.get_provides()
        data['requiredby']=pkg.get_requiredby()
    data['icon']=pkg.get_icon()
    data['id']=pkg.get_id()
    data['license']=pkg.get_license()
    data['long_desc']=pkg.get_long_desc()
    data['name']=pkg.get_name()
    data['repo']=pkg.get_repo()
    data['screenshots']=pkg.get_screenshots()
    data['url']=pkg.get_url()
    data['version']=pkg.get_version()
    return data

if __name__ == '__main__':
    options = {'swagger_path': swagger_ui_3_path}
    app = connexion.FlaskApp(__name__, port=9090, specification_dir='swagger/', options=options)
    app.add_api('manjaro-api.yaml', arguments={'title': 'Manjaro Api'})
    app.run()