str_list = ["Tutorialspoint","","Welcomes","","Everyone",""]

print("The given list of strings is")
print(str_list)

print("Removing the empty spaces")
updated_list = list(filter(None, str_list))
print(updated_list)
