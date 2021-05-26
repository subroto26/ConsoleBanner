###################################################################
##!/usr/bin/python
## FileName : update_banner.py
## Author :
## Pupose : update the Websphere console banner and login.
## Execute :  "python update_banner.py"
## version : 0.1
##
####################################################################
import re
import sys
import socket
import os
import getpass
import time
import smtplib
from email.mime.text import MIMEText
import subprocess
from subprocess import Popen, PIPE, STDOUT

#### Id's ####
global loginName
global attId
global localHost
loginName = getpass.getuser()
attId = os.getlogin()
localHost = socket.gethostname()

#### File name ####
f1BName = "Prod_banner-swoosh.png"
f2BName = "Test_banner-swoosh.png"
f3BName = "Idle_banner-swoosh.png"
f1LName = "Prod_loginBkgd.jpg"
f2LName = "Test_loginBkgd.jpg"
f3LName = "Idle_loginBkgd.jpg"
f01 = '/usr/local/bin/sshput  -u <user> -s '
f02 = '/usr/local/bin/sshcmd -q -s '
f03 = ' /appl/app/scripts/tools/ConsoleBanner/image/'
f04 = '  -u <user> "mv'
f05 = ' /usr/local/opt/was/was85/systemApps/isclite.ear/isclite.war/images/banner-swoosh.png'
f06 = ' /usr/local/opt/was/was85/systemApps/isclite.ear/isclite.war/images/loginBkgd.jpg'
f07 = ' /usr/local/opt/was/was85/systemApps/isclite.ear/isclite.war/images/'
f08 = '" 2>/dev/null'
f11 = "prod"
f21 = "test"
f31 = "idle"

### mail Ids ###
Iid = "<Name/ID>"
Mid = "xyz@abc.com"
Ccid = "xyz@abc.com"
Subid = "Websphere console banner Updated"

##### Color code ######
GS="\033[0;32m "
GE=" \033[0m"
RE="\033[0;31m"
GY="\033[0;33m"


def Prod_Image_Place(nodeName):
    try:
        now = time.ctime()
        ptime = time.strptime(now)
        cntime = time.strftime("%Y%m%d_%H%M%S", ptime)
    except:
        print( RE + "Script is failing to get system time." + GE )
    f001 = f02 + nodeName + f04 + f05 + f05 + "_B4_" + cntime + f08
    f002 = f02 + nodeName + f04 + f06 + f06 + "_B4_" + cntime + f08
    f003 = f01 + nodeName + f03 + f1BName + f05
    f004 = f01 + nodeName + f03 + f1LName + f06
    try:
        p = Popen(f001, shell=True, stdin=PIPE, stdout=PIPE, stderr=STDOUT, close_fds=True)
        output = p.stdout.read()
        print(output)
        p = Popen(f002, shell=True, stdin=PIPE, stdout=PIPE, stderr=STDOUT, close_fds=True)
        output = p.stdout.read()
        print(output)
        p = Popen(f003, shell=True, stdin=PIPE, stdout=PIPE, stderr=STDOUT, close_fds=True)
        output = p.stdout.read()
        print(output)
        p = Popen(f004, shell=True, stdin=PIPE, stdout=PIPE, stderr=STDOUT, close_fds=True)
        output = p.stdout.read()
        print(output)
    except:
        print(RE + "Error :: " + output + GE )

def Test_Image_Place(nodeName):
    try:
        now = time.ctime()
        ptime = time.strptime(now)
        cntime = time.strftime("%Y%m%d_%H%M%S", ptime)
    except:
        print(RE + "Script is failing to get system time." + GE)
    f001 = f02 + nodeName + f04 + f05 + f05 + "_B4_" + cntime + f08
    f002 = f02 + nodeName + f04 + f06 + f06 + "_B4_" + cntime + f08
    f003 = f01 + nodeName + f03 + f2BName + f05
    f004 = f01 + nodeName + f03 + f2LName + f06
    try:
        p = Popen(f001, shell=True, stdin=PIPE, stdout=PIPE, stderr=STDOUT, close_fds=True)
        output = p.stdout.read()
        print(output)
        p = Popen(f002, shell=True, stdin=PIPE, stdout=PIPE, stderr=STDOUT, close_fds=True)
        output = p.stdout.read()
        print(output)
        p = Popen(f003, shell=True, stdin=PIPE, stdout=PIPE, stderr=STDOUT, close_fds=True)
        output = p.stdout.read()
        print(output)
        p = Popen(f004, shell=True, stdin=PIPE, stdout=PIPE, stderr=STDOUT, close_fds=True)
        output = p.stdout.read()
        print(output)
    except:
        print(RE + "Error :: " + output + GE )

def Idle_Image_Place(nodeName):
    try:
        now = time.ctime()
        ptime = time.strptime(now)
        cntime = time.strftime("%Y%m%d_%H%M%S", ptime)
    except:
        print(RE + "Script is failing to get system time." + GE)
    f001 = f02 + nodeName + f04 + f05 + f05 + "_B4_" + cntime + f08
    f002 = f02 + nodeName + f04 + f06 + f06 + "_B4_" + cntime + f08
    f003 = f01 + nodeName + f03 + f3BName + f05
    f004 = f01 + nodeName + f03 + f3LName + f06
    try:
        p = Popen(f001, shell=True, stdin=PIPE, stdout=PIPE, stderr=STDOUT, close_fds=True)
        output = p.stdout.read()
        print(output)
        p = Popen(f002, shell=True, stdin=PIPE, stdout=PIPE, stderr=STDOUT, close_fds=True)
        output = p.stdout.read()
        print(output)
        p = Popen(f003, shell=True, stdin=PIPE, stdout=PIPE, stderr=STDOUT, close_fds=True)
        output = p.stdout.read()
        print(output)
        p = Popen(f004, shell=True, stdin=PIPE, stdout=PIPE, stderr=STDOUT, close_fds=True)
        output = p.stdout.read()
        print(output)
    except:
        print(RE + "Error :: " + output + GE )

def Logs_Id(type, nodes):
    now = time.ctime()
    ptime = time.strptime(now)
    cntime = time.strftime("[%d/%m/%Y %H:%M:%S CST]", ptime)
    rec_logs = cntime + ":: " + attId + " updated the banner for " + type + "  in Dmgr machine :: " + "," .join(nodes) + "."
    return rec_logs

def Mail_logs(Iid, Ccid, Mid, Subid):
    try:
        msg = MIMEText(textfile, 'plain')
        msg['Subject'] = Subid
        msg['To'] = Iid
        msg['From'] = Mid
        msg['CC'] = Ccid
        Yid = [Iid] + [Ccid]
        s =smtplib.SMTP('localhost')
        s.sendmail(Mid, Yid, msg.as_string())
        s.quit()
    except:
        print(RE + "Error: unable to send email." + GE)

if(loginName == "websphe"):
    type = raw_input(GY + "Please provide the type of DMGR. [prod/test/idle(for idle prod)]:: " + GE)
    type = type.strip()
    nodeN = raw_input(GY + "Please provide the DMGR FQDN name to update banner.:: " + GE)
    nodes = nodeN.split('|')
 #   nodeNames = nodes.strip()
    try:
        if (type == "prod"):
            if (localHost == "<hostname>"):
                for nodeName in nodes:
                    Prod_Image_Place(nodeName)
            elif (localHost == "<hostname>"):
                for nodeName in nodes:
                    Prod_Image_Place(nodeName)
            else:
                print(RE + "The local host(" + localHost + ") is not the production machine. Existing the script." + GE)
        elif (type == "test"):
            if (localHost == "<hostname>"):
                for nodeName in nodes:
                    nodeName = nodeName.strip()
                    Test_Image_Place(nodeName)
            else:
                print( RE + "Please run the script from the machine <hostname>. " + GE)
        elif (type == "idle"):
            if (localHost == "<hostname>"):
                for nodeName in nodes:
                    Idle_Image_Place(nodeName)
            elif (localHost == "<hostname>"):
                for nodeName in nodes:
                    Idle_Image_Place(nodeName)
            else:
                print(RE + "The local host(" + localHost + ") is not the production machine. Existing the script." + GE)
        else:
            print(GY + "Please provide the valid type from [prod/test/idle]" + GE)
    except:
        print(RE + "Error : Invalid input provided." +GE)

    textfile = Logs_Id(type, nodes)
    Logs_Id(type, nodeN)
    Mail_logs(Iid, Ccid, Mid, Subid)
else:
    print(RE + "You login with user " + loginName + " please use <user> to run the script." + GE)