l1= ["waliya", "Abeeha", "Hafsa", "Arfa", "Maryam"]
l2 =[5,7,9,10,2]
print(l1)
print(l1[2])
l2.sort()
l2.reverse()
print(l2)
a = l2[2]
b = l2[4]
a,b = b,a
print(a,b)
print(len(l1))
l2.append(8)
print(l2)
l2.remove(10)
print(l2)    #list is mutable
l3=l1.copy()
del l3[2]
print(l1)
print(l3)
l2.insert(2,6)
print(l2)
l2.pop(4) #remove a specific index from the list
print(l2)
t1=(1,2,3) #tuple immutable cannot change
print(type(t1))
print(t1)

