number=10
if number < 10:
    print("1.true")
else:
    print("1.false")

if number < 100:
    print("2.true")
else:
    print("2.false")

if number %2==0:
    print("3.true")
else:
    print("3.false")

oszto=5
if number % oszto ==0:
    print("4.true osztoja numbernek")
else:
    if oszto % number == 0:
        print("4.true number osztoja")
    else:
        print("4.false")


str1="Ez egy teszt szoveg"
str2="Ez a masik teszt szovege"

if str1.startswith(str2[0]):
    print("5.A ket szoveg elso karaktere megegyezik")
else:
    print("5.A ket szoveg elso karaktere nem egyezik meg")

if str1.endswith(str2[-1]):
    print("5.A ket szoveg utolso karaktere megegyezik")
else:
    print("5.A ket szoveg utolso karaktere nem egyezik meg")

if number != 0:
    if number >= 1:
        print("6.A szam pozitiv")
    else:
        print(".A szam negativ")
else:
    print("6.A szam 0")

if str1[0].isupper():
    print("7.true")
else:
    print("7.false")


nums = [1, 2, 3]
legk = nums[0]
legn = nums[0]
for x in nums:
    if x>legn:
        legn=x
    elif x < legk:
            legk = x

print(legk,legn)

char = "A"
maganhangzok=["a","á","e","é","i","í","o","ó","ö","ő","u","ú","ü","ű"]
if char.lower() in maganhangzok:
    print("true")

elif char.isnumeric():
    print("number")
else:
    print("false")










