import score_analyzer_function_taylor

num_students=int(input("how many students do you have? "))
for e in range(1,num_students+1):
    name=input("What is this students name? ")
    grade=int(input("What is "+name+"'s grade? "))
    letter_grade = score_analyzer_function_taylor.let_grade(grade)
    record =score_analyzer_function_taylor.student_record(name, grade, letter_grade)
    print(record)
