#!/usr/bin/python2
##########################################################################
##		TO SCAN THE NETWORK 
#####################################################################
import os 
import sys
import commands 

myip  = sys.argv[1]


def scan_now():
	rng = raw_input ("\t Enter the range of IPs you want to scan in the format of IP/NETMASK (default = 192.168.0.0/24 )")
	if rng is "" :
		rng = "192.168.0.0/24"  
	os.system("nmap " + rng  + " -oG crap.txt")
	os.system('cat crap.txt | grep ssh | cut -f2 -d" " > iplist.txt')
 	fobj = open("iplist.txt","rw+")
	os.system("mkdir reports")
	lis = fobj.readlines()
	for ip in lis: 
		ip = ip.strip()
		print "going inside " + ip
		os.system('sshpass -p "redhat" scp -o "StrictHostKeyChecking no" sendreport.py root@'+ip+ ':/')
		os.system("touch reports/" + ip ) 
		os.system('sshpass -p "redhat" ssh -o "StrictHostKeyChecking no" root@'+ip+ " 'python2 /sendreport.py "+ip+" "+myip+" ; cat "+ip+" ' > reports/"+ip)	


def main():
	scan_now() 

if __name__ == "__main__" : main() 
