def multiply_digits_until_single(n):
    while n > 9:
        product = 1
        for digit in str(n):
            product *= int(digit)
        n = product
    return n

# Ввід користувача
number = int(input("Введіть ціле число: "))

# Перевірка на від'ємність або нецілі числа — додатково (за бажанням)
if number < 0:
    print("Будь ласка, введіть додатнє число.")
else:
    result = multiply_digits_until_single(number)
    print(f"Результат: {result}")