# Rozwiązanie dla zadań z klasy Account, Roman, Vector, oraz Polynomial

# Zadanie 1: Klasa Account
class Account:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount > self.balance:
            print("Niewystarczające środki.")
        else:
            self.balance -= amount

    def transfer(self, other_account, amount):
        if amount > self.balance:
            print("Niewystarczające środki do przelewu.")
        else:
            self.withdraw(amount)
            other_account.deposit(amount)

class PrivateAccount(Account):
    def __init__(self, owner, balance, salary):
        super().__init__(owner, balance)
        self.salary = salary

    def receive_salary(self):
        self.deposit(self.salary)

class FirmAccount(Account):
    def __init__(self, owner, balance, zus_payment):
        super().__init__(owner, balance)
        self.zus_payment = zus_payment

    def pay_zus(self):
        self.withdraw(self.zus_payment)

# Test Account
pa = PrivateAccount("Anna", 1000, 3000)
fa = FirmAccount("Firma ABC", 5000, 1500)

pa.receive_salary()
print(f"Stan konta prywatnego: {pa.balance}")
fa.pay_zus()
print(f"Stan konta firmowego: {fa.balance}")

# Zadanie 2: Klasa Roman
class Roman:
    roman_map = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

    def __init__(self, roman):
        self.roman = roman
        self.value = self.to_integer()

    def to_integer(self):
        total = 0
        prev_value = 0
        for char in reversed(self.roman):
            current_value = self.roman_map[char]
            if current_value < prev_value:
                total -= current_value
            else:
                total += current_value
            prev_value = current_value
        return total

    def __add__(self, other):
        return Roman.from_integer(self.value + other.value)

    def __sub__(self, other):
        return Roman.from_integer(self.value - other.value)

    def __mul__(self, other):
        return Roman.from_integer(self.value * other.value)

    @classmethod
    def from_integer(cls, number):
        roman_numerals = ""
        for symbol, value in sorted(cls.roman_map.items(), key=lambda x: x[1], reverse=True):
            while number >= value:
                roman_numerals += symbol
                number -= value
        return cls(roman_numerals)

    def __str__(self):
        return self.roman

# Test Roman
r1 = Roman("X")
r2 = Roman("V")
print(f"Dodawanie: {r1 + r2}")
print(f"Odejmowanie: {r1 - r2}")
print(f"Mnożenie: {r1 * r2}")

# Zadanie 3: Klasa Vector
class Vector:
    def __init__(self, values):
        self.values = values

    def __add__(self, other):
        return Vector([a + b for a, b in zip(self.values, other.values)])

    def __sub__(self, other):
        return Vector([a - b for a, b in zip(self.values, other.values)])

    def __mul__(self, scalar):
        return Vector([x * scalar for x in self.values])

    def __str__(self):
        return str(self.values)

# Test Vector
v1 = Vector([1, 2, 3])
v2 = Vector([4, 5, 6])
print(f"Dodawanie wektorów: {v1 + v2}")
print(f"Odejmowanie wektorów: {v1 - v2}")
print(f"Mnożenie wektora przez skalar: {v1 * 3}")

# Zadanie 4: Klasa Polynomial
class Polynomial:
    def __init__(self, coefficients):
        self.coefficients = coefficients

    def __str__(self):
        result = ""
        for i, coeff in enumerate(reversed(self.coefficients)):
            if coeff == 0:
                continue
            sign = " + " if coeff > 0 and i > 0 else ""
            power = len(self.coefficients) - i - 1
            term = f"{coeff}x^{power}" if power > 1 else (f"{coeff}x" if power == 1 else f"{coeff}")
            result += f"{sign}{term}"
        return result

    def degree(self):
        return len(self.coefficients) - 1

    def __getitem__(self, index):
        return self.coefficients[index]

    def __mul__(self, other):
        result = [0] * (len(self.coefficients) + len(other.coefficients) - 1)
        for i, a in enumerate(self.coefficients):
            for j, b in enumerate(other.coefficients):
                result[i + j] += a * b
        return Polynomial(result)

    def evaluate(self, x):
        return sum(coeff * (x ** i) for i, coeff in enumerate(self.coefficients))

# Test Polynomial
p1 = Polynomial([3, -1, 1, 2])  # 3x^3 - x^2 + x + 2
p2 = Polynomial([1, 0, -1])  # x^2 - 1
print(f"Wielomian p1: {p1}")
print(f"Stopień p1: {p1.degree()}")
print(f"Mnożenie p1 i p2: {p1 * p2}")
print(f"Wartość p1 dla x=2: {p1.evaluate(2)}")
