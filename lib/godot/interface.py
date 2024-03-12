#
# interface.py
#

import socket
import struct
import time

class GodotInterface:

    def __init__(self, uPort = 4444):
        self.port = uPort
        self.sd = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)


class GodotCart1D(GodotInterface):

    def __init__(self, uPort = 4444):
        super().__init__(uPort)

    def process(self, force):
        packet = struct.pack("<f", force)
        self.sd.sendto(packet, ('localhost', self.port))
        (reply, remote) = self.sd.recvfrom(1024)
        (delta, pos, vel) = struct.unpack("<fff", reply[8:])
        return (delta, pos, vel)


class GodotArm1D(GodotInterface):

    def __init__(self, uPort = 4444):
        super().__init__(uPort)

    def process(self, force):
        packet = struct.pack("<f", force)
        self.sd.sendto(packet, ('localhost', self.port))
        (reply, remote) = self.sd.recvfrom(1024)
        (delta, theta, omega) = struct.unpack("<fff", reply[8:])
        return (delta, theta, omega)



if __name__ == "__main__":
    #g = GodotCart1D()
    g = GodotArm1D()

    while True:
        print(g.process(0.5))

