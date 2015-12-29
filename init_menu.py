#!/usr/bin/python2 

import time 
import os 
import commands 
import sys 

def init_menu(): 
	os.system("clear")
	print """
		\t\t\t#####################################\n
		\t\t\t#      Welcome to Auto-Cluster      #\n
		\t\t\t#####################################\n
		"""	
	time.sleep(2)
	flag = 0 
	while(flag == 0):
		os.system("clear")  
		
		print """
			\t\t\t#####################################\n
			\t\t\t#          Cluster Option           #\n
			\t\t\t#####################################\n
			"""
		print "\n"
		print """\n
			\t\t\t 1. Single Node Cluster \n
			\t\t\t 2. Multi-Node Cluster \n 
			""" 
		
		ch = raw_input("\t Enter your Choice : ")
		if int(ch)==1 : 
			cnf = raw_input("\t\t Press Enter to proceed making a Single Node Cluster. Press n to clear selection :")
			mode = 1 
		elif int(ch)==2 : 
			cnf = raw_input("\t\t Press Enter to proceed making a Multinode Cluster Press n to clear selection : ")
			mode = 2 
		if cnf is "n":
			continue;
		else:
			break;
	return mode 
		

def main():
	cluster_type = init_menu() 
	ch = raw_input()

if __name__ == "__main__" : main() 
