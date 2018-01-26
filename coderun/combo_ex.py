import random
import sys
import os


dirname = sys.argv[1]
lowerlimit = int(sys.argv[2])
upperlimit = int(sys.argv[3])

file = open(os.getcwd() + '/media/' + dirname + '/data.txt', 'r')
file1 = open(os.getcwd() + '/media/' + dirname + '/result.txt', 'w')
combined = {}
products = []
price = []

for i in file:
    s = i.split(',')
    s[1] = int(s[1])
    combined[s[0]] = s[1]
    products.append(s[0])
    price.append(s[1])
print(combined)
print(products)
print(price)
noi = 1000
size = 3
lpr = lowerlimit
upr = upperlimit
res = set()
for i in range(noi):
    chro = sorted(random.sample(products, size))
    prchro = [combined[x] for x in chro]
    prchro = sorted(prchro)
    if lpr <= sum(prchro) <= upr:
        res.add(tuple(chro))
        file1.write(str(chro) + ' with price    ' + str(sum(prchro)) + '\n')
print(res)
print(len(res))
