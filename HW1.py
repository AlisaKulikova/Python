# Задача 2: Найдите сумму цифр трехзначного числа.
# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0)
# ДЛЯ ТРЕХЗНАЧНОГО
 
# n=int(input("Enter a three-digit number: "))
# if n<100 or n>999:
#     print("You've entered a non-three-digit number")
# else:   
#     print ("The sum of the digits in the three- digit number is:", n//100+n//10%10+n%10)

# ДЛЯ ЛЮБОГО

# n=int(input("Enter a number: ")) 
# sum=0
# while n > 0:
#     digit = n%10
#     sum= sum+digit
#     n=n//10      
# print("The sum of the digits in the number is:",sum)


# Петя, Катя и Сережа делают из бумаги журавликов. Вместе они сделали S журавликов.
# Сколько журавликов сделал каждый ребенок, если известно, что Петя и Сережа сделали одинаковое количество журавликов,
# а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?
# 6 -> 1  4  1
# 24 -> 4  16  4
# 60 -> 10  40  10

# sum= int(input("Enter a sum of paper crane: "))
# if sum%6==0:
#     print("Petya made",sum//6,",","Sergey made", sum//6,",","Katya made",4*(sum//6))
# else:
#     print("There is no integer solution")


# Задача 6: Вы пользуетесь общественным транспортом?
# Вероятно, вы расплачивались за проезд и получали билет с номером. 
# Счастливым билетом называют такой билет с шестизначным номером, где сумма первых трех цифр равна сумме последних трех.
# Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6. 
# Вам требуется написать программу, которая проверяет счастливость билета.

# *Пример:*

# 385916 -> yes
# 123456 -> no



# n=(input("Enter a ticket number: "))
# if len(n)  %2==0:
#     if (int(n[0])+int(n[1])+int(n[2]))==(int(n[3])+int(n[4])+int(n[5])):
#         print("Congrats!You have a lucky ticket!")
#     else:
#         print("Oops:( You'll be lucky another time!)")     
# else:
#      print("it's wrong number! You have to enter 6 items")         


# Задача 8: Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек, 
# если разрешается сделать один разлом по прямой между дольками (то есть разломить шоколадку на два прямоугольника).

# *Пример:*

# 3 2 4 -> yes
# 3 2 1 -> no

# n=int(input("Enter a number of rows: "))
# m=int(input("Enter a number of strings: "))
# k=int(input("Enter a number of bites: "))
# if (n*m>k) and (k%n==0 or k%m==0):
#     print("YES")
# else:
#     print("NO")