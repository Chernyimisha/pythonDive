import fractions

frac1 = "1/2"
frac2 = "1/3"


def summa_fractions(frac1, frac2):
    numerator1 = int(frac1.split("/")[0])
    numerator2 = int(frac2.split("/")[0])
    denominator1 = int(frac1.split("/")[1])
    denominator2 = int(frac2.split("/")[1])
    res = ''

    if denominator1 != denominator2:
        min_denominator = min(denominator1, denominator2)
        max_denominator = max(denominator1, denominator2)
        if min_denominator == denominator1:
            numerator_min = numerator1
            numerator_max = numerator2
        else:
            numerator_min = numerator2
            numerator_max = numerator1
        counter1 = min_denominator
        counter2 = max_denominator
        while True:
            counter1 += min_denominator
            if counter1 < counter2:
                continue
            elif counter1 == counter2:
                res = str(numerator_min * counter1 // min_denominator + numerator_max *
                          counter2 // max_denominator) + '/' + str(counter1)
                break
            else:
                counter2 += max_denominator
    else:
        res = str(numerator1 + numerator2) + '/' + str(denominator1)
    return res


def multi_fractions(frac1, frac2):
    numerator1 = int(frac1.split("/")[0])
    numerator2 = int(frac2.split("/")[0])
    denominator1 = int(frac1.split("/")[1])
    denominator2 = int(frac2.split("/")[1])
    res = str(numerator1 * numerator2) + '/' + str(denominator1 * denominator2)
    return res


summ_res = summa_fractions(frac1, frac2)
milti_res = multi_fractions(frac1, frac2)

print(f'Сумма дробей: {summ_res}')
print(f'Произведение дробей: {milti_res}')
print(f'Сумма дробей: {fractions.Fraction(frac1) + fractions.Fraction(frac2)}')
print(f'Произведение дробей: {fractions.Fraction(frac1) * fractions.Fraction(frac2)}')

# Сумма дробей: 5/6
# Произведение дробей: 1/6
# Сумма дробей: 5/6
# Произведение дробей: 1/6
