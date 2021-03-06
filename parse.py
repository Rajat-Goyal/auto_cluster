#!/usr/bin/python2 

import os
import sys
import commands
import re
import operator
import math

mean_ram=0.0
mean_hdd = 0.0
mean_core = 0.0
mean_mhz = 0.0
free_ram = {}
free_hdd = {}
cpu_core = {}
cpu_mhz = {}


def parser():
    pwd = commands.getoutput("echo $PWD")
    print pwd
    li = os.listdir(pwd + "/reports/")
    print "List of Active IPs from which the result was gathered "
    global free_ram
    global free_hdd
    global cpu_core
    global cpu_mhz

    global mean_ram
    global mean_hdd
    global mean_core
    global mean_mhz

    valid = open(pwd + "/valid_ip.txt", "w+")
    for ip in li:
        if os.stat(pwd + "/reports/" + ip).st_size != 0:
            print ip
            valid.write(ip + "\n")
            ff = open(pwd + "/reports/" + ip, "r")
            l = ff.readline()
            x = re.split(r' +', l)[3]
            free_ram[ip] = int(x)

            l = ff.readline()
            x = l.split()
            x = x[3]
            x = x[0:-1]
            print float(x)
            free_hdd[ip] = float(x)

            l = ff.readline()
            l = l.strip()
            x = re.split(r' +', l)[1]
            cpu_core[ip] = int(x)

            l = ff.readline()
            l = l.strip()
            x = re.split(r' +', l)[2]
            cpu_mhz[ip] = float(x)

    valid.close()
    raw_input("\nPress any key to continue ...")
    print "\nSYSTEM CONFIGURATION OF WORKING IP(s)\n"
    for key1, value1 in free_ram.iteritems():
        print key1 + " : ", value1

    raw_input("\nPress any key to continue ...\n")

    print free_ram
    print free_hdd
    print cpu_core
    print cpu_mhz

    mean_values()
    raw_input("\nPress any key to continue ...\n")

    print " mean ram : ", mean_ram
    print " mean hdd : ", mean_hdd
    print " mean cores : ", mean_core
    print " mean mean MHz : ", mean_mhz


    raw_input("\nPress any key to continue ...\n")
    mean_ram = mean_hdd = mean_core = mean_mhz = 0


def mean_values():
    c = r = 0
    for x in free_ram.values():
        r += x
        c += 1
    global mean_ram
    mean_ram = (1.0 * r) / c
    c = r = 0
    for x in free_hdd.values():
        r += x
        c += 1
    global mean_hdd
    mean_hdd = (1.0 * r) / c
    c = r = 0
    for x in cpu_core.values():
        r += x
        c += 1
    global mean_core
    mean_core = math.ceil((1.0 * r) / c)
    c = r = 0
    for x in cpu_mhz.values():
        r += x
        c += 1
    global mean_mhz
    mean_mhz = math.ceil((1.0 * r) / c)
    print "mean values calculated"



#if __name__ == "__main__" : parser()
