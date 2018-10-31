#Complete the function compareTriplets in the editor below. It must return an array of two integers, the first being Alice's score and the second being Bob's.

# compareTriplets has the following parameter(s):

# a: an array of integers representing Alice's challenge rating
# b: an array of integers representing Bob's challenge rating






import sys


a0,a1,a2 = input().strip().split(' ')
A = a0,a1,a2 = [int(a0),int(a1),int(a2)]
b0,b1,b2 = input().strip().split(' ')
B = b0,b1,b2 = [int(b0),int(b1),int(b2)]
alice = bob = 0
for x,y in zip(A,B):
    if x>y: alice += 1
    if x<y: bob += 1
print (alice,bob)