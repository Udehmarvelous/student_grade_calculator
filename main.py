student_grade = {
    "English": int(input("Enter your Score on English: ")),
    "Mathematics": int(input("Enter your score on Mathematics: ")),
    "Biology": int(input("Enter your score on Biology: ")),
    "Physics": int(input("Enter your score on Physics: "))
}

def english_grade():
    english = student_grade["English"]
    if english >= 75:
        Grade = "A1 "
        comment = "Excellent"
        return f"English {Grade}"
    elif english >= 70:
        Grade = "B2 "
        comment = "Very Good"
        return f"English {Grade}"
    elif english >= 65:
        Grade = "B3 "
        comment = "Good"
        return f"English {Grade}"
    elif english >= 60:
        Grade = "C4 "
        comment = "Credit"
        return f"English {Grade}"
    elif english >= 55:
        Grade = "C5 "
        comment = "Credit"
        return f"English {Grade}"
    elif english >= 45:
        Grade = "C6"
        comment = "Credit"
        return f"English {Grade}"
    elif english >= 40:
        Grade = "D7"
        comment = "Pass"
        return f"English {Grade}"
    elif english >= 35:
        Grade = "E8"
        comment = "pass"
        return f"English {Grade}"
    else:
        Grade = "F9"
        comment = "Fail"
        return f"English {Grade}"

def math_grade():
    math = student_grade["Mathematics"]
    if math >= 75:
        Grade = "A1 "
        comment = "Excellent"
        return f"Mathematics {Grade}"
    elif math >= 70:
        Grade = "B2 "
        comment = "Very Good"
        return f"Mathematics {Grade}"
    elif math >= 65:
        Grade = "B3 "
        comment = "Good"
        return f"Mathematics {Grade}"
    elif math >= 60:
        Grade = "C4 "
        comment = "Credit"
        return f"Mathematics {Grade}"
    elif math >= 55:
        Grade = "C5 "
        comment = "Credit"
        return f"Mathematics {Grade}"
    elif math >= 45:
        Grade = "C6"
        comment = "Credit"
        return f"Mathematics {Grade}"
    elif math >= 40:
        Grade = "D7"
        comment = "Pass"
        return f"Mathematics {Grade}"
    elif math >= 35:
        Grade = "E8"
        comment = "pass"
        return f"Mathematics {Grade}"
    else:
        Grade = "F9"
        comment = "Fail"
        return f"Mathematics {Grade}"

def biology_grade():
    biology = student_grade["Biology"]
    if biology >= 75:
        Grade = "A1 "
        comment = "Excellent"
        return f"Biology {Grade}"
    elif biology >= 70:
        Grade = "B2 "
        comment = "Very Good"
        return f"Biology {Grade}"
    elif biology >= 65:
        Grade = "B3 "
        comment = "Good"
        return f"Biology {Grade}"
    elif biology >= 60:
        Grade = "C4 "
        comment = "Credit"
        return f"Biology {Grade}"
    elif biology >= 55:
        Grade = "C5 "
        comment = "Credit"
        return f"Biology {Grade}"
    elif biology >= 45:
        Grade = "C6"
        comment = "Credit"
        return f"Biology {Grade}"
    elif biology >= 40:
        Grade = "D7"
        comment = "Pass"
        return f"Biology {Grade}"
    elif biology >= 35:
        Grade = "E8"
        comment = "pass"
        return f"Biology {Grade}"
    else:
        Grade = "F9"
        comment = "Fail"
        return f"Biology {Grade}"

def physics_grade():
    physics = student_grade["Physics"]
    if physics >= 75:
        Grade = "A1 "
        comment = "Excellent"
        return f"Physics {Grade}"
    elif physics >= 70:
        Grade = "B2 "
        comment = "Very Good"
        return f"Physics {Grade}"
    elif physics >= 65:
        Grade = "B3 "
        comment = "Good"
        return f"Physics {Grade}"
    elif physics >= 60:
        Grade = "C4 "
        comment = "Credit"
        return f"Physics {Grade}"
    elif physics >= 55:
        Grade = "C5 "
        comment = "Credit"
        return f"Physics {Grade}"
    elif physics >= 45:
        Grade = "C6"
        comment = "Credit"
        return f"Physics {Grade}"
    elif physics >= 40:
        Grade = "D7"
        comment = "Pass"
        return f"Physics {Grade}"
    elif physics >= 35:
        Grade = "E8"
        comment = "pass"
        return f"Physics {Grade}"
    else:
        Grade = "F9"
        comment = "Fail"
        return f"Physics {Grade}"

def calculate_student():
    total = sum(student_grade.values())
    Average = total / 4
    if Average >= 75:
        comment = "Excellent"
        return f"Your Average is {Average} And You did {comment}"
    elif Average >= 70:
        comment = "Very Good"
        return f"Your Average is {Average} And You did {comment}"
    elif Average >= 65:
        comment = "Good"
        return f"Your Average is {Average} And You did {comment}"
    elif Average >= 60:
        comment = "Credit"
        return f"Your Average is {Average} And You have {comment}"
    elif Average >= 55:
        comment = "Credit"
        return f"Your Average is {Average} And You have {comment}"
    elif Average >= 45:
        comment = "Credit"
        return f"Your Average is {Average} And You have {comment}"
    elif Average >= 40:
        comment = "Pass"
        return f"Your Average is {Average} And You {comment}"
    elif Average >= 35:
        comment = "Pass"
        return f"Your Average is {Average} And You {comment}"
    else:
        comment = "Fail"
        return f"Your Average is {Average} And You {comment}"
print(english_grade())
print(math_grade())
print(biology_grade())
print(physics_grade())
print(calculate_student())
        
