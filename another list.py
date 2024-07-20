import os
import traceback
iplist=['10.213.163.53','192.168.1.28','10.213.163.25','10.213.161.3','10.213.161.46']
actlist,inactlist=[],[]
try:
    for eip in iplist:
        cmdstring='ping % s'%eip
        print(cmdstring)
        var=os.popen(cmdstring).read()
        if 'Reply' in var:
            actlist.append(eip)
        else:
            inactlist.append(eip)
except Exception as e:
    print(e)
print("active iplist:",actlist)
print("inactive iplist:",inactlist)  
