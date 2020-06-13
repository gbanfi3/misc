'''
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
Find the sum of all the multiples of 3 or 5 below 1000.
'''
lim = 1000
sum = 0
for i in range(1,lim):
    if not i % 3:
        sum +=i
        continue
    if not i % 5:
        sum +=i
print(sum)