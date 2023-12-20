#example (bitwise operators)
x=8
y=9
print(x&y)

a=15
b=19
print(a&b)

x=8
y=9
print(x|y)

a=10 
b=12
print(a|b)

a=11
b=12
print(a|b)


a=12
b=14
print(a|b)

a=10
b=14
print(a**b)

a=5
b=8
print(a%b)

a=4
b=6
print(a//b)

a=6
b=10
print(~a)
print(a^b)


#identity operators (is and isnot operators)

x=5
print(type(x))
print(type(x) is int)

x="ankit"
print(type(x))
print(type(x) is float)

#is not operator
x=5.5
print(type(x) is not float)
print(type(x) is float)


#operator precedence(example)
#left-right associativity
#output:3
print(5*2//3)

#shows left right associativity
#output:0
print(5*(2//3))

#shows the left right associativity of**
#output:512,since 2**(3**2)=2**9
print((2**3)**2)


print((2*3**5))
print(2**(3**2))
print(5*(8**2))
print(40/(3**5))
print((20)/(2**6))
print(10-(4**3))
print((20**2)/(4*2))