#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# Fake AP generator

__author__ = '090h'
__license__ = 'GPL'

from os import path
import logging
logging.getLogger("scapy.runtime").setLevel(logging.ERROR)
from scapy.all import *

def fake_ap(ssid, iface='wlan1', loop=0, count=100):
    sendp(Dot11(addr1="ff:ff:ff:ff:ff:ff",addr2=RandMAC(),addr3=RandMAC())/
          Dot11Beacon(cap="ESS")/
          Dot11Elt(ID="SSID",info=ssid)/
          Dot11Elt(ID="Rates",info='\x82\x84\x0b\x16')/
          Dot11Elt(ID="DSset",info="\x03")/
          Dot11Elt(ID="TIM",info="\x00\x01\x00\x00"),iface=iface,loop=loop, count=count)


def fuzz(filename):
    if not path.exists(filename):
        print('File does not exist: %s' % filename)
        return
    for ssid in open(filename, 'r').readlines():
        if ssid is None:
            continue
        print('SSID: %s' % ssid)
        fake_ap(ssid)
    print "Done"

if __name__ == '__main__':
    fuzz('ap.txt')