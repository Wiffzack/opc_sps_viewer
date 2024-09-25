from platform import node
import opcua
import time
import os,sys
import os

system_name = ""
try:
    system_name = os.getenv('HOSTNAME')
except:
    import socket
    system_name = (socket.gethostname())

class OPC_Client:
    """
    client is a list of all connections identified by the ip
    """
    client = {}
    node: any = {}
    
    def is_connection_alive(self,client):
        try:
            # Attempt a small operation to check if the connection is alive
            client.get_objects_node()
            return True
        except Exception:
            return False

    def __init__(self, ip, name, password, connect_string):
        """
        Initialize a new OPC_Client.
        """
        self.ip = ip
        self.name = name
        self.password = password
        self.connect_string = connect_string

    def get_node(self):
        if (self.connect_string):
            self.node[self.ip] = self.client[self.ip].get_node(self.connect_string)
        else:
            print ("No connection String supplied!")

    def connect(self):
        try:
            self.client[self.ip] = opcua.Client("opc.tcp://" + self.ip + ":4840")
        except Exception as e:
            sys.exit("Error: Connection could not established Error:"+e)
        try:   
            #client.set_security_string("Basic256Sha256,SignAndEncrypt,certificate.pem,key.pem")
            self.client[self.ip].set_security_string("Basic256Sha256,SignAndEncrypt,certificate.pem,key.pem")
        except TimeoutError as e:
            if("timed" in str(e)):
                print ("Target not reachable")
                sys.exit("Error: Connection could not established")      

        self.client[self.ip].application_uri = "urn:urn:"+system_name+":python:server"
        self.client[self.ip].set_user(self.name)
        self.client[self.ip].set_password(self.password)
        
        try:
            self.client[self.ip].connect()
        except Exception as e:
            if("BadUserAccessDenied" in str(e)):
                sys.exit("Error: Password or Username wrong!")
            if("BadTooManySessions" in str(e)):
                sys.exit("Error: Too many session (max reached): Did you close the old connection correctly?")
            if("BadCertificateUriInvalid" in str(e)):
                print ('"Error: The URI specified in the ApplicationDescription does not match the URI in the certificate."(BadCertificateUriInvalid)')
                sys.exit('Did you configure the application_uri ?')
    
        # Check if connection work
        assert(self.is_connection_alive(self.client[self.ip]) == True)

    

    def get_children(self):
        if self.node:
            return self.node[self.ip].get_children()
