# Sieve of Eratosthenes

stop = 101
numbers = [None, None] + list(range(2, stop))

for sieve in range(2, stop):
    start = 2 * sieve
    skip = sieve
    for i in range(start, stop, skip):
        numbers[i] = None

primes = []
for n in numbers:
    if n:
        primes.append(n)

print(primes)
