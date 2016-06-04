import socket
import sys

class ajbSocket:
    def __init__(self, sock=None):
        if arg < 3:
            raise ValueError("Invalid Number of Arguments")
        if sock is None:
            self.sock = socket.socket(
                socket.AF_INET, socket.SOCK_STREAM)
        else:
            self.sock = sock

    def connect(self, host, port):
        self.sock.connect((host, port))


    def sendData(self):
        print
        try:
            self.connect('10.97.216.51',31001)
            message = '161,100,,,,10,GiftCard,0000000,00659,0001,BalanceInquiry,,,6006493301500049959,,,0,1220551,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,6100,,,\n'
            print >>sys.stderr, 'sending "%s"' % message
            self.sock.sendall(message)

        # Receive the data in small chunks and retransmit it

            data = self.sock.recv(1024)
            print >>sys.stderr, 'received "%s"' % data


        finally:
            self.sock.close()

def main():
    ajbObj = ajbSocket()
    ajbObj.sendData()

sys.exit(main())