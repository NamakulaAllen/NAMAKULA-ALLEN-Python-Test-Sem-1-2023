def sum(student_marks):
    total = 0
    for m in student_marks:
        total += m
    return total
print(sum((78, 83, 90, 88, 75)))

student_marks =[78, 83, 90, 88, 75]
first_letter =[78]
last_letter =[75]
print(first_letter)
print(last_letter)

student_marks.append(96)
print(tuple(student_marks))

student_marks = [78, 83, 90, 88, 75]
first_letter.append(87)
print(first_letter)


#UPDATE 78 TO 87
student_marks[0] = 87
print(student_marks)



