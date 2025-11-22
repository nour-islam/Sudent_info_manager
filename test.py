from fileinput import filename
from os import name
import time
from datetime import datetime

class StudenInfotManager:
    def __init__(self):
        self.students = []
    
    def create_fixed_file(self, filename):
        students_data = [
            {"NAME": "Nour", "AGE": "21", "ID": "1001", "MAJOR": "CS"},
            {"NAME": "MArwan", "AGE": "21", "ID": "1002", "MAJOR": "CS"},
            {"NAME": "Menna", "AGE": "21", "ID": "1003", "MAJOR": "CS"},
            {"NAME": "Nourhan", "AGE": "21", "ID": "1004", "MAJOR": "CS"},
            {"NAME": "Islam", "AGE": "21", "ID": "1005", "MAJOR": "CS"},
        ]
            
        with open(filename, 'w') as f:
            f.write("FILE_TYPE = STUDENT\n")
            f.write("STRUCTURE = FIXED\n")
            f.write("FIELDS = NAME,AGE,ID,MAJOR\n")
            f.write("===DATA===\n")
            
            for student in students_data:
                line = f"{student['NAME']:10}{student['AGE']:3}{student['ID']:6}{student['MAJOR']:8}\n"
                f.write(line)
        
        print(f"file {filename} created successfully")
    
    def create_delimited_file(self, filename):
        students_data = [
            {"NAME": "Nour", "AGE": "21", "ID": "1001", "MAJOR": "CS"},
            {"NAME": "MArwan", "AGE": "21", "ID": "1002", "MAJOR": "CS"},
            {"NAME": "Menna", "AGE": "21", "ID": "1003", "MAJOR": "CS"},
            {"NAME": "Nourhan", "AGE": "21", "ID": "1004", "MAJOR": "CS"},
            {"NAME": "Islam", "AGE": "21", "ID": "1005", "MAJOR": "CS"},
        ]
        
        with open(filename, 'w') as f:
            f.write("FILE_TYPE=STUDENT\n")
            f.write("STRUCTURE=DELIMITED\n")            
            f.write("FIELDS = NAME,AGE,ID,MAJOR\n")
            f.write("DELIMITER=|\n")
            f.write("===DATA===\n")
            
            for student in students_data:
                line = f"{student['NAME']}|{student['AGE']}|{student['ID']}|{student['MAJOR']}\n"
                f.write(line)
        
        print(f"file {filename} created successfully")
    
    def read_file(self, filename):
        try:
            with open(filename, 'r') as f:
                print(f"Contents of {filename}:")
                for line in f:
                    print(line.strip())
        except FileNotFoundError:
            print(f"File {filename} not found!")
    
    def search_student(self, filename, student_name):
        """search for student by name"""
        start_time = time.time()
        found = False
        
        try:
            with open(filename, 'r') as f:
                # skip header
                for line in f:
                    if line.strip() == "===DATA===":
                        break
                
                # search in data
                for line in f:
                    if student_name.lower() in line.lower():
                        print(f"found: {line.strip()}")
                        found = True
            
            if not found:
                print("student not found")
            
            end_time = time.time()
            print(f"search time: {end_time - start_time:.4f} seconds")
            
        except:
            print("file not found")
            
    def add_student(self, filename, name, age, student_id, major):
        """add a new student to the file"""
        try:
            with open(filename, 'a') as f:
                if "fixed" in filename:
                    line = f"{name:10}{age:3}{student_id:6}{major:8}\n"
                else:
                    line = f"{name}|{age}|{student_id}|{major}\n"
                
                f.write(line)   
        except:
            print("file not found")
             
def delete_student(self, filename, student_name):
    """delete a student by name"""
    try:
        header_lines = []
        data_lines = []
        found = False
        inside_data = False
        
        with open(filename, 'r') as f:
            for line in f:
                # detect data section
                if line.strip() == "===DATA===":
                    header_lines.append(line)
                    inside_data = True
                    continue
                
                # before ===DATA=== → header only
                if not inside_data:
                    header_lines.append(line)
                else:
                    # we are inside data → check names
                    if student_name.lower() in line.lower():
                        found = True
                        continue   # skip (delete)
                    data_lines.append(line)

        if found:
            # rewrite file
            with open(filename, 'w') as f:
                for h in header_lines:
                    f.write(h)
                for d in data_lines:
                    f.write(d)

            print(f"student {student_name} deleted successfully")
        else:
            print("student not found")
    
    except:
        print("file not found")
        
def update_student(self, filename, student_id, new_data):
    """Update a student record by ID"""
    updated = False
    lines = []

    try:
        with open(filename, 'r') as f:
            for line in f:
                if line.strip() == "===DATA===":
                    lines.append(line)
                    break
                lines.append(line)

            data_lines = f.readlines()

        new_file_data = []
        for line in data_lines:
            if student_id in line:
                updated = True
                if "fixed" in filename.lower():
                    new_line = f"{new_data['NAME']:10}{new_data['AGE']:3}{new_data['ID']:6}{new_data['MAJOR']:8}\n"
                else:
                    new_line = f"{new_data['NAME']}|{new_data['AGE']}|{new_data['ID']}|{new_data['MAJOR']}\n"

                new_file_data.append(new_line)
            else:
                new_file_data.append(line)

        with open(filename, 'w') as f:
            for l in lines:
                f.write(l)
            for d in new_file_data:
                f.write(d)

        if updated:
            print("Student updated successfully")
        else:
            print("Student ID not found")

    except:
        print("Error while updating")


    def show_menu(self):
        """display main menu"""
        print("\n" + "=" * 40)
        print("     simple student file management system")
        print("=" * 40)
        print("1. create fixed length file")
        print("2. create delimited file")
        print("3. read file")
        print("4. search for student")
        print("5. add student")
        print("6. add student")
        print("7. exit")
        print("=" * 40)
    
    def run(self):
        """run the program"""
        print("welcome to simple student file management system")
        
        while True:
            self.show_menu()
            choice = input("enter your choice (1-6): ")
            
            if choice == "1":
                self.create_fixed_file("students_fixed.txt")
            elif choice == "2":
                self.create_delimited_file("students_delimited.txt")
            elif choice == "3":
                filename = input("enter filename: ")
                self.read_file(filename)
            elif choice == "4":
                filename = input("enter filename: ")
                name = input("enter student name to search: ")
                self.search_student(filename, name)
            elif choice == "5":
               filename = input(
                   """  choose to add in 
1.students_fixed.txt 
2.students_delimited.txt   """)
                
               name = input("enter student name: ")
               age = input("enter student age: ")           
               student_id = input("enter student ID: ")
               major = input("enter student major: ")  
               self.add_student(filename,name, age, student_id, major)
               print(f"\nstudent {name} added successfully")
            elif choice == "6":
                filename = input(
                   """  choose to delete in     
1.students_fixed.txt 
2.students_delimited.txt   """) 
                
            elif choice == "7":
                print("goodbye")
                break
            else:
                print("invalid choice")

# run the program
if __name__ == "__main__":
    manager = StudenInfotManager()
    manager.run()