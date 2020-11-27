import portscanner
import sys

try:
    lol = sys.argv[1]
except:
    lol = input("address: ")

print("Please make sure, that you are allowed by the Server Owner to do this Porttscan")
isAllowed = input("If you are Allowed, please press Enter: ")

portscanner.scan(lol, 0, 7000)
