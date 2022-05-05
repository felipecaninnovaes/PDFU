#///////////////////////////////////////////////////////////////
#
# BY: FELIPE CANIN NOVAES
# PROJECT MADE WITH: PDFU
# V: 1.0.6
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



import requests, platform
from PySide6.QtWidgets import *

import webbrowser

class PDFUpdater(object):
    def pdf_updater(self, pdfu_version):
        os = platform.system()
        url= "https://api.github.com/repos/felipecaninnovaes/PDFU/releases/latest"
        resp = requests.get(url)
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