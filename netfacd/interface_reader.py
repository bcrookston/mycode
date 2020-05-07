#!/usr/bin/env python3

import netifaces

print(netifaces.interfaces())

for i in netifaces.interfaces():
    print('\n********Details of Interface - ' + i + ' ************')
    try:
        print('MAC: ' + (netifaces.ifaddresses(i)[netifaces.AF_LINK])[0]['addr']) # Prints the MAC address
        print('IP: ' + (netifaces.ifaddresses(i)[netifaces.AF_INET])[0]['addr']) # Prints the IP address
    except: 
        print('could not collect adapter information')
