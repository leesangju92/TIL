def sum_digits(n, sum=0):
    if n < 10:
        return sum + n
    else:
        digit_n = 0
        nameogi = 0
        number_length = len(str(n))
        digit_n = n // (10**(number_length-1))
        nameogi = n % (10**(number_length-1))
        sum += digit_n
        return sum_digits(nameogi, sum)




print(sum_digits(345))
