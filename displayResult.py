#3. Write a program to enter marks of 4 subjects and display result (result shall include total, percentage and grade)

sub1 = float(input("Enter marks of Subject 1: "))
sub2 = float(input("Enter marks of Subject 2: "))
sub3 = float(input("Enter marks of Subject 3: "))
sub4 = float(input("Enter marks of Subject 4: "))

total = sub1 + sub2 + sub3 + sub4
percentage = total/4

if percentage >= 90:
    grade = 'A'
elif percentage >= 80:
    grade = 'B'
elif percentage >= 70:
    grade = 'C'
elif percentage >= 60:
    grade = 'D'
elif percentage >= 50:
    grade = 'E'
else:
    grade = 'F'

print("\nTotal Marks:", total)
print("Percentage:", percentage, "%")
print("Grade:", grade)
