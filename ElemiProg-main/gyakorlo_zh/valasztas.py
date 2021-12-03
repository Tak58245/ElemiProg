import kepviselo

# 1.feladat
szavazatok = []
fpath = "szavazatok.txt"
f = open(fpath, "r")
c = 0
with open(fpath) as f:
    for line in f:
        stripped_line = line.strip()
        i = stripped_line.split()
        szavazatok.append(kepviselo.Képviselőjelölt(i[0], i[1], i[2], i[3], i[4]))

# 2.feladat
print("2.feladat")
print(len(szavazatok))

# 3.feladat
print("3.feladat")
# nev = input("Adja meg a képviselő nevét: ")
nev = "a"

i = 0
while i < len(szavazatok) and nev != szavazatok[i].jelolt_Neve:
    i = i + 1

if i < len(szavazatok):
    print(
        szavazatok[i].jelolt_Neve + " nevu jelolt " + str(szavazatok[i].szavazatok_Szama) + " szamu szavazatot kapott")
else:
    print("Nincs ilyen nevu jelolt")

# 4.feladat
print("4.feldat")
jogosultak = 12345
j = 0
szvazatok_Szama = 0

while j < len(szavazatok):
    szvazatok_Szama = szvazatok_Szama + szavazatok[j].szavazatok_Szama
    j = j + 1

szvazatok_Aranya = (szvazatok_Szama / jogosultak) * 100

print("A szavazaton %d ember vett reszt,a szavazo arany %.2f%%" % (szvazatok_Szama, szvazatok_Aranya))

# 5.feladat
print("5.feladat")

partok = {"GYEP": ["Gyümölcsevők Pártja", 0],
          "HEP": ["Húsevők Pártja", 0],
          "TISZ": ["Tejivók Szövetsége", 0],
          "ZEP": ["Zöldségevők Pártja", 0],
          "-": ["Független jelöltek", 0]}

k = 0
while k < len(szavazatok):
        partok.get(szavazatok[k].tamogato_Párt)[1] += szavazatok[k].szavazatok_Szama
        k = k + 1

for i in partok.values():
    print("%s= %.2f%%"%(i[0],((i[1]/szvazatok_Szama)*100)))

#6.feladat

