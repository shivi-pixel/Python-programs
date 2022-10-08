
# Asking for User-Input
# Code written by Shivsagar Mishra

a=input("Enter Name:")
b=input("Enter Department:")

# Exception-Handling for Marks if user enters a String Value instead of Integer
try:
    # User-Input for Marks
    c=int(input("Enter Marks:"))
    # if-loop for Grading
    if c>=80:
        grade = "A"
    elif c>=70:
        grade = "B"
    elif c>=60:
        grade = "C"
    elif c>=50:
        grade ="D"
    elif c>=40:
        grade = "E"
    else:
        grade="Failed !"
except Exception as e:
    print(e)

    # Printing all the details of Student in IDLE
print('-------------------------------------')
print("Student details:- \nName:",a,"\nDepartment:",b,"\nMarks:",c,"\nGrade:",grade)
# Creating Variables for printing the Values in .txt File
name="\n\nStudent details:- \nName:"
Department="\nDepartment:"
Marks ="\nMarks:"
result="\nGrade:"

# Creating a Data.txt file if it is already existing Opening it in Write MOde
ch='a'
p='a'
choice=input("Choose the mode you want to open the file:\n1. Write Mode\n2. Append Mode\n3. Text Mode\n4. Creation Mode\n5. Read Mode\nYour Choice:")
if choice==1:
    ch='w'
    print("selected write mode")
elif choice==2:
    ch='a'
    print('selected append mode')
elif choice==3:
    ch='t'
    print('selected text mode')
elif choice==4:
    ch='x'
    print('selected create mode')
elif choice==5:
    ch='r'
    print('selected read mode')
f=open('C:/Users/Pradeep Mishra/Documents/data.txt',ch)

# Using Write function for writing Data in .txt files
# Writing Name Details of Students
f.write(str(name))
f.write(str(a))
# Writing Department Details of Students
f.write(str(Department))
f.write(str(b))
# Writing Marks Details of Students
f.write(str(Marks))
f.write(str(c))
# Writing Grade Details of Students
f.write(str(result))
f.write(str(grade))
# Closing the file
print("The data in the file added successfully!")
f.close()


'''
output

Enter Name:ABC
Enter Department:computer Engineering
Enter Marks:90
-------------------------------------
Student details:- 
Name: ABC 
Department: computer Engineering 
Marks: 90 
Grade: A
Choose the mode you want to open the file:
1. Write Mode
2. Append Mode
3. Text Mode
4. Creation Mode
5. Read Mode
Your Choice:2
The data in the file added successfully!


before running the code:
'''


