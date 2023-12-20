dog={'name':'jax','age':'15','colour':'brown'}
print(dog)

#add an item
dog['weight']=90
print(dog)

#modify the value
dog['age']=10
print(dog)

#length of dictionary
print(len(dog))

#only keys
print(dog.keys())

#only values
print(dog.values())

#get items
print(dog.items())

#removing the items
dog.pop('colour')
print(dog)

dog.popitem()
print(dog)

del dog['age']
print(dog)

dog.clear()
print(dog)


#frozenset
nu=(1,2,3,4,5,6,7,8,9)
fnum=frozenset(nu)
print("frozenset object is:",fnum)

va=("a,b,c,d,e,f,g")
fvar=frozenset(va)
print("frozenset of variable is:",fvar)