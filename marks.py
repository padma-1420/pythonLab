def determine_grade(marks):
    if marks >= 90:
        return "Grade: A"
    elif marks >= 80:
        return "Grade: B"
    elif marks >= 70:
        return "Grade: C"
    elif marks >= 60:
        return "Grade: D"
    else:
        return "Grade: F"
marks = float(input("Enter your marks: "))
print(determine_grade(marks))
