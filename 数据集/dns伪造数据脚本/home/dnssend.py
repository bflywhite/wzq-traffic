import random

import dns.resolver
import sys
import time

domain = sys.argv[1]
try:
    start = sys.argv[2]
except:
    start = 60
try:
    end = sys.argv[3]
except:
    end = 60
if(int(end)-int(start)<0):
    print "eg:python DNS.py www.test.com 50 60"
    exit()
try:
        dns.resolver.query(domain,'A')
        
       
except Exception as e:
        print e
except KeyboardInterrupt as e:
        print "bye~~"

