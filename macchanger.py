#!/usr/bin/env python3
import subprocess
import optparse
import re
import time
import datetime


def get_args():
     parse = optparse.OptionParser()
     parse.add_option("-i", "--interface",dest="interface", help="Enter interface to apply changes to")
     parse.add_option("-m", "--mac-address", dest="new_mac", help="Enter new MAC address")
     (options, arguments) = parse.parse_args()
     if not options.interface:
         parse.error("[-] Enter the interface to apply changes to. Use --help for more information")
     elif not options.new_mac:
         parse.error("[-] Enter the preferred MAC. Use --help for more information")
     return options

def change_mac(interface, new_mac):
    print("[+] Trying to change MAC for " + interface + " to " + new_mac)
    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface,"hw", "ether", new_mac])
    subprocess.call(["ifconfig", interface, "up"])
    #print("[+] Updated MAC for " + interface + " is " + new_mac)

def get_curr_mac(interface):
    ifconfig_result = subprocess.check_output(["ifconfig", interface])
    mac_search = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", str(ifconfig_result))

    if mac_search:
        return mac_search.group(0)
    else:
        print("[-] Interface " + interface + " does not have a MAC")

options = get_args()

curr_mac = get_curr_mac(options.interface)
print("[+] Current MAC is " + str(curr_mac))

change_mac(options.interface, options.new_mac)

curr_mac = get_curr_mac(options.interface)
if curr_mac == options.new_mac:
    print("[+] MAC updated to " + curr_mac)
else:
    print("[-] Failed to update MAC ")

curr_time = time.time()
duration = (time.time() - curr_time)
print("[+] Completed in: " + str(format(duration, ".10f")) + " seconds")
