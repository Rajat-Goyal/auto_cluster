#!/usr/bin/python2 

import os 
import commands 
import sys 



ip = sys.argv[1] 
dest = sys.argv[2]
fname = ip  

f=open(fname,"w+") 
f.close()
os.system('lscpu | grep "CPU(s):" | head -n 1 > ' + fname )
os.system('df -Th | grep " /" | head -n 1 >> ' + fname ) 
os.system("free -m | grep Mem >> " + fname )  
exit() 

