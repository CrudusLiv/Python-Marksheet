import os 
import json  
import matplotlib.pyplot as plt

def menu(): # a menu of grades for a teacher. It lists the different grade ranges and their corresponding grades. 
    print("Final Mark         Grade") 
    print("x < 50              F") 
    print("50% ? x < 55%      PS2") 
    print("55% ? x < 60%      PS1 ") 
    print("60% ? x < 65%      CR2") 
    print("65% ? x < 70%      CR1") 
    print("70% ? x < 75%      DI2 ")
    print("75% ? x < 80%      DI1 ") 
    print("80% ? x < 85%      HD2") 
    print(" x >= 85%          HD1")
class PythonMarksheet:
    def __init__(self):
        self.student_data = {}
        #creates an empty dictionary to store the data for each student in the Student class instance.

    def add_student(self): # this promps user to key in the information of students (test information), the loop ends when user presses enter 
        while True:
            student_id = input("Enter student ID (press enter to finish): ")
            if not student_id:
                break
            name = input("Enter student name: ")
            test1_mark = float(input("Enter Test 1 mark: "))
            assign1_mark = float(input("Enter Assignment 1 mark: "))
            test2_mark = float(input("Enter Test 2 mark: "))
            assign2_mark = float(input("Enter Assignment 2 mark: "))
            final_mark = float(input("Enter student final mark: "))
            total_mark = self.total_mark({'test1': test1_mark, 'assign1': assign1_mark, 'test2': test2_mark, 'assign2': assign2_mark, 'final_mark': final_mark})
            grade = self.grade(total_mark)
            self.student_data[student_id] = {'student_id':student_id, 'name': name, 'test1': test1_mark, 'assign1': assign1_mark, 'test2': test2_mark, 'assign2': assign2_mark, 'final_mark': final_mark , 'total_mark':total_mark, 'grade':grade} #adding a new student record to the dictionary self.student_data with a unique key student_id
            print(" ")

    def total_mark(self, data): #formula on how to calculate total mark of a student 
        total_mark = round(data['test1']*0.1 + data['assign1']*0.1 + data['test2']*0.1 + data['assign2']*0.1 + data['final_mark']*0.6 , 2)
        return total_mark

    def grade(self, total_mark):
        if total_mark < 50:
            return 'F'
        elif 50 <= total_mark < 55:
            return 'PS2'
        elif 55 <= total_mark < 60:
            return 'PS1'
        elif 60 <= total_mark < 65:
            return 'CR2'
        elif 65 <= total_mark < 70:
            return 'CR1'
        elif 70 <= total_mark < 75:
            return 'DI2'
        elif 75 <= total_mark < 80:
            return 'DI1'
        elif 80 <= total_mark < 85:
            return 'HD2'
        else:
            return 'HD1'
        
    def show(self): #display information that have been key in earlier in the add_student function
        for student_id, data in self.student_data.items():
            print("Student ID: "+ data['student_id'])
            print("Student Name: "+ data['name'])
            print("Student Marks for test 1: "+ str(data['test1']))
            print("Student Assignment 1: "+ str(data['assign1']))
            print("Student Test 2: "+ str(data['test2']))
            print("Student Assignment 2: "+ str(data['assign2']))
            print("Student Final exam mark:" + str(data['final_mark']))
            print("Student Total mark :" + str(data['total_mark']))
            print("Student Grade:" + data['grade'])
            print(" ")
            
            
    def AddModifyRecords(self):
        os.system('cls')
        print('You are adding/modifying records...')
        year = input('Enter year: ')
        semester = input('Enter semester: ')
        filename = f'PythonMarksheet_{year}_Semester{semester}.txt'
        try:
            with open(filename) as f:
                content = f.read()
                content = content.replace("'", '"')
                content = content.replace('None', 'null')
                content = json.loads(content)
        except:
            content = dict()
            student_name = input("Enter student's name: ")
            if student_name not in content.keys():
                student  = PythonMarksheet(student_name)
            else:
                student_data = content[student_name]
                student = PythonMarksheet(student_name)
                student.marks = student_data['marks']
            option = 0
            counter = 0
            while True:
                print('1: Test 1')
                print('2: Assignment 1')
                print('3: Test 2')
                print('4: Assignment 4')
                print('5: Final Examination')
                print('6: Back to Main Menu')
                option = input('Select an option: ')
                if option == '1':
                    if student.marks['test_1'] != None:
                        print(f"Current Test 1 Record = {student.marks['test_1']:.1f}")
                    student.marks['test_1'] = float(input('Enter the mark for Test 1: '))
                    counter += 1
                elif option == '2':
                    if student.marks['assignment_1'] != None:
                        print(f"Current Assignment 1 Record = {student.marks['assignment_1']:.1f}")
                        student.marks['assignment_1'] = float(input('Enter the mark for Assignment 1: '))
                        counter += 1
                elif option == '3':
                    if student.marks['test_2'] != None:
                        print(f"Current Test 2 Record = {student.marks['test_2']:.2f}")
                    student.marks['test_2'] = float(input('Enter the mark for Test 2: '))
                    counter += 1
                elif option == '4':
                    if student.marks['assignment_2'] != None:
                        print(f"Current Assignment 2 Record = {student.marks['assignment_2']:.1f}")
                    student.marks['assignment_2'] = float(input('Enter the mark for Assignment 2: '))
                    counter += 1
                elif option == '5':
                    if student.marks['final_examination'] != None:
                        print(f"Current Final Examination Record = {student.marks['final_examination']:.1f}")
                    student.marks['final_examination'] = float(input('Enter the mark for Final Examination: '))
                    counter += 1
                elif option == '6':
                    if counter != 0:
                        save_option = 0
                        while True:
                            save_option = input('Do you want to save your change(s)? (Y/N): ')
                            save_option = save_option.upper()
                            if save_option == 'Y':
                                content[student_name] = student.save()
                                content = str(content)
                                with open(filename, 'w') as f:
                                                                    f.write(content)
                                print('Your change(s) are saved.')
                                os.system('cls')
                                break
                            elif save_option == 'N':
                                print('Your change(s) are not saved.')
                                os.system('cls')
                                break
                            else:
                                print('Invalid option!!!')
                    break
                else:
                    print('Invalid option!!!')

    def ReadRecords(self):
        os.system('cls')
        print('You are reading records...')
        year = input('Enter year: ')
        semester = input('Enter semester: (in PythonMarksheet_{year}_Semester{semester} format)')
        filename = filename = f'PythonMarksheet_{year}_Semester{semester}.txt'
        try:
            with open(filename, 'r') as f:
                content = f.read()
                content = content.replace("'", '"')
                content = content.replace('None', 'null')
                content = json.loads(content)
        except:
            print('No Record Found')
            input('Press enter to return to continue.')     
            os.system('cls')   
            return 0             
            df = pd.DataFrame(columns=['Name', 'Test 1 (10%)', 'Assignment 1 (10%)', 'Test 2 (10%)', 'Assignment 2 (10%)', 'Final Examination (60%)', 'Total (100%)', 'Grade'])
            for i in content:
                if content[i]['grade'] == None:
                    pass
                else:
                    data = pd.DataFrame({'Name': [i],
                                        'Test 1 (10%)': [content[i]['marks']['test_1']],
                                        'Assignment 1 (10%)': [content[i]['marks']['assignment_1']],
                                        'Test 2 (10%)': [content[i]['marks']['test_2']],
                                        'Assignment 2 (10%)': [content[i]['marks']['assignment_2']],
                                        'Final Examination (60%)': [content[i]['marks']['final_examination']],
                                        'Total (100%)': [content[i]['final_mark']],
                                        'Grade': [content[i]['grade']]})
                    df = df.append(data)
            if df.empty:
                print('No Record Found')
                input('Press enter to return to continue.')
                os.system('cls')
                return 0
            else:
                print(df)
                input('Press enter to return to main menu.')
                os.system('cls')
                return 0

            

        

        
    
    def selection(self): #menu for teacher to choose which one they want
        while True:
            print("*********************************************************************")
            print("**                                                                 **")
            print("**                                                                 **")
            print("**                    DATA STORING SYSTEM                          **")
            print("**                                                                 **")
            print("**                                                                 **")
            print("*********************************************************************")
            print("**                    Press 1 to add student                       **")
            print("**                       Press 2 to edit                           **")
            print("**                 Press 3 to delete student                       **")
            print("**            Press 4 to display student grade's distribution      **")
            print("**                     Press 5 to save file                        **")
            print("**        Press 6 to add generate a grade distribution histogram   **")
            print("**              Press 7 to exit this program                       **")
            print("*********************************************************************")

            user_inp = input("Key in the selection you want here:")

            if user_inp == '1': #brings the user back to add_student function and put enter addition informations
                self.add_student()
                print("Student added successfully!")

            elif user_inp == '2': #allows user to edit the information of specific student they want by enter their student id
                student_id = input("Enter student ID to edit: ") #key in the student's student id they want to edit here 
                if student_id in self.student_data: #promps user to edit the informations
                    student = self.student_data[student_id]
                    print(f"Editing data for {student['name']}")
                    test1_mark = float(input("Enter new Test 1 mark: "))
                    assign1_mark = float(input("Enter new Assignment 1 mark: "))
                    test2_mark = float(input("Enter new Test 2 mark: "))
                    assign2_mark = float(input("Enter new Assignment 2 mark: "))
                    final_mark = float(input("Enter new final mark: "))
                    total_mark = self.total_mark({'test1': test1_mark, 'assign1': assign1_mark, 'test2': test2_mark, 'assign2': assign2_mark, 'final_mark': final_mark})
                    grade = self.grade(total_mark)
                    student.update({'test1': test1_mark, 'assign1': assign1_mark, 'test2': test2_mark, 'assign2': assign2_mark, 'final_mark': final_mark, 'total_mark': total_mark, 'grade': grade})
                    print("Student data updated successfully!")
                else:
                    print("Invalid student ID!") #if the student id not in the dictionary

            elif user_inp == '3': #allows user to delete student's infromation by just key in the student's id
                student_id = input("Enter student ID to delete: ")
                if student_id in self.student_data:
                    del self.student_data[student_id]
                    print("Student data deleted successfully!")
                else:
                    print("Invalid student ID!")

             
            elif user_inp == '4' : #a table that shows student's marks, grade , total mark
                print(f"{'ID':<15}{'Name':<20}{'Test 1':<10}{'Assignment 1':<15}{'Test 2':<10}{'Assignment 2':<15}{'Final Mark':<10}{'Total Mark':<10}{'Grade':<10}")
                for student_id, data in self.student_data.items():
                    print(f"{student_id:<15}{data['name']:<20}{data['test1']:<10}{data['assign1']:<15}{data['test2']:<10}{data['assign2']:<15}{data['final_mark']:<10}{data['total_mark']:<10}{data['grade']:<10}")
                    
            elif user_inp == '5': #save file
                self.ReadRecords()
        
            elif user_inp == '6': # section that generate grade distribution histogram of students
                grades = [data['grade'] for data in self.student_data.values()]
                grade_counts = {grade: grades.count(grade) for grade in set(grades)}
                grades_sorted = sorted(grade_counts.items())
                x = [grade[0] for grade in grades_sorted]
                y = [grade[1] for grade in grades_sorted]

                plt.bar(x, y)
                plt.xlabel('Grades')
                plt.ylabel('Number of Students')
                plt.title('Grade Distribution')
                plt.show()
                    
            elif user_inp == '7': #end program
                print("Exiting program...")
                break
                
                
            else: #this happens when user key in a value that is out of the menu function (in selection), which is out of 1-7.
                print("Please enter a valid number!!")
                






                
menu() #Calls the menu() function, which prints out a menu for the teacher.
pms = PythonMarksheet() #Creates an instance of the PythonMarksheet class called pms.
pms.add_student()# Calls the add_student() method of the pms object, which prompts the user to enter details of each student, calculates their total mark and grade, and adds them to the student_data dictionary.
pms.show() #Calls the show() method of the pms object, which prints out a table of all the student data that has been added.
pms.selection() #Calls the selection() method of the pms object, which prompts the user to enter a student ID and then displays the data for that student.

