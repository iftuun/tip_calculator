print("Welcome to tip Calculator......")
n =float(input("What was the total bill? $"))
m=float(input("How many people to split the bill? : "))
o=float(input("What percentage of tips you would like to give? 10, 12, 15 or more (please mention %): "))
p= (n+((n*o)/100))
q= (p/m)


formatted_float = "{:.2f}".format(p)
print("So, you wanna tip $:",formatted_float)

#print(formatted_float)

formatted_float1 = "{:.2f}".format(q)
print("Each person should pay $: ",formatted_float1 )

#print(formatted_float)