# constants for spolksping package
import socket
import struct


ICMP_ECHO_REQUEST = 8, 0
ICMP_ECHO_REPLY = 0, 0
ICMP_PROTO = socket.getprotobyname("icmp")

MIN_PAYLOAD_SIZE = struct.calcsize("d")
