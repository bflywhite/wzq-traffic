import requests
import time
import re
domains=[]
for i in range(2,20):
        url='http://alexa.chinaz.com/Category/index_Business_{}.html'.format(i)
        # //http://alexa.chinaz.com/Category/index_Business_2.html
        print(url)
        while 1:
            try:
                res=requests.get(url,timeout=3)
                break
            except:
                pass
        urls=re.findall(r'<a href=".*?domain=(.*?)"',res.text)
        domains.extend(urls)

    # print(res.text)
print(domains)
with open(r'domain.txt','a+') as f:
    for i in domains:
        f.write(i+'\n')
