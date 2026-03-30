a = int(input("Enter a number"))
b = int(input("Enter another number"))
c = int(input("Enter another number"))
avg = a + b + c / 3
print(avg , "is your numbers average")
if avg > a and avg > b and avg > c:
    print("Avg is greater thn a,b and c")
elif avg > a and avg > b:
    print('Avg is greater than a and b')
elif avg > a and avg > c:
    print("Avg is greater than a and c")
elif avg > b and avg > c:
    print("Avg is greater than b and c")
elif avg > a:
    print("Avg is just greater than a")
elif avg > b:
    print("Avg is just greater than b")
elif avg > c:
    print("Avg is just greater than c")
else:
    print("INVALID INPUT!!!!!!!!!!!!!")