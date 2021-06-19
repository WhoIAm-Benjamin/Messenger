# import all design
from PySide2 import QtWidgets, QtCore#, QtGui

import design_messenger
# import all libraries
import socket
import sys
import os
import logging
import pickle


server_settings = ('192.168.0.47', 8080)
all_messages = []
all_contacts = []

logging.basicConfig(filename = 'logs.log',
                    filemode = 'w',
                    format = '%(asctime)s %(levelname)s : %(message)s',
                    level = logging.DEBUG)

class MainWindow(QtWidgets.QMainWindow, design_messenger.Ui_client):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.messages.clicked.connect(self.message_manager)
        self.contacts.clicked.connect(self.contact_manager)
        self.new_message.clicked.connect(self.write_new_message)
        self.send.clicked.connect(self.sender)

        self.name_label.hide()
        self.name_edit.hide()
        self.message_write.hide()
        self.send.hide()

        if not os.path.exists('data'):
            os.system('mkdir data')
        self.message_manager()
        main()

    def message_manager(self):
        self.checker(1)
        for i in all_messages:
            self.listing.addItem(i)
        self.scrollArea.setGeometry(QtCore.QRect(0, 62, 190, 414))
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 188, 412))
        self.listing.setGeometry(QtCore.QRect(0, 0, 190, 414))
        self.new_message.show()

    def contact_manager(self):
        self.checker(2)
        for i in all_contacts:
            self.listing.addItem(i)
        self.scrollArea.setGeometry(QtCore.QRect(0, 34, 190, 442))
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 188, 412))
        self.listing.setGeometry(QtCore.QRect(0, 0, 190, 442))
        self.new_message.hide()

    def checker(self, mode):
        global all_messages, all_contacts, window
        if mode == 1:
            try:
                with open(os.path.join('data', 'messages.bin'), 'r') as f:
                    all_messages = pickle.load(f)
            except FileNotFoundError:
                f = open(os.path.join('data', 'messages.bin'), 'w')
                f.close()
            except TypeError:
                all_messages = []
            if len(all_messages) == 0:
                self.empty_label.setText('Empty')
        elif mode == 2:
            try:
                with open(os.path.join('data', 'contacts.bin'), 'r') as f:
                    all_contacts = pickle.load(f)
            except FileNotFoundError:
                f = open(os.path.join('data', 'contacts.bin'), 'w')
                f.close()
            except TypeError:
                all_contacts = []
            if len(all_contacts) == 0:
                self.empty_label.setText('Empty')

    # noinspection PyArgumentList
    def write_new_message(self):
        self.select_dialog.hide()
        # self.name_label.raise_()
        # self.name_edit.raise_()
        self.name_label.show()
        self.name_edit.show()
        self.message_write.show()
        self.send.show()

    def sender(self):
        pass

def main():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    while True:
        if connect(sock):
            break
    # print('Successfull connected')

def connect(sock):
    # noinspection PyBroadException
    try:
        sock.connect(server_settings)
        logging.debug('Connected to ' + server_settings[0] + ':' + str(server_settings[1]))
        return True
    except:
        return False


if __name__ == '__main__':
    app = QtWidgets.QApplication()
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())