price = int(input("Add meg a termék árát: \n"))
if price <= 10000:
     price = (price/100) * 80
     print("A termékre 20% kedvezmény vonatkozik, a termék kedvezményes ára:", price)
else:
    price = (price / 100) * 90
    print("A termékre 10% kedvezmény vonatkozik, a termék kedvezményes ára:", price,)

