student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}
# 🚨 Don't change the code above 👆

#TODO-1: Create an empty dictionary called student_grades.


#TODO-2: Write your code below to add the grades to student_grades.👇
def assign_grades(score):
  if score >= 90:
    grade = "Outstanding"
  elif score >= 81 and score<=90:
    grade = "Exceeds Exceptions"
  elif score >= 71 and score<=80:
    grade = "Acceptable"
  else:
    grade = "Fail"
  return grade

for keys in student_scores:
  student_scores[keys] = assign_grades(student_scores[keys])

student_grades = student_scores
# 🚨 Don't change the code below 👇
print(student_grades)





