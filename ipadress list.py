iplist=['10.213.163.53','10.213.162.41','10.213.163.25','10.213.161.3','10.213.161.46']
templist=[]
for eitem in iplist:
    if eitem.split('.')[2]=='163':
        print(eitem)
        templist.append(eitem)
print("result list is:",templist)        
