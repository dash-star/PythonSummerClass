# This program calculates the grades of 3 exams input from the
# user to give out a GPA letter grade


# functions to calculate the average of the student's grades
# rounds the average to the nearest hundredth place
def calculateAverageGrade(g1, g2, g3):
    grade = g1 + g2 + g3
    grade = grade / 3
    grade = round(grade, 2)
    return grade


# function to say what grade the student got. Checks the grade down the list
# A = 90+, B = 80+, C = 70+, D = 60+, F = 59 or below
def letterGrade(grade):
    if grade >= 90:
        return "A"
    elif grade >= 80:
        return "B"
    elif grade >= 70:
        return "C"
    elif grade >= 60:
        return "D"
    else:
        return "F"


# function to generate the output
def output(name, g1, g2, g3, avg, lg):
    print("Student name: " + name)
    print("Test1: " + str(g1))
    print("Test2: " + str(g2))
    print("Test3: " + str(g3))
    print("Avg: " + str(avg))
    print("Letter Grade: " + lg)


# driver function that runs the program
def main():
    print("This program calculates GPA from exam grades.")
    name = input("Enter student name: ")
    grade1 = int(input("Enter exam 1 number grade: "))
    grade2 = int(input("Enter exam 2 number grade: "))
    grade3 = int(input("Enter exam 3 number grade: "))
    print()
    average = calculateAverageGrade(grade1, grade2, grade3)
    letter = letterGrade(average)
    output(name, grade1, grade2, grade3, average, letter)


# call main to run the program
main()
