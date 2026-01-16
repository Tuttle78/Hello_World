# Welcome to my grade scale.
# These ask for the name of the student and their grade.
name=input("What is the name of your first student?")
name2=input("What is the name of your second student?")
name3=input("What is the name of your third student?")
grade=int(input("what is "+ name+ "'s grade?"))
grade2=int(input("what is "+ name2+ "'s grade?"))
grade3=int(input("what is "+ name3+ "'s grade?"))
students=[]
students.append(name)
students.append(name2)
students.append(name3)
grades=[]
let_grades=[]
grades.append(grade)
grades.append(grade2)
grades.append(grade3)
if grades[0] >= 90:
    if grades[0]>=97:
        let_grades.append("A+")
    elif grades[0]>=93:
        let_grades.append("A")
    else:
        let_grades.append("A-")
    if grades[0]>=80:
        if grades[0]>=87:
                    let_grades.append("B+")
        elif grades[0]>=83:
            let_grades.append("B")
        else:
            let_grades.append("B-")
            if grades[0] >= 70:
                if grades[0]>=77:
                    let_grades.append("C+")
                elif grades[0]>=73:
                    let_grades.append("C")
                else:
                    let_grades.append("C-")

print(let_grades)