#!/usr/bin/python2 

import os
import sys
import commands
import time

nnport = "9001"
nndir = "/name"
tmp = open("nn", "r")
nnip = tmp.readline()
nnip = nnip.strip()
tmp.close()


def auto_nn():
    global nndir
    global nnport
    global nnip
    tmp = open("nn", "r")
    nnip = tmp.readline()
    nnip = nnip.strip()
    tmp.close()
    st1 = make_core(nnip, nnport)
    st2 = make_hdfs(nndir)
    f1 = open("hdfs-site.xml", "w")
    f1.write(st1)
    f2 = open("core-site.xml", "w")
    f2.write(st2)
    f1.close()
    f2.close()
    print "The namenode config files have been generated. "
    print "datanode dir  : " + nndir
    print "namenode ip   : " + nnip
    print "namenode port : " + nnport
    print "Press Any key to copy it to the selected namenodes "
    print "sshpass -p \"redhat\" scp -o \"StrictHostKeyChecking no\" hdfs-site.xml root@" + nnip + ":/etc/hadoop/ "
    os.system("sshpass -p \"redhat\" scp -o \"StrictHostKeyChecking no\" hdfs-site.xml root@" + nnip + ":/etc/hadoop/ ")
    #l = raw_input()
    print "sshpass -p \"redhat\" scp -o \"StrictHostKeyChecking no\" core-site.xml root@" + nnip + ":/etc/hadoop/ "
    os.system("sshpass -p \"redhat\" scp -o \"StrictHostKeyChecking no\" core-site.xml root@" + nnip + ":/etc/hadoop/ ")
    print "Files successfully copied into target system. NameNode configured at " + nnip
    ddd = raw_input ("Enter any key  ")


def nn_menu():
    global nnip
    global nndir
    global nnport
    while True:
        os.system("clear")
        print """
\t\t\t###########################\n
\t\t\t# Name Node Configuration #\n
\t\t\t###########################\n
"""
        print """
\t\t 1. Configure a fresh namenode(Manual)\n
\t\t 2. Configure a fresh namenode(Automatic)\n
\t\t 3. Update an existing namenode configuration.(under Devolopment)\n
"""
        ch = raw_input("\t Enter Your Choice : ")

        if int(ch) == 1:
            nndir = raw_input("\tName for the name node directory          : ")
            nnport = raw_input("\tPort number for namenode (default=9001)   : ")
            if nnport is "":
                nnport = "9001"
                print "user did not specify any port . Using defautl port : " + nnport
            print "Directory with the name " + nndir + "will be created and formatted "
            st1 = make_hdfs(nndir)
            st2 = make_core(nnip, nnport)
            f1 = open("hdfs-site.xml", "w")
            f1.write(st1)
            f2 = open("core-site.xml", "w")
            f2.write(st2)
            f1.close()
            f2.close()
            print "sshpass -p \"redhat\" scp -o \"StrictHostKeyChecking no\" hdfs-site.xml root@" + nnip + ":/etc/hadoop/ "
            os.system("sshpass -p \"redhat\" scp -o \"StrictHostKeyChecking no\" hdfs-site.xml root@" + nnip + ":/etc/hadoop/ ")
            #l = raw_input()
            print "sshpass -p \"redhat\" scp -o \"StrictHostKeyChecking no\" core-site.xml root@" + nnip + ":/etc/hadoop/ "
            os.system("sshpass -p \"redhat\" scp -o \"StrictHostKeyChecking no\" core-site.xml root@" + nnip + ":/etc/hadoop/ ")
            ddd = raw_input ("Enter any key  ")
            break
        elif int(ch) == 2:
            auto_nn()
            ddd = raw_input ("Enter any key  ")
            break
        elif int(ch) == 3:
            print "This feature is still under progress. Please wait for the next update"
            ddd = raw_input ("Enter any key  ")
            break  # cccccc
        else:
            print "Enter A valid option (1-3) "
            time.sleep(2)
            continue


def make_hdfs(nndir):
    s = """
<?xml version="1.0"?>
<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>

<!-- Put site-specific property overrides in this file. -->

<configuration>

<property>
<name>dfs.name.dir</name>
<value>/""" + nndir + """</value>
</property>


</configuration>
"""
    return s.strip()


def make_core(nnip, nnport):
    s = """
<?xml version="1.0"?>
<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>

<!-- Put site-specific property overrides in this file. -->

<configuration>

<property>
<name>fs.default.name</name>
<value>hdfs://""" + nnip + """:""" + nnport + """</value>
</property>


</configuration>
"""
    tmp = open("nn", "w+")
    tmp.write(nnip+"\n")
    tmp.write(nnport+"\n")
    tmp.close()
    return s.strip()


'''

def main():
    nn_menu()


if __name__ == "__main__": main()

# def nn_config():
'''