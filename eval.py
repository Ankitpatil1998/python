#evaluating expression - using eval function
evaluate= 'x*(x+1)*(x+2)'
print(type(evaluate))
x=3
expression=eval(evaluate)

print(expression)
             
evaluate='(x*y)+(3*x+2*y)*4*x'
x=4
y=2
expression=eval(evaluate)
print(expression)