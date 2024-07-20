import os
filepath=input("Enter the directory path:")
outlist=[ef for ef in os.listdir(filepath) if ef.endswith('.py')]
print(outlist)
