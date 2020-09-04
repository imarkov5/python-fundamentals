#1
def a():
    return 5
print(a()) #returns and outputs 5

#2
def a():
    return 5
print(a()+a()) #returns 5 2 times and outputs 10

#3
def a():
    return 5
    return 10
print(a()) #returns 5 and outputs 5

#4
def a():
    return 5
    print(10)
print(a()) #returns and outputs 5

#5
def a():
    print(5)
x = a()
print(x) #returns nothing outputs 5 (output was 5,none)

#6
def a(b,c):
    print(b+c)
print(a(1,2) + a(2,3)) #returns nothing, outputs 3,5,none (output was 3,5 and Error:unsupported operand)

def a(b,c):
    print(b+c)
x =int(a(1,2))
y = int(a(2,3))
print(x+y)
#7
def a(b,c):
    return str(b)+str(c)
print(a(2,5)) #returns and outputs 25 (25 became a string))

#8
def a():
    b = 100
    print(b)
    if b<10:
        return 5
    else:
        return 10
    return 7
print(a())
#outputs 100,10 returns 10

#9
def a(b,c):
    if b<c:
        return 7
    else:
        return 14
    return 3
print(a(2,3))
print(a(5,3))
print(a(2,3) + a(5,3))
#returns 7 and 14, outputs 7,14,21

#10
def a(b,c):
    return b+c
    return 10
print(a(3,5))
#returns and outputs 8

#11
b = 500
print(b)
def a():
    b = 300
    print(b)
print(b)
a()
print(b)
#returns nothing, outputs 500,500,300,500

#12
b = 500
print(b)
def a():
    b = 300
    print(b)
    return b
print(b)
a()
print(b)
#output 500,500,300,500, returns 300

#13
b = 500
print(b)
def a():
    b = 300
    print(b)
    return b
print(b)
b=a()
print(b)
#outputs 500, 500, 300, 300 returns 300 and stores in a b parameter

# #14
def a():
    print(1)
    b()
    print(2)
def b():
    print(3)
a()
# #outputs 1,3 (correct answer 1,3,2)

 #15
def a():
     print(1)
     x = b()
     print(x)
     return 10
def b():
    print(3)
    return 5
y = a()
print(y)
#outputs 1,3,5,10