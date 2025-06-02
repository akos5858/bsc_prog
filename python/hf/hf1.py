n = int(input())

s = str(bin(n))
s2 = s[2:]
s3 = s[2:][::-1]
num = int(s3, base=2)
dif = (len(str(bin(n)))-len(str(bin(num))))

n2 = n - 2**dif

print(n2)