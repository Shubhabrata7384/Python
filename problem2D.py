#wap to take input of 6 students' marks and store them in a list, then sort the list and print it
marks=[]

student1=int(input("Enter marks for student 1: "))
marks.append(student1)
student2=int(input("Enter marks for student 2: "))
marks.append(student2)  
student3=int(input("Enter marks for student 3: "))
marks.append(student3)
student4=int(input("Enter marks for student 4: "))
marks.append(student4)
student5=int(input("Enter marks for student 5: "))
marks.append(student5)
student6=int(input("Enter marks for student 6: "))
marks.append(student6)
marks.sort()
print(marks)