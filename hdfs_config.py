#!/usr/bin/python2

import os
import sys
import commands
import time
import nn_create
import dn_create


def hdfs_menu():
    while True:
        os.system("clear")
        print """
\t\t\t###########################\n
\t\t\t#    HDFS Configuration   #\n
\t\t\t###########################\n
"""
        print """
\t\t 1. Automatically Configure NameNode - DataNode\n
\t\t 2. Manually Configure the NameNode - DataNode.\n
"""
        ch = raw_input("\t Enter Your Choice : ")

        if int(ch) == 1:
            nn_create.auto_nn()
            dn_create.auto_dn()
            break
        elif int(ch) == 2:
            nn_create.nn_menu()
            dn_create.dn_menu()
            break



def main():
    hdfs_menu()

#if __name__ == "__main__" : main()
