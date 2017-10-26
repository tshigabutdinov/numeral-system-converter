import sys

from_ns = int(sys.argv[1])
new_ns = int(sys.argv[2])

my_number_raw = str(raw_input("Please, input number: "))

symbol_to_num = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5,
                 '6': 6, '7': 7, '8': 8, '9': 9, 'a': 10, 'b': 11,
                 'c': 12, 'd': 13, 'e': 14, 'f': 15, 'g': 16, 'h': 17,
                 'i': 18, 'j': 19, 'k': 20, 'l': 21, 'm': 22, 'n': 23,
                 'o': 24, 'p': 25, 'q': 26, 'r': 27, 's': 28, 't': 29,
                 'u': 30, 'v': 31, 'w': 32, 'x': 33, 'y': 34, 'z': 35}

num_to_symbol = {0: '0', 1: '1', 2: '2', 3: '3', 4: '4', 5: '5',
                 6: '6', 7: '7', 8: '8', 9: '9', 10: 'a', 11: 'b',
                 12: 'c', 13: 'd', 14: 'e', 15: 'f', 16: 'g', 17: 'h',
                 18: 'i', 19: 'j', 20: 'k', 21: 'l', 22: 'm', 23: 'n',
                 24: 'o', 25: 'p', 26: 'q', 27: 'r', 28: 's', 29: 't',
                 30: 'u', 31: 'v', 32: 'w', 33: 'x', 34: 'y', 35: 'z'}


def to_dec_frac(base, number_string):
    """Convert fractional part of number with given base to decimal fraction"""
    splited_number_string = list(number_string)
    exponent = 1
    result = 0
    for digit in splited_number_string:
        result += 1.0 / pow(base, exponent) * symbol_to_num[digit]
        exponent += 1
    return result


def to_ns_frac(base, dec_fraction):
    """convert decimal fraction to fraction with given base"""
    result = list()
    for exponent in range(1, 14):
        p = 1.0 / pow(base, exponent)
        digit = int(dec_fraction / p)
        result.append(num_to_symbol[digit])
        dec_fraction -= int(dec_fraction / p) * p
    return ''.join(result)


def to_dec_int(base, number_string):
    """Convert to decimal from any given numeric system with given base (2-36)"""

    result = 0
    l = list(number_string)

    for i in range(len(l)):
        digit = symbol_to_num[l.pop()]
        result += digit * pow(base, i)

    return result


def to_ns_int(base, dec_number):
    """Convert decimal number to any given numeric system with given base (2-36)"""

    exponent = 1
    power_table = list()
    while True:
        power_table.append((exponent, pow(base, exponent)))
        exponent += 1
        if pow(base, exponent) > dec_number:
            break

    temp_result = list()
    for i in range(len(power_table)):
        power, ns_in_power = power_table.pop()
        positional_num = dec_number / ns_in_power
        dec_number = dec_number - ns_in_power * positional_num
        temp_result.append(positional_num)

    result = list()
    for item in temp_result:
        result.append(num_to_symbol[item])

    result_string = ''.join(result) + num_to_symbol[dec_number]
    # Hack with removing '0' for 'short' numbers
    return result_string.lstrip('0')


# converted_to_dec = int (to_dec(from_ns, my_number))
# print to_ns(new_ns, converted_to_dec)


if '.' in my_number_raw:
    my_number_int, my_number_frac = my_number_raw.split('.')
    my_temp_dec_int = to_dec_int(from_ns, my_number_int)
    my_temp_dec_frac = to_dec_frac(from_ns, my_number_frac)
    print to_ns_int(new_ns, my_temp_dec_int) + '.' + to_ns_frac(new_ns, my_temp_dec_frac)

else:
    my_temp_dec_int = to_dec_int(from_ns, my_number_raw)
    result = to_ns_int(new_ns, my_temp_dec_int)
    print result
