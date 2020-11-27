import socket
from datetime import datetime

freeports = []
MAXPORTS = 65535

PORTDEFS = {1:"TCPMUX", 5:"RJE",7:"ECHO",18:"MSP",20:"FTP",21:"FTP",22:"SSH",23:"Telnet",
            25:"SMTP",29:"MSG ICP",37:"Time",42:"Host Name Server",43:"WhoIs",49:"Login",
            53:"DNS",69:"TFTP",70:"Gopher Services",79:"Finger",80:"HTTP",103:"X.400 Standard",
            108:"SNA",109:"POP2",110:"POP3",115:"SFTP",118:"SQL",119:"NNTP",137:"NetBIOS",
            139:"NetBIOS",143:"IMAP",150:"NetBIOS",156:"SQL",161:"SNMP",179:"BGP",190:"GACP",
            194:"IRC",197:"DLS",389:"LDAP",396:"Novell Netware over IP",443:"HTTPS",444:"SNPP",
            445:"Microsoft-DS",458:"Apple QuickTime",546:"DHCP",547:"DHCP",563:"SNEWS",
            569:"MSN",1080:"Socks"}

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def scan(target, portsart, portend):
    targetIP = socket.gethostbyname(target)
    tstart = datetime.now()
    for port in range(portsart, portend):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        res = s.connect_ex((targetIP, port))
        if res == 0:
            freeports.append(str(port))
            print(bcolors.OKCYAN+"Port "+str(port)+" is "+bcolors.ENDC+bcolors.OKGREEN+"Open"+bcolors.ENDC)
        s.close()

    tend = datetime.now()
    diff = tend - tstart
    print(bcolors.HEADER+"Scan Completed in "+str(diff)+bcolors.ENDC)
    print(bcolors.WARNING+"Open Ports: "+bcolors.ENDC)
    for i in range(len(freeports)):
        try:
            print(str(freeports[i])+"   "+str(PORTDEFS[int(freeports[i])]))
        except:
            print(str(freeports[i])+"   UNKNOWN")