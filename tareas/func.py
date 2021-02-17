'''
def g(a):
   s = 0
   while a>0:
       d = a%10
       a = a//10
       s = s*10 + d
   return s

r = int(input())
r2 = g(r)
print(r2)
'''


'''
def f(x,y):
   return x==y

def g(a):
   s = 0
   while a>0:
       d = a%10
       a = a//10
       s = s*10 + d
   return s

r = 365
r2 = g(r)
print(f(r,r2))
'''


def f2(y, z):
    return y % z == 0


def f1(x):
    s = 0
    i = 1
    while i < x:
        if f2(x, i) is True:
            s += i
        i += 1
    return x == s


a = 28
if f1(a):
    print("Es")
else:
    print("No es")
