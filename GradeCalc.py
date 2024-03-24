numGrades = 0
studentName = " "

# prompt user to enter number of grades to be processed and student name
numGrades = int(input("Enter number of grades to process : "))

i = 0
studentAverage = 0
studentGradeTally = 0
# continue processing assignment grades for student for until number of assignments processed
studentName = input("Enter student name: ")

if numGrades == 0:
    print("Please enter a number bigger than 0")

while (i < numGrades):
    studentGrade = int(input("Enter assignment grade: "))

    # accumulate student grades
    studentGradeTally = studentGradeTally + studentGrade
    print("Grade entered is: ", studentGrade)
    print("Current running total is: ", studentGradeTally)

    # increment loop counter
    i = i + 1
    print("Current loop variable value is: ", i)

if numGrades > 0:
    # calculate student average and set letter grade value
    studentAverage = studentGradeTally / numGrades

print()
print(studentName, "has an average of: ", studentAverage)
print()