import os
import sys
import colorama
import subprocess
from datetime import datetime
from colorama import Fore, Back, Style, init
from socket import gethostbyname, socket, AF_INET, SOCK_STREAM, gaierror, error
           
def getpDescr(pNum):
    knowPorts = {
        '1':	'TCP Port Service Multiplexer (TCPMUX)',
        '5':	'Remote Job Entry (RJE)',
        '7':	'ECHO',
        '18':	'Message Send Protocol (MSP)',
        '20':	'FTP -- Data',
        '21':	'FTP -- Control',
        '22':	'SSH Remote Login Protocol',
        '23':	'Telnet',
        '25':	'Simple Mail Transfer Protocol (SMTP)',
        '29':	'MSG ICP',
        '37':	'Time',
        '42':	'Host Name Server (Nameserv)',
        '43':	'WhoIs',
        '49':	'Login Host Protocol (Login)',
        '53':	'Domain Name System (DNS)',
        '69':	'Trivial File Transfer Protocol (TFTP)',
        '70':	'Gopher Services',
        '79':	'Finger',
        '80':	'HTTP',
        '103':	'X.400 Standard',
        '108':	'SNA Gateway Access Server',
        '109':	'POP2',
        '110':	'POP3',
        '115':	'Simple File Transfer Protocol (SFTP)',
        '118':	'SQL Services',
        '119':	'Newsgroup (NNTP)',
        '137':	'NetBIOS Name Service',
        '139':	'NetBIOS Datagram Service',
        '143':	'Interim Mail Access Protocol (IMAP)',
        '150':	'NetBIOS Session Service',
        '156':	'SQL Server',
        '161':	'SNMP',
        '179':	'Border Gateway Protocol (BGP)',
        '190':	'Gateway Access Control Protocol (GACP)',
        '194':	'Internet Relay Chat (IRC)',
        '197':	'Directory Location Service (DLS)',
        '389':	'Lightweight Directory Access Protocol (LDAP)',
        '396':	'Novell Netware over IP',
        '443':	'HTTPS',
        '444':	'Simple Network Paging Protocol (SNPP)',
        '445':	'Microsoft-DS',
        '458':	'Apple QuickTime',
        '546':	'DHCP Client',
        '547':	'DHCP Server',
        '563':	'SNEWS',
        '569':	'MSN',
        '1080': 'Socks'
    }

    if knowPorts[str(pNum)]:
        return knowPorts[str(pNum)]
    else:
        return ''


def welcome():

    print "-" * 60
    print "-" * 60

    ART = """
                   _____
                  / ____|
      _ __  _   _| (___   ___ __ _ _ __  _ __   ___ _ __
     | '_ \| | | |\___ \ / __/ _` | '_ \| '_ \ / _ \ '__|
     | |_) | |_| |____) | (_| (_| | | | | | | |  __/ |
     | .__/ \__, |_____/ \___\__,_|_| |_|_| |_|\___|_|
     | |     __/ |
     |_|    |___/

        >   Author: Glenn LE GAC
        >   Course: Offensive Pytrhon

        >   Just a simple Port Scanner ...

    """
    print ART

    print "-" * 60
    print "-" * 60
    print "\n"



def portScan(rHostIP, pMin, pMax):

    for p in range(pMin, pMax):

        s = socket(AF_INET, SOCK_STREAM)
        s.settimeout(0.1)
        result = s.connect_ex((rHostIP, p))

        if result == 0:
            print "[+] Port %s" %p + ' ' * 10 + Fore.GREEN + "Open" + Fore.RESET + ' ' * 10 + getpDescr(p)
        else:
            print "[-] Port %s" %p + ' ' * 10 + Fore.RED + "Closed" + Fore.RESET

        s.close()


def main():

    init()
    welcome()

    rHost   = raw_input("Enter a remote host to scan: ")


    print   "> Enter the port range"

    pMin    = int(raw_input("Min: "))
    pMax    = int(raw_input("Max: ")) + 1

    os.system('cls')

    print "-" * 60
    print "Please wait, scanning remote host", rHost
    print "-" * 60

    time1     = datetime.now()
    portScan(rHost, pMin, pMax)
    time2     = datetime.now()
    totalTime = time2 - time1

    print "-" * 60
    print 'Scanning Completed in: %s' %totalTime
    print "-" * 60



main()
