# -*- coding: utf-8 -*-
"""
Created on 9/8/2020

@author: Thomas Beha
"""

from cryptography.fernet import Fernet
import getpass
from lxml import etree 

uname = input("Username: ")
password = getpass.getpass()
logfile = input("Logfile: ")
ovc = input("OVC IP Addr: ")
fname = input("Filename: ")

keyfile=fname+'.key'
xmlfile=fname+'.xml'
key = Fernet.generate_key()
k1 = key.decode('ASCII')
f = open(keyfile,'w')
f.write(key.decode('ASCII'))
f.close()

f = Fernet(key)
token = f.encrypt(password.encode('ASCII'))
user = f.encrypt(uname.encode('ASCII'))

root = etree.Element("data")
etree.SubElement(root,"username").text=uname
etree.SubElement(root,"user").text=user
etree.SubElement(root,"password").text=token
etree.SubElement(root,"ovc").text=ovc
etree.SubElement(root,"logfile").text=logfile
xmloutput = etree.tostring(root, pretty_print=True)
f = open(xmlfile,'w')
f.write(xmloutput.decode('ASCII'))
f.close()

""" Test the keys """ 
""" Read keyfile """
f = open(keyfile, 'r')
k2=f.readline()
f.close()
key2=k2.encode('ASCII')

""" Parse XML File """

tree = etree.parse(xmlfile)
u2=(tree.find("user")).text
p2=(tree.find("password")).text


f = Fernet(key2)
user = f.decrypt(u2.encode('ASCII')).decode('ASCII')
password = f.decrypt(p2.encode('ASCII')).decode('ASCII')
print(user,password)