#!/usr/bin/env python

import argparse
import sys
import socket
import random
import struct
import re
import readline
import numpy as np
import time

from scapy.all import sendp, send, srp1, get_if_list, get_if_hwaddr
from scapy.all import Packet, hexdump
from scapy.all import Ether, IP, UDP, ShortField, StrFixedLenField, XByteField, IntField
from scapy.all import bind_layers
from scapy.config import conf

DPORT = 0x1F40


def get_if():
    ifs=get_if_list()
    iface=None # "h1-eth0"
    for i in get_if_list():
        if "eth0" in i:
            iface=i
            break;
    if not iface:
        print "Cannot find eth0 interface"
        exit(1)
    return iface


def main():

    if len(sys.argv)<2:
        print 'pass 1 argument: <destination IP>'
        exit(1)

    addr = socket.gethostbyname(sys.argv[1])
    iface = get_if()
    print "sending on interface %s to %s" % (iface, str(addr))

    jsonFile = open("test.json", 'r')
    data = jsonFile.read()

    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    # data = struct.pack('>III10s', t[0],t[1],t[2], string)
    s.sendto(data, (addr, DPORT))
    time.sleep(0.01)

         


if __name__ == '__main__':
    main()
