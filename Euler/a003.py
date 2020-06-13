'''
https://projecteuler.net/problem=3
The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143 ?
'''
import logging
logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')

# n = 1*3*5*11
# primes = [2,3,5]
# max_prim = primes[len(primes) - 1]
# # logging.INFO(str(primes))
# while True:
#     for i in range(max_prim+1, max_prim*20):
#         for j in primes:
#             oszthato = False
#             if not i % j:   # ha osztható egyik prímmel
#                  oszthato = True
#                  break
#         if not oszthato:
#             primes.append(i)
#             # logging.INFO("added: %s" % i)
#             # logging.INFO(str(primes))
#     # logging.INFO("eddig ennyi: %s" % str(primes))
#     max_prim = primes[len(primes) - 1]
#     if max_prim >= n:
#         break
# print(primes)



# n = 2*3*5*11*23
szam = 3*3*3*5*7*7*19*29*29
n = szam

ig = n
primes = []
i_primes = -1
i = 1
while True:
    if i >= ig:
        break
    i += 1
    if not n % i: # osztható
        primes.append([i,1,i])
        i_primes += 1
        ig /= i
        m = n / i
        while not m % i:
            primes[i_primes][1] += 1
            primes[i_primes][2] *= i
            ig /= i
            m = m/i
        print("új prim: %s" % i)

print(primes)