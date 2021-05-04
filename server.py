import sys
from PyQt5 import QtWidgets as qtw
import socket
import threading




participants = ['localhost' , 55555
                            ,      ]
class MainServer():
        def __init__(self):

            self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.ADDR = ('localhost', 55555)
            ADDR = self.ADDR
            self.server.bind(ADDR)
            self.server.listen()
            print("Server running")
        def accept_request(self):
                while True:
                        self.adress = self.server.accept()
                        print(f"ADDR joined --> {self.adress}")
                        participants.add[self.adress]
                        request_accepting_thread = threading.Thread(target=self.accept_request(self))
                        request_accepting_thread.start(self)
        def send_request(self , message , argAdress , port):
                complete_message = socket.sendmsg(message.encode("ascii") , argAdress , port)
                return f"message sent to {argAdress} , {port} "
        def broadcast_participants(self , broadcast_message):
                print(broadcast_message)

                for self.client in participants:
                        self.server.send(broadcast_message)
        def accept_messages(self):
                while True:
                        try:
                                self.message , self.received_adress = self.participant.recv(2048)
                                print(f"Message received from {self.received_adress} , here it is -> {self.message}")


                        except:
                                print(
                                        f"Connection with client -> {self.adress} , {self.client} has been closed due to unexpected error.")
                                participants.remove[self.client]
                                self.client.close()

                                break

                        accept_messages_thread = threading.Thread(target=self.accept_messages(self))
                        accept_messages_thread.start()
        def accepting_admin_input(self):
                admin_input = input("_>")
                if (admin_input == "!close"):
                        self.server.close()
                if (admin_input == "!info"):
                        print(f"List of PARTICIPANTS:\n")
                        for self.client in participants:
                                print(f"{self.client}")
                if (admin_input == "!kick"):
                        kick = input("Enter client to kick:")
                        participants.remove[kick]
                        self.client.close(kick)
class MainWindow(qtw.QMainWindow , MainServer):#can
    def __init__(self):
        super().__init__()

        #Main Widget and Layout
        self.main_widget = qtw.QWidget()
        self.main_layout = qtw.QVBoxLayout()

        self.main_widget.setLayout(self.main_layout)
        self.setCentralWidget(self.main_widget)

        #Secondary Layout
        self.bottom_layout = qtw.QHBoxLayout()

        #Widgets
        self.send_msg_lnedt = qtw.QLineEdit()
        self.send_msg_btn = qtw.QPushButton()
        self.msg_view_lstwd = qtw.QListWidget()

        #Widgets -> Layouts
        self.main_layout.addWidget(self.msg_view_lstwd)
        self.main_layout.addLayout(self.bottom_layout)
        self.bottom_layout.addWidget(self.send_msg_btn)
        self.bottom_layout.addWidget(self.send_msg_lnedt)

        #Connect Signals and Slots
        self.send_msg_btn.pressed.connect(self.display_msg)#would be better with lineedit as the arg can be directly passes

        self.show()

    def display_msg(self):
        self.msg_view_lstwd.addItem(self.send_msg_lnedt.text())
        self.send_msg_lnedt.clear()
        connector = Connector()
class Connector(MainWindow):
    def __init__(self):
        super().__init__()
        server = MainServer()
        window = MainWindow()
        server.broadcast_participants(window.msg_view_lstwd.text())



if __name__ == "__main__":
    app = qtw.QApplication(sys.argv)
    mw = MainWindow()
    sys.exit(app.exec())
    server = MainServer()


    server.accept_request()
    server.accept_messages()
    server.accepting_admin_input()
