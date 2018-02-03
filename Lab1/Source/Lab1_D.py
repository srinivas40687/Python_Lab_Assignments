#Students who are attending python class are stored in List1:
List_1 = ['Srinivas', 'Kranthi', 'Avinash', 'Sireesha', 'Dinesh', 'Sudheer', 'Pujita']

#Students who are attending Web_Application class are stored in List2:
List_2 = ['Srinivas', 'Girish', 'Dinesh', 'Pujita', 'Prudhvi', 'Sireesha', 'Avinash', 'Yeshwanth', 'Prabha']


print("Students who are attending both python and web_aaplication classes are: \n")

for A in List_1:             #Here A is a student in List1
    if A in List_2:          #This checks if the same student is present in the List2, If Yes prints the student
        print(A)
print('\n')


print("Students who are not common in both the python and web_application classes are: \n")

for B in List_1:             #Here B is a student in List1
    if B not in List_2:      #This checks if the same student is present in the List2, If No prints the student
        print(B)


for C in List_2:             #Here C is a student in List2
    if C not in List_1:      #This checks if the same student is present in the List1, If No prints the student
        print(C)