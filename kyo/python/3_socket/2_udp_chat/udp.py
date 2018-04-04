#!/usr/bin/env python3


import socket


BUFSIZE = 1024

class PacketTypeExistsError(Exception):
    pass


class SendPacketError(Exception):
    pass


class PacketType:

    valMax = 1
    nameList = []
    valList = []

    def __init__(self, name, ack=False, val=None):
        if name in PacketType.nameList or val in PacketType.valList:
            raise PacketTypeExistsError

        self.name = name
        self.ack = ack
        self.val = val or PacketType.valMax
        PacketType.nameList.append(self.name)
        PacketType.valList.append(self.val)
        PacketType.valMax += 1

    def isAck(self):
        return self.ack

    def __str__(self):
        return "%s(%s):%s" % (self.name, self.val, self.ack)

    def __repr__(self):
        return str(self)

    def __bytes__(self):
        return chr(self.val).encode()

    def __eq__(self, val):
        return bool(val == self.val)

    def __ne__(self, val):
        return bool(val != self.val)

PT_CONN = PacketType('Connection')
PT_CONN_ACK = PacketType('Connection Ack', True)
PT_DATA = PacketType('Data')
PT_DATA_ACK = PacketType('Data Ack', True)
PT_ERROR = PacketType('Error', True)


class UdpBase:

    def __init__(self, port=9000, ip="0.0.0.0", **kwargs):
        self.ip = ip
        self.port = port
        self.last_addr = None
        self.last_type = None
        self.__dict__.update(kwargs)
        self.sd = socket.socket(type=socket.SOCK_DGRAM)

    def recv(self, packet_type=None, timeout=None, sd=None,
             ack_type=None, ack_data=b''):
        sd = sd or self.sd

        old_timeout = sd.gettimeout()
        sd.settimeout(timeout)

        while True:
            data, self.last_addr = sd.recvfrom(BUFSIZE)
            data_type, data = data[0], data[1:]
            #  print("<<<< recv: %s %s, %s, type = %s, ack = %s" % (self.last_addr, data, data_type, packet_type, ack_type))
            if packet_type is None or packet_type == data_type:
                self.last_type = data_type
                break

        if not packet_type.isAck() and ack_type is not None:
            #  print("SEND ACK %s | %s" % (packet_type, ack_type))
            self.send(ack_data, self.last_addr, sd, ack_type)

        sd.settimeout(old_timeout)

        return data

    def send(self, data=b'', addr=None, sd=None,
             packet_type=PT_DATA, ack_type=PT_DATA_ACK, ack_timeout=3):
        sd = sd or self.sd
        addr = addr or (self.ip, self.port)

        if not isinstance(data, bytes):
            data = data.encode()

        data = bytes(packet_type) + data

        ret = sd.sendto(data, addr)
        if ret != len(data):
            raise SendPacketError

        #  print(">>>> send(%s): %s type=%s, ack=%s" % (addr, data, packet_type, ack_type))

        if not packet_type.isAck():
            return self.recv(ack_type, timeout=ack_timeout)


    def __del__(self):
        self.sd.close()


class UdpSrv(UdpBase):

    def __init__(self, port=9000, ip='0.0.0.0', **kwargs):
        self.independent = True

        UdpBase.__init__(self, port, ip, **kwargs)

        self.sd.bind((ip, port))

    def run(self):
        while True:
            data = self.recv(PT_CONN)
            cli_sd = None

            if self.independent:
                cli_sd = socket.socket(type=socket.SOCK_DGRAM)

            self.handle(data, self.last_addr, cli_sd)

            if self.independent:
                cli_sd.close()


class UdpCli(UdpBase):

    def connect(self, request=b'', timeout=None):
        data = self.send(request, (self.ip, self.port), packet_type=PT_CONN,
                         ack_type=PT_CONN_ACK, ack_timeout=timeout)
        self.ip, self.port = self.last_addr
        print("connect server: ", self.last_addr)

        return data


if __name__ == '__main__':
    s = bytes(PT_CONN_ACK)



