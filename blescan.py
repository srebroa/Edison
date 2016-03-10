#!/usr/bin/env python
print "BLE SCANER v1.0"
user_input = raw_input("Would you like to start scanning BLE devices? (Y/N)")
if user_input.strip() == 'y' or 'Y':
 print "Start Scanning ....."
 bashCommand = "bluetoothctl"
 import subprocess
 process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
 output = process.communicate()[0]

else:
 print "Close"


