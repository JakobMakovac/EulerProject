600851475143
main_number = int(input("Input your number:"))


def trial_division(main_number: int) -> list[int]:
    """Return a list of the prime factors for a natural number."""
    prime_factors = []               # Prepare an empty list.
    factor = 2                # The first possible factor.    
    while main_number > 1:         # While n still has remaining factors...
        if main_number % factor == 0:   # The remainder of n divided by f might be zero.        
            prime_factors.append(factor)  # If so, it divides n. Add f to the list.
            main_number //= factor      # Divide that factor out of n.
        else:            # But if f is not a factor of n,
            factor += 1       # Add one to f and try again.
    return prime_factors             # Prime factors may be repeated: 12 factors to 2,2,3.

largest = 0
for number in trial_division(main_number):
    if number > largest:
        largest = number
    
print(number)