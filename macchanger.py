#!/usr/bin/env python3
import subprocess
import optparse

def get_args():
     parse = optparse.OptionParser()
     parse.add_option("-i", "--interface",dest="interface", help="Enter interface to apply changes to")
     parse.add_option("-m", "--mac-address", dest="new_mac", help="Enter new MAC address")
     (options, arguments) = parse.parse_args()
     if not options.interface:
         parse.error("[+] Enter the interface to apply changes to. Use --help for more information")
     elif not options.new_mac:
         parse.error("[+] Enter the preferred MAC address. Use --help for more information")
     return options

def change_mac(interface, new_mac):
    print("[+] Changing MAC address for " + interface + " to " + new_mac)
    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface,"hw", "ether", new_mac])
    subprocess.call(["ifconfig", interface, "up"])
    print("[+] Updated MAC address for " + interface + " is " + new_mac)

options = get_args()
change_mac(options.interface, options.new_mac)