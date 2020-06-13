'''
https://projecteuler.net/problem=3
The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143 ?
'''
import logging
logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')
# szam = 3*3*91*5*7*7*19*29*29*19
szam = 600851475143
# szam = 600881475143
n = szam

ig = n
primes = []
i_primes = -1
i = 1
hany = 0
while True:
    if i >= ig:
        break
    i += 1
    if not n % i: # osztható
        hany += 1
        primes.append([i,1,i])
        i_primes += 1
        ig /= i
        n = n / i
        while not n % i:
            primes[i_primes][1] += 1
            primes[i_primes][2] *= i
            ig /= i
            n = n/i
        print("új prim: %s" % i)

j = 1
for i in range(len(primes)):
    j *= primes[i][2]

print("szam:    %s" % szam)
print("szorzat: %s" % j)
print(primes)
print(hany)