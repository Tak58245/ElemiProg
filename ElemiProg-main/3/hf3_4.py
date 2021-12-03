age1 = int(input("Add meg a korod: "))
gender1 = input("Add meg hogy fiu(m) vagy lány(f) vagy: ")

if (age1 >= 10 and age1 <= 12) and (gender1=="f"):
    print("játszhatsz a csapatban")
else:
    print("nem játszhatsz a csapatban")

gender2 = input("Add meg hogy fiu(m) vagy lány(f) vagy: ")
if gender2 == "f":
    age2 = input("Add meg a korod: ")
    if age2 >=  10 and age2 <= 12:
        print("játszhatsz a csapatban")
    else:
        print("nem játszhatsz a csapatban")
else:
    print("nem játszhatsz a csapatban")



