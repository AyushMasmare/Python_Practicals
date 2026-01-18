name=input("Name: ")

dep=input("Department: ")

year=input("Year: ")

sem=input("Semester: ")

sec=input("Section: ")

r=input("Roll Number: ")

m1=float(input("Enter marks for subject 1: "))

m2=float(input("Enter marks for subject 2: "))

m3=float(input("Enter marks for subject 3: "))

m4=float(input("Enter marks for subject 4: "))

m5=float(input("Enter marks for subject 5: "))

m=m1+m2+m3+m4+m5

per=m/5

print("STUDENT MARKSHEET")

print("Name: ", name)

print("Department: ", dep)

print("Year: ", year)

print("Semester: ", sem)

print("Section: ", sec)

print("Roll Number: ",r)

print("Subject 1 Marks: ", m1)

print("Subject 2 Marks: ", m2)

print("Subject 3 Marks: ", m3)

print("Subject 4 Marks: ", m4)
print("Subject 5 Marks: ",m5)

print("Total Marks: ",m);

print(f"Percentage: {per:.2f}%")