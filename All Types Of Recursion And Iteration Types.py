# recursion are mainly of two types depending on whether a function calls itself from whithin itself or more than one function call one another mutually. The first one is called direct recursion and and another one is called indirect recursion.

# Thus the two types of recursion are :

# 1. Direct Recursion: these can be further categorized into four types

# a. Tail Recursion: if a recursive function calling itself and that recursive call is the last statement in the function then it is known as Tail recursion. After that call the recursive function performs nothing. the function has to process or perform any operation at the time of calling and it does nothing at returning time

# tail recursion
def fun(n):
    if (n > 0):
        print(n, end=" ")

        # last statement in the function 
        fun(n -1)

# driver code
x = 3
fun(x)

# convert tail recursion into loop and compare each other in terms of time and space complexity

def fun(y):
    while(y > 0):
        print(y, end = " ")
        y -= 1

# driver code
y = 3
fun(y)

# head recursion: if a recursion function calling itself and that recursive call is the first statement in the function then it is known as Head recursion
# There is no statement no operation before the call. The function doesnt have to process or performany operation at the time of calling and all operations are done at returning tume

# head recursion 
def head(n):
    if (n > 0):

        # first statement in the function
        fun(n-1)
        print(n , end = " ")

# drive code
n = 3
head(n)

# converting head recursion to iteration. 
def convertHeadToIteration(n):

    i = 1
    while (i <=n):
        print(i, end = " ")
        i += 1

n = 7
convertHeadToIteration(n)

# tree recursion: to understand tree recursion let first understand linear recursion - if a recursion function calling itself for one time then it's known as linear recursion. otherwise if a recursive function calling itself for more than one time then it is known as tree recursion

def treeRecursion(n):
    if (n > 0):
        print(n, end = " ")

        # calling once
        treeRecursion(n-1)

        # calling twice
        treeRecursion(n-1)

treeRecursion(6)

# nested recursion ~ in this recursion a recursive function will pass the parameter as a recursive call. That means (recursion inside recursion)
def nestedRecursion(n):
    if (n > 100):
        return n - 10
    
    # a recursive function passing parameter as a recursive call or recursion inside the recursion
    return nestedRecursion(nestedRecursion(n + 11))

runNestedRecursion = nestedRecursion(95)
print(" ", runNestedRecursion)