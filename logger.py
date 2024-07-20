import traceback
import logging
import time
#Logging handler
logger=logging.getLogger("Exception2")
logger.selfLevel(logging.DEBUG)

fh=logging.FileHandler("Exception2.log")
fh.selfLevel(logging.DEBUG)

fmtr=logging.Formatter("%casctime)s[levelnames)s]%(message)s",detefmt="%m%d%y%1:%m:%s%p")
fh.setFormatter(fmtr)
print(fh)
logger.addHeader(fh)
#Exception handling
while True:
    try:
        n=input("please enter an integer:")
        n=int(n)
        logger.info("successfull entered %s",n)
        break
    except Exception as e:
        #print e
        print(traceback.format_exc())
        logger.error("Throughs Exception %s",e)
        #print("no valid integer please try again...")
print("Great,you successfully entered an integer")        
