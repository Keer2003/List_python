import os
var=input("Enter ip address:")
print(var)
cmdstring=os.popen("ping "+var).read()
if "Reply from" in cmdstring:
    print("Ip address:"+var+"is active")
