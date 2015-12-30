#!/usr/bin/python2 

import os 
import sys 
import commands 

nnport = "9001"
nndir = "/name"
nnip = sys.argv[1]

def nn_menu():
	while(True):
		os.system("clear")
		print """ 
			  \t\t\t###########################\n
			  \t\t\t# Name Node Configuration #\n 
			  \t\t\t###########################\n
			"""
		print """
			 \t\t 1. Configure a fresh namenode\n 
	 		 \t\t 2. Update an existing namenode configuration.\n 
			"""
		ch = raw_input("\t Enter Your Choice : " )
		
		if int(ch)==1:
			nnip = raw_input("\tEnter the  ip for namenode                : " ) 
			nndir = raw_input("\tName for the name node directory         : " )
			nnport = raw_input("\tPort number for namenode (default=9001) : " )
			if nnport is "":
				nnport = "9001"
				print "user did not specify any port . Using defautl port : " + nnport 
			print "Directory with the name "+ nndir + "will be created and formatted "
			st1 = make_hdfs(nndir)
			st2 = make_core(nnip,nnport)
			f1 = open("hdfs-site.xml","w")
			f1.write(st1)
			f2 = open("core-site.xml","w")
			f2.write(st2)
			f1.close()
			f2.close()
			print "sshpass -p \"redhat\" scp -o \"StrictHostKeyChecking no\" hdfs-site.xml root@" + nnip + ":/etc/hadoop/ "		
			os.system("sshpass -p \"redhat\" scp -o \"StrictHostKeyChecking no\" hdfs-site.xml root@" + nnip + ":/etc/hadoop/ ")
			l = raw_input()
			print "sshpass -p \"redhat\" scp -o \"StrictHostKeyChecking no\" core-site.xml root@" + nnip + ":/etc/hadoop/ "		
			os.system("sshpass -p \"redhat\" scp -o \"StrictHostKeyChecking no\" core-site.xml root@" + nnip + ":/etc/hadoop/ ")
				
		elif int(ch)==2 :
			break;#cccccc 
		else: 
			print "Enter A valid option (1-3) " 
			sleep(2)
			continue;

def make_hdfs(nndir):
	s="""
<?xml version="1.0"?>
<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>

<!-- Put site-specific property overrides in this file. -->

<configuration>

<property>
<name>dfs.name.dir</name>
<value>/"""+nndir+"""</value>
</property>


</configuration>
"""
	return s.strip()


def make_core(nnip,nnport):
	s = """
<?xml version="1.0"?>
<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>

<!-- Put site-specific property overrides in this file. -->

<configuration>

<property>
<name>fs.default.name</name>
<value>hdfs://"""+nnip+""":"""+nnport+"""</value>
</property>


</configuration>
"""
	return s.strip()


def main():
	nn_menu()

if __name__ == "__main__" : main() 

#def nn_config():
	 
	
