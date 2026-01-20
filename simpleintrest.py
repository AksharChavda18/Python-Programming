#1. Write a program to input p, r, n and find out interest using simple input output statement.

p = int(input("enter price : "))
r = int(input("enter rate of intrest : "))
n = int(input("enter number of years : "))

simpleintrest = (p*r*n)/100
print(simpleintrest)