DP = [0 for _ in range(250)]
DP[0] = 1

for i in range(1, 250251):
    power = pow(i, i, 250)    # = i^i mod 250, kiszamoljuk a maradekot
    DP = [ (value + DP[(idx - power) % 250]) % 1e16 for (idx, value) in enumerate(DP) ]  
    # frissitjuk a tombot
     
    # kicsit gyorsabb, ha floattal dolgozunk integer helyett de ugyanazt adja

print(f' a megfelelo reszhalmazok szamanak utolso 16 szamjegye: {int(DP[0] - 1)}' )

# output: -> a megfelelo reszhalmazok szamanak utolso 16 szamjegye: 1425480615190209
# futasido: 8 sec