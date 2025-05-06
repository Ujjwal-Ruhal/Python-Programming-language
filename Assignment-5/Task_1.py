'''
Task 1: Create a Dictionary of Student Marks
----> Creates a dictionary where student names are keys and their marks are values.
----> Asks the user to input a student's name.
----> Retrieves and displays the corresponding marks.
----> If the student’s name is not found, display an appropriate message.
'''
# Variable_name = key_name:Key_Values,Key:Value,..............
# like Key = Ujjwal , Udit ,....
# and Values = 85 , 80 , .....

# create a dictionary and fill's the details like student name and marks...
student_marks= {'Ujjwal':85, 'Udit':80, 'Aman':79, 'Annu':83, 'Ankita':72}
print(student_marks)
student_name = input('Enter the student name: ')

if student_name in student_marks:
    print(student_name+ ' marks: '+ str(student_marks[student_name]))
else:
    print(student_marks.get(student_name,'student not found.'))

print('Thank you')