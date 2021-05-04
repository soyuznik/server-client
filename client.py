import socket
import threading




class MainClient():
    def __init__(self):
        # Connecting To Server
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.ADDR = ('localhost' , 55555)
        ADDR = self.ADDR
        self.client.connect(ADDR)


    # Listening to Server and Sending Nickname
    def receive(self):
        while True:

            self.message_received = self.client.recv()

            print(f"Message -> '{self.message_received}' received")
        receive_thread = threading.Thread(target=self.receive)
        receive_thread.start()

    # Sending Messages To Server
    def write(self):
        while True:
            self.message = input("_>")
            self.client.send(self.message.encode('ascii'))





    # Starting Threads For Listening And Writing

client = MainClient
receive_thread = threading.Thread(target=client.receive)
receive_thread.start()
write_thread = threading.Thread(target=client.write)
write_thread.start()





