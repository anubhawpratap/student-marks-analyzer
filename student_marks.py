name = "Anubhaw"

python_marks = 78
maths_marks = 85
dbms_marks = 72
english_marks = 80

total = python_marks + maths_marks + dbms_marks + english_marks

percentage = total / 400 * 100

# Grade
if percentage >= 90:
    grade = "A+"
elif percentage >= 80:
    grade = "A"
elif percentage >= 70:
    grade = "B"
elif percentage >= 60:
    grade = "C"
else:
    grade = "D"

# Result
if percentage >= 40:
    result = "PASS"
else:
    result = "FAIL"

print("==============================")
print("    STUDENT MARKS ANALYZER")
print("==============================")

print("Student:", name)
print("Total Marks:", total)
print("Percentage:", percentage)
print("Grade:", grade)
print("Result:", result)