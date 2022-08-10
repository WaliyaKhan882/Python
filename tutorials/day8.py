list1= [["harry",6], ["carry",8],["marrie",10], ["larry",2]]
for items in list1:
    print(items)
for items,cookies in list1:
    print(items,"eats",cookies,"cookies")
dict1= dict(list1)
print(type(dict1))
for items in dict1.items():
    print(items)
for cookies in dict1.values():
    print(cookies)
for items,cookies in dict1.items():
    print(items, "eats", cookies, "cookies")
for items in dict1.keys():
    print(items)

