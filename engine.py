#!/usr/bin/python2

import os 
import math
import sys 
import commands 
import re 
from parse import *
import time 
import commands 

pwd = commands.getoutput("echo $PWD")

def print_list():
	valid = open(pwd+"/valid_ip.txt","r")
        ips = valid.readlines()
        sno = 0
        print "\t------------------------------------------------------------------------------"
        print "\t SNO \t IP \t\t RAM \t HDD \t CPU(MHz) \t CPU(cores)"
        print "\t------------------------------------------------------------------------------"
        iplist =[]
        for ip in ips:
                sno+=1
                ip = ip.strip()
                iplist.append(ip)
                print "\t  ",sno,"\t"+ip+"\t",free_ram[ip],"\t",free_hdd[ip],"\t",(cpu_mhz[ip]+0.001),"\t  \" ",cpu_core[ip]," \"\t"
	valid.close()
	
def auto_config(): 
	no_valid = commands.getoutput("cat valid_ip.txt | wc -l ")
	no_valid = int(no_valid)
	no_dn = int(raw_input(("Enter the number of datanodes you want to make (max = ",no_valid,") :  ") ))
	while (no_valid < no_dn ):
		print (no_valid < no_dn) 
		no_dn=int(raw_input(("No is not valid.Please Enter a valid number (max = " ,no_valid,") :  ")))
		print no_valid
		print no_dn
	
 
def man_config():
	valid = open(pwd+"/valid_ip.txt","r")
	ips = valid.readlines()
	sno = 0 
	print "\t------------------------------------------------------------------------------"
	print "\t SNO \t IP \t\t RAM \t HDD \t CPU(MHz) \t CPU(cores)" 
	print "\t------------------------------------------------------------------------------"
	iplist =[]
	for ip in ips:  
		ip = ip.strip()
		iplist.append(ip)
		print "\t  ",sno,"\t"+ip+"\t",free_ram[ip],"\t",free_hdd[ip],"\t",(cpu_mhz[ip]+0.001),"\t  \" ",cpu_core[ip]," \"\t"
		sno+=1
		valid.close()
	
	for_nn = raw_input("Serial number of the system you want to make namenode :   ")
	for_nn=for_nn.split()	
	nn_sno = int(for_nn[0])
	nn_ip = iplist[nn_sno]
	print "Name node will be configured on the ip :   "+ nn_ip
	nnf = open(pwd+"/nn","w+")
	nnf.write(nn_ip+"\n")
	nnf.close() 

	for_jt = raw_input("Serial number of the system you want to make JobTracker :   ")
	for_jt=for_jt.split()	 
	jt_sno = int(for_jt[0])
	jt_ip = iplist[jt_sno]
	print "Job Tracker will be configured on the ip :   "+ jt_ip
	jtf = open(pwd+"/jt","w+")
	jtf.write(jt_ip+"\n")
	jtf.close() 
	
 
	for_dn = raw_input("Serial numbers of the systems you want to make datanode(space seperated)   :  ")
	dn_list = for_dn.split()
	print "The systems with following ips will be configured as datanode" 
	dnf = open(pwd+"/dn","w+")
	for i in range(len(dn_list)):
		tmp= iplist[int(dn_list[i])]
		print "\t" + tmp		
		dnf.write(tmp+"\n")
	dnf.close()

	for_tt = raw_input("Serial numbers of the systems you want to make tasktracker.(space seperated) :  ")
	tt_list = for_tt.split()
	print "TaskTracker will be configured on the following machines "  
	jtf = open(pwd+"/tt","w+")	
	for i in range(len(tt_list)):
		tmp=iplist[int(tt_list[i])]	
		print "\t" + tmp		
		jtf.write(tmp+"\n")
	jtf.close() 

def main():
	#time.sleep(5)
	l = raw_input("enter any key to continue ====> " )
	while(True):
		os.system("clear")
		print ("""
			##############################
			#    CONFIGURE THE CLUSTER   #
			##############################
	
			1. Automatic Configuration
			2. Manual Configuration 
		
		 """)
		choice=raw_input("\tEnter Choice " )
		if int(choice) == 1 : 
			auto_config()
			break;
		elif int(choice) == 2 : 
			man_config()
			break;
		else: 
			xx = raw_input("Enter a Valid Option! Press Any Key To Retry ")
			continue   
	

if __name__ == "__main__" : main()

