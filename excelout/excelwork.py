#!/usr/bin/en
import socket
## sudo apt install python3-pip

## python3 -m pip install pyexcel
## python3 -m pip install pyexcel-xls
import pyexcel

# Request data from user
x = 0

while x < 0:
    def get_ip_data():
        try:
             input_ip = input("\nWhat is the IP address? ")
             socket.inet_aton(input_ip)
   x = 1
         except:
             print("Entry was not in the correct Format.")

 input_driver = input("What is the driver associated with this device? ")
 input_passenger = input("What is your favorite color? ")
 input_back_seat_driver = input("Why are you back there? ")
 d = {"IP": input_ip, "driver": input_driver, "passenger": input_passenger, "BackSeat": input_back_seat_driver}
 return d
     
## This code is left turned off, but might help visualize how pyexcel works with data sets.
## IP is the first column, whereas driver is the second column.
## mylistdict = [ {"IP": "172.16.2.10", "driver": "arista_eos"}] {"IP": "172.16.2.20", "driver": "arista_eos"} ]
## pyexcel.save_as(records=mylistdict, dest_file_name="ip_list.xls")


# Runtime
mylistdict = []  # this will be our list we turn into a *.xls file
print("Hello! This program will make you a *.xls file")

while(True):
    mylistdict.append(get_ip_data()) # add an item to the list returned by get_ip_data() \

    keep_going = input("\nWould you like to add another value? Enter to continue, or \
    enter 'q' to quit: ")
    if (keep_going.lower() == 'q'):
        break

filename = input("\nWhat is the name of the *.xls file? ")

pyexcel.save_as(records=mylistdict, dest_file_name=f'{filename}.xls')

print("The file " + filename + ".xls should be in your local directory")
