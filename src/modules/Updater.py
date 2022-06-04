#///////////////////////////////////////////////////////////////
#
# BY: FELIPE CANIN NOVAES
# PROJECT MADE WITH: PDFU
# V: 1.0.7
#
# This project can be used freely for all uses, as long as they maintain the
# respective credits only in the Python scripts, any information in the visual
# interface (GUI) can be modified without any implication.
#
# There are limitations on Qt licenses if you want to use your products
# commercially, I recommend reading them on the official website:
# https://doc.qt.io/qtforpython/licenses.html
#
# ///////////////////////////////////////////////////////////////



import requests, platform, json
from PySide6.QtWidgets import *

import webbrowser

class PDFUpdater(object):
    def pdf_updater(self, pdfu_version):
        f = open('proxy.json')
        data = json.load(f)
        proxy_ip = data['proxy_ip']
        proxy_port = data['proxy_port']
        proxy_user = data['proxy_user']
        proxy_password = data['proxy_password']
        
        proxies = {
        'http': 'http://' + proxy_ip + ':' + proxy_port,
        'https': 'http://' + proxy_ip + ':' + proxy_port,
        }
        
        os = platform.system()
        url= "https://api.github.com/repos/felipecaninnovaes/PDFU/releases/latest"
        
        if proxy_ip == '0' :
            resp = requests.get(url)
        else :
            resp = requests.get(url, proxies=proxies, auth=(proxy_user, proxy_password))
            
        resp = resp.json()
        version = resp['tag_name']
        print (version)
        
        if pdfu_version == version :
            return 0
        else :
            answer = QMessageBox.question(self,'Deseja atualizar?', "Deseja atualizar?", QMessageBox.Yes | QMessageBox.No)
            if QMessageBox.Yes == answer:
                if os == 'Darwin' :
                    webbrowser.open('https://github.com/felipecaninnovaes/PDFU/releases/download/' + version + '/PDFU_Setup_' + version + '_' + 'MacOS' + '.dmg')
                elif os == 'Linux':
                    webbrowser.open('https://github.com/felipecaninnovaes/PDFU/releases/download/' + version + '/PDFU_Setup_' + version + '_' + 'Linux' + '.zip')
                elif os == 'Windows':
                    webbrowser.open('https://github.com/felipecaninnovaes/PDFU/releases/download/' + version + '/PDFU_Setup_' + version + '_' + 'Windows' + '.exe')
            elif QMessageBox.No == answer:
                print ('nao')