#!/usr/bin/python2

import os
import time
import sys
import commands


tmp = open("nn", "r")
nnip = tmp.readline()
nnip = nnip.strip()
nnport = tmp.readline()
nnport = nnport.strip()
tmp.close()

dndir = "/data"


def auto_dn():
    global dndir
    global nnport
    global nnip
    st1=make_core(nnip, nnport)
    st2=make_hdfs(dndir)
    f1 = open("hdfs-site.xml", "w")
    f1.write(st1)
    f2 = open("core-site.xml", "w")
    f2.write(st2)
    f1.close()
    f2.close()
    print "The datanode config files have been generated. "
    print "datanode dir  : " + dndir
    print "namenode ip   : " + nnip
    print "namenode port : " + nnport
    print "Press Any key to copy it to the selected datanodes "
    tmp = open("dn", "r")
    dnlist = tmp.readlines()
    for dnip in dnlist:
        dnip = dnip.strip()
        print "copying hdfs-site.xml ##comment this later ##"
        print "sshpass -p \"redhat\" scp -o \"StrictHostKeyChecking no\" hdfs-site.xml root@" + dnip + ":/etc/hadoop/ "
        os.system("sshpass -p \"redhat\" scp -o \"StrictHostKeyChecking no\" hdfs-site.xml root@" + dnip + ":/etc/hadoop/ ")
        l = raw_input("press any key to copy core file ")
        print "sshpass -p \"redhat\" scp -o \"StrictHostKeyChecking no\" core-site.xml root@" + dnip + ":/etc/hadoop/ "
        os.system("sshpass -p \"redhat\" scp -o \"StrictHostKeyChecking no\" core-site.xml root@" + dnip + ":/etc/hadoop/ ")
        print "Files successfully copied into target system. DataNode configured at " + dnip
    tmp.close()


def dn_menu():
    global dndir
    global nnip
    global nnport
    while True:
        os.system("clear")
        print """
\t\t\t###########################\n
\t\t\t# Data Node Configuration #\n
\t\t\t###########################\n
"""
        print """
\t\t 1. Manually Configure Datanode\n
\t\t 2. Automatically Configure Datanode\n
"""
        ch = raw_input("\t Enter Your Choice : ")

        if int(ch) == 1:
            dndir = raw_input("\tName for the data node directory          : ")
            print "Directory with the name " + dndir + "will be created "
            st1 = make_hdfs(dndir)
            st2 = make_core(nnip, nnport)
            f1 = open("hdfs-site.xml", "w")
            f1.write(st1)
            f2 = open("core-site.xml", "w")
            f2.write(st2)
            f1.close()
            f2.close()
            print "The config files for data nodes is ready "
            print "DataNode directory " + dndir
            print "Namenode ip in core-site" + nnip
            print "NameNode port in core-site " + nnport
            print "Press Any Key to copy the datanode files "
            tmpp = open("dn", "r")
            dnlist = tmpp.readlines()
            for dnip in dnlist:
                dnip = dnip.strip()
                print "copying hdfs-site.xml ##comment this later ##"
                print "sshpass -p \"redhat\" scp -o \"StrictHostKeyChecking no\" hdfs-site.xml root@" + dnip + ":/etc/hadoop/ "
                os.system("sshpass -p \"redhat\" scp -o \"StrictHostKeyChecking no\" hdfs-site.xml root@" + dnip + ":/etc/hadoop/ ")
                l = raw_input("enter any key to copy core-site ")
                print "sshpass -p \"redhat\" scp -o \"StrictHostKeyChecking no\" core-site.xml root@" + dnip + ":/etc/hadoop/ "
                os.system("sshpass -p \"redhat\" scp -o \"StrictHostKeyChecking no\" core-site.xml root@" + dnip + ":/etc/hadoop/ ")
                print "Datanode ready at :  " + dnip

        elif int(ch) == 2:
            print " Automatically configuring the DataNode"
            auto_dn()
            print "configured DNs"
            break  # cccccc
        else:
            print " Enter A valid option (1-2) "
            time.sleep(2)
            continue


def make_hdfs(dndir):
    s = """
<?xml version="1.0"?>
<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>

<!-- Put site-specific property overrides in this file. -->

<configuration>

<property>
<name>dfs.data.dir</name>
<value>/""" + dndir + """</value>
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
    return s.strip()





'''
def main():
    nn_menu()


if __name__ == "__main__": main()

# def nn_config():
'''
