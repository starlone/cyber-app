import binascii
import socket
import struct


def packet_sniffer(callback):
    s = socket.socket(socket.PF_PACKET, socket.SOCK_RAW, socket.ntohs(0x0800))
    while True:
        pkt = s.recvfrom(2048)

        # Ethernet Frame
        ethhead = pkt[0][0:14]
        eth = struct.unpack("!6s6s2s", ethhead)

        # IP
        binascii.hexlify(eth[2])
        ipheader = pkt[0][14:34]
        ip_hdr = struct.unpack("!12s4s4s", ipheader)

        obj = {
            'mac': {
                'dest': binascii.hexlify(eth[0]),
                'source': binascii.hexlify(eth[1])
            },
            'ip': {
                'source': socket.inet_ntoa(ip_hdr[1]),
                'dest': socket.inet_ntoa(ip_hdr[2])
            }
        }

        callback(obj)
