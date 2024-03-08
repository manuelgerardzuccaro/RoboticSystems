#
# interface.py
#

import socket
import struct
import time

class GodotCart1D:

    def __init__(self, uPort = 4444):
        self.port = uPort
        self.sd = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    def process(self, force):
        packet = struct.pack("<f", force)
        self.sd.sendto(packet, ('localhost', self.port))
        (reply, remote) = self.sd.recvfrom(1024)
        (delta, pos, vel) = struct.unpack("<fff", reply[8:])
        return (delta, pos, vel)



if __name__ == "__main__":
    g = GodotCart1D()

    while True:
        print(g.process(1000.0))

