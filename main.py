from gen_pr import *
from math import gcd

p = pr_num()
q = pr_num()
while True:
    if p == q:
        q = pr_num()
    else:
        break

n = p*q

phi = (p-1)*(q-1)


for i in range(phi):
    if i > 20 and gcd(i, phi) == 1 and i % 2 != 0 and "False" not in miller(i):
        e = i
        break

#print(phi)
#print(e)
#print('НОД = '+str(gcd(phi, e)))

d = pow(e, -1, phi)

print('p = ' + str(p))
print('q = ' + str(q))
print('n = ' + str(n))
print('phi = ' + str(phi))
print('e = ' + str(e))
print('НОД = '+str(gcd(phi, e)))
print('d = ' + str(d))


with open('C:\\Users\\kalma\\Desktop\\rsa.txt', 'r', encoding='utf-8') as file:
    full_book = file.read()
a = full_book
z = [ord(i) for i in a]
shifr = [pow(m, e, n) for m in z]
j = ' '.join(map(str, shifr))

f = open('C:\\Users\\kalma\\Desktop\\encr.txt', 'w', encoding='utf-8')
f.write(str(j))
f.close()


with open('C:\\Users\\kalma\\Desktop\\encr.txt', 'r', encoding='utf-8') as file:
    full_book = file.read()
a = full_book
desh_1 = ''

l = ''
for i in range(len(a)):
    if a[i] == ' ':
        x = pow(int(l), d, n)
        desh_1 += chr(x)
        l = ''
    elif i == len(a)-1:
        l += a[i]
        x = pow(int(l), d, n)
        desh_1 += chr(x)
    else:
        l += a[i]

f = open('C:\\Users\\kalma\\Desktop\\decr.txt', 'w', encoding='utf-8')
f.write(str(desh_1))
f.close()