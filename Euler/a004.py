'''
https://projecteuler.net/problem=4
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
Find the largest palindrome made from the product of two 3-digit numbers.
'''

list9 = [993,983,973,963,953]

for i in range(999999,900009,-1):
    for j in list9:
        if not i % j:
            print("ez az: %s" % j)
