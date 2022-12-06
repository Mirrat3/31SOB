# Calculating Grades (ok, let me think about this one)

# Write a program that will average 3 numeric exam grades, return an average test score, a corresponding letter grade, and a message stating whether the student is passing.

# Average	Grade
# 90+	         A
# 80-89	         B
# 70-79	         C
# 60-69	         D
# 0-59	         F

# Exams: 89, 90, 90
# Average: 90
# Grade: A
# Student is passing.

# Exams: 50, 51, 0
# Average: 33
# Grade: F
# Student is failing.........

exam_one = int(input("Input exam grade one: "))

exam_two = int(input("Input exam grade two: "))

exam_three = int(input("Input exam grade three: "))

grades = [exam_one,exam_two,exam_three]
sum_of_grades = 0
for grade in grades:
    sum_of_grades = sum_of_grades + grade

avg = sum_of_grades / len(grades)

if avg >= 90:
    letter_grade = "A"
elif avg >= 80 and avg < 90:
   letter_grade = "B"
elif avg >= 70 and avg < 80:
    letter_grade = "C"
elif avg >= 60 and avg <70:
    letter_grade = "D"
else:
    letter_grade = "F"

print("Exam: " , sep="," , *grades)

print("Average: " , (avg))

print("Grade: " , letter_grade)

if letter_grade == "F":
    print ("Student is failing.")
else:
    print ("Student is passing.")
