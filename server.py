# import all design
from PySide2 import QtWidgets, QtCore, QtGui

import server_design
# import all libraries
import socket
import sys
from threading import Thread as Th

addresses = ['127.168.0.47']

def starter(value):
    if not value:
        return False

def server_start(server):
    server.listen(4)
    # message about server is working
    while True:
        client_socket, address = server.accept()
        if address not in addresses:
            continue
        data = client_socket.recv(1024).decode('utf-8')
        if data == '':
            client_socket.shutdown(socket.SHUT_WR)
            continue

class MainWindow(QtWidgets.QMainWindow, server_design.Ui_server_window):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.stop_button = QtWidgets.QPushButton(parent = self.centralwidget, text = 'Stop')
        self.stop_button.setGeometry(QtCore.QRect(10, 115, 441, 51))
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(16)
        self.stop_button.setFont(font)
        self.stop_button.setStyleSheet("color: rgb(193, 195, 154);")
        self.stop_button.setObjectName("stop_button")
        self.start_button.clicked.connect(self.start)
        # noinspection PyUnresolvedReferences
        self.stop_button.clicked.connect(self.stop)
        self.stop_button.hide()

    def start(self):
        ip_host = self.IP_host.text()
        if self.Port.text() != '':
            port = int(self.Port.text())
            if port > 65535:
                port = int(str(port)[:4])
            elif port < 0:
                port = - port
        else:
            port = 8080
        self.Port.setText(str(port))
        value = True
        try:
            server = socket.create_server((ip_host, port))
        except OSError:
            value = starter(False)
        if value:
            if self.stop_button.isHidden():
                self.start_button.hide()
                self.stop_button.show()
            self.th = Th(target = server_start, args = (server, ))
            self.th.start()
            return

    def stop(self):
        self.stop_button.hide()
        self.start_button.show()
        # self.th._stop()
        del self.th
        return


if __name__ == '__main__':
    app = QtWidgets.QApplication()
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())