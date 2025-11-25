import time
from datetime import datetime

class StudentInfoManager:
    def __init__(self):
        self.students = []
    
    # create file---------------------------------------    
    
    def create_fixed_file(self, filename):
        students_data = [
            {"NAME": "Nour", "AGE": "21", "ID": "1001", "MAJOR": "CS"},
            {"NAME": "Marwan", "AGE": "21", "ID": "1002", "MAJOR": "CS"},
            {"NAME": "Menna", "AGE": "21", "ID": "1003", "MAJOR": "CS"},
            {"NAME": "Nourhan", "AGE": "21", "ID": "1004", "MAJOR": "CS"},
            {"NAME": "Islam", "AGE": "21", "ID": "1005", "MAJOR": "CS"},
        ]
            
        with open(filename, 'w') as f:
            f.write("FILE_TYPE=STUDENT\n")
            f.write("STRUCTURE=FIXED\n")
            f.write("FIELDS=NAME,AGE,ID,MAJOR\n")
            f.write("===DATA===\n")
            
            for student in students_data:
                line = f"{student['NAME']:10}{student['AGE']:3}{student['ID']:6}{student['MAJOR']:8}\n"
                f.write(line)
        
        print(f"file {filename} created successfully")
    
    
    # create file---------------------------------------   
     
    def create_delimited_file(self, filename):
        students_data = [
            {"NAME": "Nour", "AGE": "21", "ID": "1001", "MAJOR": "CS"},
            {"NAME": "Marwan", "AGE": "21", "ID": "1002", "MAJOR": "CS"},
            {"NAME": "Menna", "AGE": "21", "ID": "1003", "MAJOR": "CS"},
            {"NAME": "Nourhan", "AGE": "21", "ID": "1004", "MAJOR": "CS"},
            {"NAME": "Islam", "AGE": "21", "ID": "1005", "MAJOR": "CS"},
        ]
        
        with open(filename, 'w') as f:
            f.write("FILE_TYPE=STUDENT\n")
            f.write("STRUCTURE=DELIMITED\n")            
            f.write("FIELDS=NAME,AGE,ID,MAJOR\n")
            f.write("DELIMITER=|\n")
            f.write("===DATA===\n")
            
            for student in students_data:
                line = f"{student['NAME']}|{student['AGE']}|{student['ID']}|{student['MAJOR']}\n"
                f.write(line)
        
        print(f"file {filename} created successfully")
    
    
    # read file---------------------------------------  
    
    def read_file(self, filename):
        try:
            with open(filename, 'r') as f:
                print(f"Contents of {filename}:")
                for line in f:
                    print(line.rstrip())
        except FileNotFoundError:
            print(f"File {filename} not found!")
    
    # search student---------------------------------------
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
            
        except FileNotFoundError:
            print("file not found")
        
           
    # add student---------------------------------------
            
    def add_student(self, filename, name, age, student_id, major):
        """add a new student to the file"""
        try:
            with open(filename, 'a') as f:
                if "fixed" in filename.lower():
                    line = f"{name:10}{age:3}{student_id:6}{major:8}\n"
                else:
                    line = f"{name}|{age}|{student_id}|{major}\n"
                
                f.write(line)
            print(f"student {name} added successfully")
        except FileNotFoundError:
            print("file not found")
        
           
    # delete student---------------------------------------
            
    def delete_student(self, filename, student_name):
        """delete a student by name"""
        try:
            header_lines = []
            data_lines = []
            found = False
            inside_data = False
            
            with open(filename, 'r') as f:
                for line in f:
                    if line.strip() == "===DATA===":
                        header_lines.append(line)
                        inside_data = True
                        continue
                    
                    if not inside_data:
                        header_lines.append(line)
                    else:
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
        except FileNotFoundError:
            print("file not found")
        
        
        
    # update student-------------------------------
    
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
    
        except FileNotFoundError:
            print("Error: file not found")
       
        
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
        print("6. delete student")
        print("7. update student")  
        print("8. exit")
        print("=" * 40)
    
    def choose_file(self):
        choice = input("Choose file: 1) students_fixed.txt  2) students_delimited.txt  -> ")
        if choice.strip() == "1":
            return "students_fixed.txt"
        else:
            return "students_delimited.txt"
    
    def run(self):
        """run the program"""
        print("welcome to simple student file management system")
        
        while True:
            self.show_menu()
            choice = input("enter your choice (1-8): ").strip()
            
            if choice == "1":
                self.create_fixed_file("students_fixed.txt")
            elif choice == "2":
                self.create_delimited_file("students_delimited.txt")
            elif choice == "3":
                filename = input("enter filename: ").strip()
                self.read_file(filename)
            elif choice == "4":
                filename = input("enter filename: ").strip()
                name = input("enter student name to search: ").strip()
                self.search_student(filename, name)
            elif choice == "5":
                filename = self.choose_file()
                name = input("enter student name: ").strip()
                age = input("enter student age: ").strip()           
                student_id = input("enter student ID: ").strip()
                major = input("enter student major: ").strip()  
                self.add_student(filename, name, age, student_id, major)
            elif choice == "6":
                filename = self.choose_file()
                name = input("enter student name to delete: ").strip()
                self.delete_student(filename, name)
            elif choice == "7":
                filename = self.choose_file()
                student_id = input("enter student ID to update: ").strip()
                name = input("enter new student name: ").strip()
                age = input("enter new student age: ").strip()           
                new_id = input("enter new student ID: ").strip()
                major = input("enter new student major: ").strip()  
                new_data = {"NAME": name, "AGE": age, "ID": new_id, "MAJOR": major}
                self.update_student(filename, student_id, new_data)
            elif choice == "8":
                print("goodbye")
                break
            else:
                print("invalid choice")

if __name__ == "__main__":
 manager = StudentInfoManager()
 manager.run()