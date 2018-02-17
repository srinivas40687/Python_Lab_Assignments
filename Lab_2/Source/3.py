class Person:
    def _init_(self,name,email):
        self.name = name
        self.email = email
    def display(self):
        print("Name: ", self.name)
        print("Email: ", self.email)
class Student(Person):
    StudentCount = 0
    def _init_(self,name,email,student_id):
        Person._init_(self,name,email)
        self.student_id = student_id
        Student.StudentCount +=1
    def displayCount(self):
        print("Total Students:", Student.StudentCount)
    def display(self):
        print("Student Details:")
        Person.display(self)
        print("Student Id: ",self.student_id)
class Librarian(Person):
    StudentCount = 0
    def _init_(self,name,email,employee_id):
        super()._init_(name,email)
        self.employee_id = employee_id
    def display(self):
        print("Employee Details:")
        Person.display(self)
        print("Employee Id: ",self.employee_id)
class Book():
    def _init_(self, bookname, author, book_id):
        self.book_name = bookname
        self.author = author
        self.book_id = book_id
    def display(self):
        print("Book Details")
        print("BookName: ", self.book_name)
        print("Author: ", self.author)
        print("BookID: ", self.book_id)
class BookCheckout(Student,Book):
    def _init_(self, name, email, student_id, bookname, author, book_id):
        Student._init_(self,name,email,student_id)
        Book._init_(self, bookname, author, book_id)
    def display(self):
        print("Book details: ")
        Student.display(self)
        Book.display(self)
samplelist= []
samplelist.append(Student('Srini', 'abc@gmail.com', 1234))
samplelist.append(Student('Sampath', 'def@mail,umkc.edu', 5678))
samplelist.append(Librarian('Sriram', 'ghi@gmail.com', 1357))
samplelist.append(Librarian('Dinesh', 'jkl@gmail.com', 9987))
samplelist.append(Book('FOOTBALL', 'J.K ROWLING', 1937492))
samplelist.append(Book('BADMINTON', 'MON0POLY', 938493))
samplelist.append(BookCheckout('CRICKET', 'Triplets', 8328))
for obj, a in enumerate(samplelist):
    a.display()
    print("\n")
    if obj == len(samplelist)-1:
        a.displayCount()
