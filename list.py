#list
L1=["data",10,20,30,[2,4,6],[1,3,5]]
print(L1[0][1])
print(L1[3])
print(L1[4][1])
print(L1[5][2])
print(L1[4])
print(L1[0][0:2])
print(L1[5][0:3])
print(L1[4][0:2])

x=["ankit",20,40,60,[4,6,8],[2,3,5]]
print(x[0])
print(x[4][0:2])
print(x[5][1:3])
print(x[0][2:5])
print(x[4][0:2])
print(x[0][0:4])

#list slicing
a=['p','r','o','g','r','a','m','i','z']
print(a[2:5])
print(a[5:])
print(a[:1])
print(a[4:])
print(a[6:])
print(a[3:])
print(a[:6])
print(a[4:7])
print(a[:4])

#changing the item value
odd=[2,4,6,8]

#chnge the first item
odd[0]=1
print(odd)
odd[1]=3
print(odd)
odd[2]=5
print(odd)
odd[3]=2
print(odd)

#chnge 2nd to 4th items
odd[1:4]=[3,5,7]
print(odd)
odd[2:4]=[2,4,6]
print(odd)

#Appending&Extending
odd=[1,3,5]
odd.append(7)

odd.extend([8,10,12])
print(odd)


#insert the item in the list to particular index
fruits=["apple","banana","cherry"]
fruits.insert(1,"orange")
print(fruits)
fruits.insert(2,"mango")
print(fruits)
fruits.insert(3,"pineapple")
print(fruits)
fruits.insert(3,"kiwi")
print(fruits)

#list of numbers
age=[100,3,12,4,56,2,54]
print(age)
print(max(age))
print(min(age))
age.sort()
print(age)
age.sort(reverse=True)
print(age)
a=sum(age)
print('sum is:',(a))

#count
#Return how many items is repeated. 

fruits=("apple","mango","papaya","pineapple","cherry","mango","mango")
print(fruits.count("mango"))
print(fruits.count("apple"))
print(fruits.count("cherry"))

#extracting items fom the list
fruits=['apple','banana','grape','kiwi']
print(fruits[0])
print(fruits[2:3])
print(fruits[0:3])
print(fruits[:3])
print(fruits[2:])
print(fruits[-1])
print(fruits[::-1])
fruits.insert(2,'watermelon')
print(fruits)
fruits.insert(3,'orange')
print(fruits)
print(fruits[::-1])
print(fruits[:3])


#extracting items from the list
fruits=['strawberry','blackberry','pear','melon','grape']
print(fruits[0])
print(fruits[0:2])
print(fruits[1:3])
print(fruits[1:4])
print(fruits[:1])
print(fruits[:-2])
print(fruits[-2])
print(fruits[-1:])
print(fruits[1:])
print(fruits[0:])
print(fruits[2:])
print(fruits[1:5])
print(fruits[-1:])
print(fruits[-3:])
print(fruits[2:-2])
print(fruits[2:-1])