list1=[{"name": "Srinivas", "number": "816", "email": "srinivas@gmail.com"}]
while True:
    print("a) Display contact by name")
    print("b) Display contact by number")
    print("c) Edit contact by name")
    print("d) Exit")

    entry=str(input("Please enter your choice: "))
    if entry== 'a':
        i1=(input("Please enter the name: "))
        print(next(item for item in list1 if item["name"] == i1))
    elif entry== 'b':
        i2=(input("Please enter the number: "))
        print(next(item for item in list1 if item["number"] == i2))
    elif entry== 'c':
        i3=input("Please enter the contact name you want to edit: ")
        for item in list1:
            if item["name"]==i3:
                item["number"]=input("Please enter the new contact number: ")
        print(list1)
    elif entry== 'd':
        break
