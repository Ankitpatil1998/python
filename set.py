#creating the set
Days={"monday","tuesday","wednesday","thrusday","friday","saturday","sunday"}
print(Days)

#adding the element
fruits={"apple","banana","mango","grapes"}
print(fruits)

fruits.add("banana")
print(fruits)
fruits.update("kiwi")
print(fruits)

#remove
fruits={"apple","banana","cherry","kiwi","grapes"}
print(fruits)
fruits.discard("apple")
print(fruits)

fruits.remove("cherry")
print(fruits)

#pop
fruits.pop()
print(fruits)   


#operators 
#operations
my_set= {1,2,3,4}
my_set2={3,4,5,6}
print(my_set.union(my_set2))
print(my_set|my_set2)

print(my_set.intersection(my_set2))
print(my_set&my_set2)

print(my_set.difference(my_set2))
print(my_set-my_set2)

print(my_set.symmetric_difference(my_set2))
print(my_set^my_set2)

#check is subset
a={4,5}
b={1,2,3,4,5}
a.issubset(b)
print(a.issubset(b))
print(b.issubset(a))

#check if a set is subset,using comparison operators
a=('a','b')
b=('a','b','c')
print(a<=b)
print(b<=a)

#in and not in
s={5,7,9}
print(5 in s)
print(6 in s)