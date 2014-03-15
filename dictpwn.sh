#!/bin/sh

#TODO: iface list
airmon-ng start wlan1
airmon-ng start wlan2


#wifidict=/usr/share/dict/words
wifidict=/usr/share/dict/words

wifite -pow 30 -i mon0 -mac -pyrit -crack -dict /usr/share/dict/Super-WPA