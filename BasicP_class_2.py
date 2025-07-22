import math 
# x = 10
# string = 'ok google'
# isBool = True
# floatInt = 435.35


# num = "1"
# print("Value of num is ", num)
# print("type of num" , type(int(num)))

# number = int(input())

#   if x % 2 == 0:
#    print("Even")
#   elif x == 0:
#    print("WTF")
#   else:
#    print("Odd")



# T = True
# F = False

# print(T and not F)

# num = int(input("Enter Number :"))
# num2 = int(input("Enter Number :"))

# print(type(num))
# print(type(num2))

# print(num > num2)

# x = 10
# y = 10

# if x == y:
#     print("True")
# elif x > y:
#     print("Elif")
# else:
#     print("False")
# print("starter pack yai mak")

distance = int(input("ระยะทาง : "))

if 5 <= distance >= 50:
    print("10 Baht")
elif 51 <= distance  >= 100:
    print("15 Baht")
elif 101 <= distance  >= 300:
    print("25 Baht")    
elif 301 <= distance  >= 500:
    print("35 Baht")
elif distance > 500:
    print("45 Baht")
else:
    print("มึงเมาหรอ")        