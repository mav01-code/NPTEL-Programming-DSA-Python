# Reverse of a Number
"""
n = int(input())
rev = 0
while n!=0:
    rev = rev*10+n%10
    n//=10
print(rev)
"""

# Matching Brackets
"""
s = input()
sum = 0
for i in range(len(s)):
    if (s[i]==")"):
        sum+=1
    elif (s[i]=="("):
        sum-=1
if(sum==0):
    print(True)
else:
    print(False)
"""

# Sum of Prime Numbers in a List
def factors(n):
    factorlist = []
    for i in range(1,n+1):
        if n%i==0:
            factorlist.append(i)
    return factorlist
def isPrime(n):
    return factors(n)==[1,n]
def sumOfPrimes(l):
    sum = 0
    for i in range(len(l)):
        if(isPrime(l[i])):
            sum+=l[i]
    return sum
l = [11,11,11,13,11,-11]
print(sumOfPrimes(l))