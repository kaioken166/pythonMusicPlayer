class Number:
    @staticmethod
    def gcd(a, b):
        if b == 0:
            return a
        return Number.gcd(b, a % b)

    @staticmethod
    def lcm(a, b):
        return a * b // Number.gcd(a, b)

    @staticmethod
    def sumdivisor(n):
        res = 0
        for i in range(1, n + 1):
            if n % i == 0:
                res += i
        return res


number = Number()
print(number.gcd(12, 16))       # 4
print(number.lcm(12, 16))       # 48
print(number.sumdivisor(12))    # 28
