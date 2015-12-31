#!#!/usr/bin/python2

import os
import sys
import commands
import time
import tt_create
import jt_create


def hdfs_menu():
    while True:
        os.system("clear")
        print """
\t\t\t#############################\n
\t\t\t#    MapRed Configuration   #\n
\t\t\t#############################\n
"""
        print """
\t\t 1. Automatically Configure Job Tracker\n
\t\t 2. Manually Configure the Task Tracker.\n
"""
        ch = raw_input("\t Enter Your Choice : ")

        if int(ch) == 1:
            jt_create.auto_jt()
            tt_create.auto_tt()
        elif int(ch) == 2:
            jt_create.jt_menu()
            tt_create.tt_menu()
