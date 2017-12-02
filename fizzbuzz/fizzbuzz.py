#
# Print the numbers from 1 to 100, but print "fizz" instead of the number for
# multiples of 3, print "buzz" instead of the number for multiples of 5, and
# print "fizzbuzz" instead of the number for multiples of both 3 and 5.
#

for i in range(1, 101):
    x = ''
    if i % 3 == 0:
        x = 'fizz'
    if i % 5 == 0:
        x += 'buzz'
    if not x:
        x = i
    print(x)
