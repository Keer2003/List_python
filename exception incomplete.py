import traceback
while True:
    try:
        n=input("please enter a integer")
        n=int(n)
        #break
    except Exception as e:
        print(traceback.format_exc())
        #safeprint("through exception "xs",e)
        #longer.error("through exception "xs",e)
        
            

