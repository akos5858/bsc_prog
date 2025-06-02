egysegar1, egysegar2, egysegar3 = map(float, input().split()) 
szallitasi_koltseg, hatar = map(float, input().split()) 
darabszam = int(input())

if darabszam < 10: ertek = darabszam*egysegar1
elif darabszam < 100: ertek = darabszam*egysegar2
else: ertek = darabszam*egysegar3

if ertek < hatar: szallitasi_koltseg = szallitasi_koltseg
else: szallitasi_koltseg = 0

vegosszeg = ertek + szallitasi_koltseg

print(ertek)
print(szallitasi_koltseg)
print(vegosszeg)          
