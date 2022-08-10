d1= {"Waliya":"Plum", "Abeeha":"Black", "Abba":"White", "Maida":"Red"}
print(d1)
print(d1["Waliya"])
print(d1.keys())
print(d1.items())
print(d1.values())
d1["Ammi"]="green"
d1[420]="Chor Nani"
print(d1)
print(d1["Abeeha"])
del d1[420]
print(d1)
d2=d1.copy()
del d2["Abeeha"]
print(d1)
print(d2)
d3=d1
del d3["Abeeha"]
print(d1)
print(d3)