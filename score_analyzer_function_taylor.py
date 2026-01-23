def let_grade(grade):
    if grade >=90:
        return "A"
    elif grade>=80:
        return "B"
    elif grade>=70:
        return"C"
    else:
        return "F"
    
def student_record(name, grade, letter_grade):
    return [name,grade,letter_grade]