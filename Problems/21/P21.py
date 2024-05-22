def sum_divisors(number: int) -> int:
    divisors = []
    for i in range(1, (number // 2) + 2):
        if number % i == 0:
            divisors.append(i)

    return sum(divisors)

def get_divisor_sum(cache: dict[int], number: int) -> int:
    cache_key = str(number)
    if cache_key in cache:
        return cache[cache_key]
    else:
        sum = sum_divisors(number)
        cache[cache_key] = sum
        return sum


sums_by_number = {}

amicable_set = set()

for a in range(10000):
    da = get_divisor_sum(sums_by_number, a)
    db = get_divisor_sum(sums_by_number, da)

    if db == a and a != da:
        amicable_set.add(da)
        amicable_set.add(a)

print(list(amicable_set))