#https://replit.com/@SakshamVerma1/day-5-1-test-your-code#README.md

# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆


#Write your code below this row 👇

sum = 0
length = 0
for i in student_heights:
  sum += i
  length += 1
  
print(round(sum/length))


######################################################################

print(len(student_heights))
print(sum(student_heights))