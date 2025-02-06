class PrimeNumbers:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __iter__(self):
        return self.prime_generate()

    def prime_generate(self):
        for num in range(self.start, self.end + 1):
            if self.is_prime(num):
                yield num

    def is_prime(self, num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

primes = PrimeNumbers(10,50)
for p in primes:
    print(p, end = " ")