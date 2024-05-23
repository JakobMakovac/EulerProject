def is_palindrome(number: int) -> bool:
    return str(number) == str(number)[::-1]

largest = 0

for i in range(1000, 1, -1):
    for j in range(1000, 1, -1):
        multiple = i * j
        if multiple > largest and is_palindrome(multiple):
            largest = multiple

print(largest)