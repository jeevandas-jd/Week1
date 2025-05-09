import os
import json
class StudentManagement(object):
    def __init__(self):
        self.file="may9/studentData.json"

        self.data=None
        self.studentID=1000
        if os.path.exists(self.file):
            with open(self.file,'r') as json_file:
                self.data=json.load(json_file)
        else:
            self.data={
                "lastStudentID":self.studentID,
                "students":{}
            }
            with open(self.file,"w") as f:
                json.dump(self.data,f,indent=4)
    def addStudent(self):

        studentID=self.data["lastStudentID"]+1
        self.data["lastStudentID"]=studentID
        self.data["students"][studentID]={
            "name":input("Enter your name: "),
            "age":int(input("Enter your age: ")),
            "department":input("Enter your department: "),
        }
        with open(self.file,"w") as f:
            json.dump(self.data,f,indent=4)
        print(f"Student added successfully. Your student ID is {studentID}.")
    def searchStudent(self):
        studentID=int(input("Enter your student ID: "))
        if studentID in self.data["students"]:
            studentDetails=self.data["students"][studentID]
            print(f"Student ID: {studentID}")
            print(f"Name: {studentDetails['name']}")
            print(f"Age: {studentDetails['age']}")
            print(f"Department: {studentDetails['department']}")
        else:
            print("Student not found.")
    def removeStudent(self):
        studentID=input("Enter your student ID: ")
        if studentID in self.data["students"]:
            del self.data["students"][studentID]
            with open(self.file,"w") as f:
                json.dump(self.data,f,indent=4)
            print(f"Student with ID {studentID} removed successfully.")
        else:
            print("Student not found.")
def main():
    sm=StudentManagement()
    while True:
        print("1. Add Student")
        print("2. Search Student")
        print("3. Remove Student")
        print("4. Exit")
        choice=int(input("Enter your choice: "))
        if choice==1:
            sm.addStudent()
        elif choice==2:
            sm.searchStudent()
        elif choice==3:
            sm.removeStudent()
        elif choice==4:
            break
        else:
            print("Invalid choice.")
if __name__=="__main__":
    main()
        

        
        