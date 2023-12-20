thistuple=("apple","banana","cherry")
print(thistuple)

#tuple length
print(len(thistuple))

#access tuple items
thistuple=("apple","banana","cherry","mango")
print(thistuple[1])
print(thistuple[-2])

#range of values
thistuple=("apple","banana","cherry","mango","kiwi","melon","orange")
print(thistuple[2:5])
print(thistuple[2:4])
print(thistuple[1:5])

#when starting value is not specified
thistuple=("apple","banana","cherry","mango","kiwi","melon","orange")
print(thistuple[:5])
print(thistuple[2:4])
print(thistuple[:4])

#negative range
thistuple=("apple","banana","cherry","mango","kiwi","melon","orange")
print(thistuple[-1:-5])
print(thistuple[-2:-4])
print(thistuple[-6:-2])
print(thistuple[-4:-1])

#change tuple values 
x=("apple","banana","cherry")
y=list(x)
y[1]="kiwi"
x=tuple(y)
print(x)

y=list(x)
y[2]="mango"
x=tuple(y)
print(x)

y=list(x)
y[0]="pineapple"
x=tuple(y)
print(x)

#adding items
x=("apple","banana","cherry")
y=list(x)
y.append("orange")
x=tuple(y)
print(x)

y=list(x)
y.append("kiwi")
x=tuple(y)
print(x)

y=list(x)
y.append("pineapple")
x=tuple(y)
print(x)

#remove the items
x=("apple","banana","cherry")
y=list(x)
y.remove("cherry")
x=tuple(y)
print(x)

y=list(x)
y.remove("banana")
x=tuple(y)
print(x)


#unpacking the tuple 
fruits=("apple","banana","cherry")
(green,yellow,red)=fruits
print(green)
print(yellow)
print(red)

#count and index
fruits=("apple","banana","cherry","apple","apple")
print(fruits.count("apple"))
print(fruits.index("apple"))

#To delete the tuple completely
x=("apple","banana","cherry")
del(x)
print(x)
