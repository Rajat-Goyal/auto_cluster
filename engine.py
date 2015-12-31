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
    valid = open(pwd + "/valid_ip.txt", "r")
    ips = valid.readlines()
    sno = 0
    print "\t------------------------------------------------------------------------------"
    print "\t SNO \t IP \t\t RAM \t HDD \t CPU(MHz) \t CPU(cores)"
    print "\t------------------------------------------------------------------------------"
    iplist = []
    for ip in ips:
        sno += 1
        ip = ip.strip()
        iplist.append(ip)
        print "\t  ", sno, "\t" + ip + "\t", free_ram[ip], "\t", free_hdd[ip], "\t", (cpu_mhz[ip] + 0.001), "\t  \" ", \
            cpu_core[ip], " \"\t"
    valid.close()


# currently the auth_config just sorts on the basis of ram and harddisk and
# then choses the datanodes and task trackers accordingly
def auto_config():
    no_valid = commands.getoutput("cat valid_ip.txt | wc -l ")
    no_valid = int(no_valid)
    no_dn = int(raw_input(("Enter the number of datanodes you want to make (max = ", no_valid, ")  :  ")))
    while no_valid < no_dn:
        print (no_valid < no_dn)
        no_dn = int(raw_input(("No is not valid.Please Enter a valid number (max = ", no_valid, ")  :  ")))
    no_tt = int(raw_input(("Enter the number of Task Trackers you want to make (max = ", no_valid, ")  :  ")))
    while no_valid < no_tt:
        print (no_valid < no_tt)
        no_tt = int(raw_input(("No is not valid.Please Enter a valid number (max = ", no_valid, ") :  ")))

    sort_ram = sorted(free_ram.items(), key=operator.itemgetter(1))
    sort_ram.reverse()
    sort_hdd = sorted(free_hdd.items(), key=operator.itemgetter(1))
    sort_hdd.reverse()

    # took nntmp and jt tmp for temporary decision as namenode and datanode
    # cannot be one of the data nodes or task tracker node
    # Still needd to consider if no available systems
    # then will have to overlap
    # overlapping of DN and TT is no problem . infact its more efficient

    nntmp = sort_hdd[no_dn][0]
    nnlist = []
    tmp = open("dn", "w+")
    print "Data Nodes Selected  :  "
    for i in range(0, no_dn):
        print "\tData Node ", i + 1, " :  " + sort_hdd[i][0] + "  ", sort_hdd[i][1]
        nnlist.append(sort_hdd[i][0])
        tmp.write(sort_hdd[i][0] + "\n")
    tmp.close()

    jttmp = sort_ram[no_tt][0]
    ttlist = []
    tmp = open("tt", "w+")
    print "Task Trackers Selected  : "
    for i in range(0, no_tt):
        print "\tTask Tracker ", i + 1, "  :  " + sort_ram[i][0] + "  ", sort_ram[i][1]
        ttlist.append(sort_ram[i][0])
        tmp.write(sort_ram[i][0] + "\n")
    tmp.close()
    # the following is done to avoid overlapping of JT with DN and
    # and also avoid overlapping of NN with TT
    # avoiding nn overlap
    i = 1
    while nntmp in ttlist or nntmp is jttmp:
        nntmp = sort_hdd[no_dn + i][0]
        i += 1
    print "Namenode Selected is :  " + nntmp
    tmp = open("nn", "w+")
    tmp.write(nntmp + "\n")
    tmp.close()
    # avoiding jt overlap
    i = 1
    while jttmp in nnlist or jttmp is nntmp:
        jttmp = sort_hdd[no_dn + i][0]
        i += 1

    print "Job Tracker Selected is :  " + jttmp
    tmp = open("jt", "w+")
    tmp.write(jttmp + "\n")
    tmp.close()


def man_config():
    valid = open(pwd + "/valid_ip.txt", "r")
    ips = valid.readlines()
    sno = 0
    print "\t------------------------------------------------------------------------------"
    print "\t SNO \t IP \t\t RAM \t HDD \t CPU(MHz) \t CPU(cores)"
    print "\t------------------------------------------------------------------------------"
    iplist = []
    for ip in ips:
        ip = ip.strip()
        iplist.append(ip)
        print "\t  ", sno, "\t" + ip + "\t", free_ram[ip], "\t", free_hdd[ip], "\t", (cpu_mhz[ip] + 0.001), "\t  \" ", \
            cpu_core[ip], " \"\t"
        sno += 1
        valid.close()

    for_nn = raw_input("Serial number of the system you want to make namenode :   ")
    for_nn = for_nn.split()
    nn_sno = int(for_nn[0])
    nn_ip = iplist[nn_sno]
    print "Name node will be configured on the ip :   " + nn_ip
    nnf = open(pwd + "/nn", "w+")
    nnf.write(nn_ip + "\n")
    nnf.close()

    for_jt = raw_input("Serial number of the system you want to make JobTracker :   ")
    for_jt = for_jt.split()
    jt_sno = int(for_jt[0])
    jt_ip = iplist[jt_sno]
    print "Job Tracker will be configured on the ip :   " + jt_ip
    jtf = open(pwd + "/jt", "w+")
    jtf.write(jt_ip + "\n")
    jtf.close()

    for_dn = raw_input("Serial numbers of the systems you want to make datanode(space seperated)   :  ")
    dn_list = for_dn.split()
    print "The systems with following ips will be configured as datanode"
    dnf = open(pwd + "/dn", "w+")
    for i in range(len(dn_list)):
        tmp = iplist[int(dn_list[i])]
        print "\t" + tmp
        dnf.write(tmp + "\n")
    dnf.close()

    for_tt = raw_input("Serial numbers of the systems you want to make tasktracker.(space seperated) :  ")
    tt_list = for_tt.split()
    print "TaskTracker will be configured on the following machines "
    jtf = open(pwd + "/tt", "w+")
    for i in range(len(tt_list)):
        tmp = iplist[int(tt_list[i])]
        print "\t" + tmp
        jtf.write(tmp + "\n")
    jtf.close()


def main():
    # time.sleep(5)
    l = raw_input("enter any key to continue ====> ")
    while True:
        os.system("clear")
        print ("""
\t\t\t##############################
\t\t\t#    CONFIGURATION MODE      #
\t\t\t##############################

\t\t\t1. Automatic Configuration
\t\t\t2. Manual Configuration
""")
        choice = raw_input("\tEnter Choice ")
        if int(choice) == 1:
            auto_config()
            break
        elif int(choice) == 2:
            man_config()
            break
        else:
            # noinspection PyUnusedLocal
            xx = raw_input("Enter a Valid Option! Press Any Key To Retry ")
            continue

        hdfs_config()
        mapreduce_config()

if __name__ == "__main__": main()
