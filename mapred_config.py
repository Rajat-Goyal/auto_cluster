#!/usr/bin/python2

import os
import time
import commands
import sys

tmp = open("jt", "r")
jtip = tmp.readline()
jtip = jtip.strip()
jtport = "9002"
tmp.close()


def auto_mr():
    global jtip
    global jtport

    tmp = open("jt", "r")
    jtip = tmp.readline()
    jtip = jtip.strip()
    tmp.close()

    print " The ip of jobtacker is  :  " + jtip
    print " the port for the jobtracker is  : " + jtport
    st1 = make_mapred(jtip, jtport)
    f1 = open("mapred-site.xml", "w")
    f1.write(st1)
    f1.close()

    copy_into_jt(jtip)
    copy_into_tt()
    print "automatically configured jt and tt "
    ddd = raw_input ("Enter any key  ")


def mr_menu():
    global jtip
    global jtport
    while True:
        os.system("clear")
        print """
\t\t\t################################################\n
\t\t\t#   Job Tracker - Task Tracker Configuration   #\n
\t\t\t################################################\n
"""
        print """
\t\t 1. Manually Configure JobTracker TaskTracker\n
\t\t 2. Automatically Configure JobTracker TaskTracker \n
"""
        ch = raw_input("\t Enter Your Choice : ")

        if int(ch) == 1:
            jtport = raw_input("Enter the port number for the job Tracker (default=9002)")
            if jtport is "":
                jtport = "9002"
                print "user did not specify any port . Using defautl port : " + jtport
            tmp = open("jt", "r")
            jtip = tmp.readline()
            jtip = jtip.strip()
            tmp.close()
            st1 = make_mapred(jtip, jtport)
            f1 = open("mapred-site.xml", "w+")
            f1.write(st1)
            f1.close()

            print "The mapred-site.xml file is ready.Press any key to copy it to selected jobtracker and task trackers"
            print "copyting into jt "
            copy_into_jt(jtip)
            print "copying into tt"
            copy_into_tt()
            print "configured tasktrackers and jobtrackers"
            ddd = raw_input ("Enter any key  ")
            break
        elif int(ch) == 2:
            auto_mr()
            ddd = raw_input ("Enter any key  ")
            break




def make_mapred(jtip, jtport):
    s = """
<?xml version="1.0"?>
<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>

<!-- Put site-specific property overrides in this file. -->

<configuration>

<property>
<name>mapred.job.tracker</name>
<value>""" + jtip + ":"+jtport+"""</value>
</property>


</configuration>
"""

    tmp = open("jt", "w+")
    tmp.write(jtip+"\n")
    tmp.write(jtport+"\n")
    tmp.close()
    return s.strip()


def copy_into_jt(jtip):
    print "copying mapred-site.xml into jobtracker ##comment this later ##"
    print "sshpass -p \"redhat\" scp -o \"StrictHostKeyChecking no\" mapred-site.xml root@" + jtip + ":/etc/hadoop/ "
    os.system("sshpass -p \"redhat\" scp -o \"StrictHostKeyChecking no\" mapred-site.xml root@" + jtip + ":/etc/hadoop/ ")

    print "copying core-site.xml into jobtracker ##comment this later ##"
    print "sshpass -p \"redhat\" scp -o \"StrictHostKeyChecking no\" core-site.xml root@" + jtip + ":/etc/hadoop/ "
    os.system("sshpass -p \"redhat\" scp -o \"StrictHostKeyChecking no\" core-site.xml root@" + jtip + ":/etc/hadoop/ ")
    ddd = raw_input ("Enter any key  ")


def copy_into_tt():
    tmp = open("tt", "r")
    ttlist = tmp.readlines()
    for ttip in ttlist:
        ttip = ttip.strip()
        print "copying mapred-site.xml ##comment this later ##"
        print "sshpass -p \"redhat\" scp -o \"StrictHostKeyChecking no\" mapred-site.xml root@" + ttip + ":/etc/hadoop/ "
        os.system("sshpass -p \"redhat\" scp -o \"StrictHostKeyChecking no\" mapred-site.xml root@" + ttip + ":/etc/hadoop/ ")
        print "tasktracker ready at :  " + ttip
    tmp.close()
    ddd = raw_input ("Enter any key  ")




