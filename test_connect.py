import opcua
import time
import os


client1 = opcua.Client("opc.tcp://192.168.137.7:4849")
#client1.set_user("admin")
#client1.set_password("wago")
client1.connect()
print ("connected ")
client1.disconnect()