import ssl
import re
import socket
import logging
from socketserver import TCPServer, ThreadingMixIn, StreamRequestHandler

logging.basicConfig(level=logging.INFO, format='%(message)s',
                    datefmt='', filename='logfile.log', filemode='a')
p_octet = None


class MySSL_TCPClient:
    """
    """
    print('in Myssl Client')
    def __init__(cls, ip, port):
        cls.ssl_sock = ssl.wrap_socket(socket.socket(socket.AF_INET, socket.SOCK_STREAM),
                                   ca_certs="cert.pem",
                                   cert_reqs=ssl.CERT_NONE,
                                   ssl_version=ssl.PROTOCOL_TLS)
        cls.ssl_sock.connect((ip, port))
        print('in init----')

    def send(self, data):
        """
        :param data:
        :return:
        """
        data = repr(data)
        self.ssl_sock.send(data[1:-1].encode())
        print('in send-----')

    def close(self):
        self.ssl_sock.close()


class MySSL_TCPServer(TCPServer):
    def __init__(self,
                 server_address,
                 RequestHandlerClass,
                 certfile,
                 keyfile,
                 ssl_version=ssl.PROTOCOL_TLS,
                 bind_and_activate=True):
        TCPServer.__init__(self, server_address, RequestHandlerClass, bind_and_activate)
        self.certfile = certfile
        self.keyfile = keyfile
        self.ssl_version = ssl_version

    def get_request(self):
        newsocket, fromaddr = self.socket.accept()
        connstream = ssl.wrap_socket(newsocket,
                                     server_side=True,
                                     certfile=self.certfile,
                                     keyfile=self.keyfile,
                                     ssl_version=self.ssl_version)
        return connstream, fromaddr


class testHandler(StreamRequestHandler):
    def handle(self):
        global p_octet
        total_data = ""
        data = self.connection.recv(8192)
        total_data += data.decode()
        octet = re.match('(^\d*)\s*<\d+>s*.*', total_data)
        if octet:
            p_octet = octet.groups()[0]
        if p_octet:
            if int(p_octet) <= len(data[len(p_octet) + 1:]):
                # print(str(p_octet) + " " + total_data[len(p_octet) + 1:int(p_octet)+ len(str(p_octet)) + 1])
                logging.info(str(p_octet) + " " + total_data[len(p_octet) + 1:int(p_octet) + len(str(p_octet)) + 1])
                total_data = total_data[int(p_octet) + 1 + len(str(p_octet)):]
                p_octet = None


class MySSL_ThreadingTCPServer(ThreadingMixIn, MySSL_TCPServer): pass


def start_server():
    """
    :return:
    """
    listening = True
    try:
        MySSL_ThreadingTCPServer(('0.0.0.0', 6514), testHandler, "cert.pem", "key.pem").serve_forever()
    except (IOError, SystemExit):
        raise
    except KeyboardInterrupt:
        print("Crtl+C Pressed. Shutting down.")


if __name__ == "__main__":
    listening = True
    try:
        MySSL_ThreadingTCPServer(('0.0.0.0', 6514), testHandler, "cert.pem", "key.pem").serve_forever()
    except (IOError, SystemExit):
        raise
    except KeyboardInterrupt:
        print("Crtl+C Pressed. Shutting down.")
