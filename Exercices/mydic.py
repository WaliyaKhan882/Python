print("Welcome to MyDictionary to get knowledge about countries' capitals")
Dic={"Pakistan": "Islamabad", "Turkey":"Istanbul","Germany":"Berlin","France":"Paris","India":"New Dehli","China":"Beijing"
     ,"Russia":"Moscow","Afghanistan":"Kabul","Bangladesh":"Dhaka","Iran":"Tehran"}
print("Please Enter the Country Name")
country = input()
print("The Capital of this country is",end=" ")
print(Dic[country])
