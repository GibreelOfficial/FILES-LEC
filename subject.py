#a programm to compute average and total marks for 4 subjects

name=input("Enter your name: ")
#subjects
english=float(input("English score: "))
biology=float(input("Biology score: "))
chemistry=float(input("chemistry score: "))
physics=float(input("Physics score: "))

#computations
total=int(english+biology+chemistry+physics)

average=(total/4)

#output

print(f"\n{('--'*15)}\n{name}\nThe total score is {total}\nThe average mark is {average}")