list1={"python":50, "web":30, "c":20, "java":40}
list2=[]
first=int(input("Please enter the start number: "))
last=int(input("Please enter the end number: "))
for key,value in list1.items():
    if value >= first and value <= last:
        list2.append(key)
output= ','.join(list2)
print("You can purchase these books (" + output + ")")
