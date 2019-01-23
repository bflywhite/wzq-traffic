import random

import dns.resolver
import sys
import time


with open(r'domain.txt','r') as f:
    for line in f:
        domain=line
        try:
            dns.resolver.query(domain,'A')


        except Exception as e:
            print e
    # # except KeyboardInterrupt as e:
    #     print "bye~~"

