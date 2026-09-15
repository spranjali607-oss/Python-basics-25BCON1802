import random

num = random.randint(1, 10)

print("Multiplication Table of", num)

for i in range(1, 11):
    print(num, "x", i, "=", num * i)