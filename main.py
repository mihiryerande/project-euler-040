# Problem 40:
#     Champernowne's Constant
#
# Description:
#     An irrational decimal fraction is created by concatenating the positive integers:
#         0.123456789101112131415161718192021...
#
#     It can be seen that the 12th digit of the fractional part is 1.
#
#     If d_n represents the nth digit of the fractional part, find the value of the following expression.
#         d_1 × d_10 × d_100 × d_1000 × d_10000 × d_100000 × d_1000000

from typing import List, Tuple


def main(n: int) -> Tuple[List[int], int]:
    """
    Returns the list of digits {d_{10^i}} for `i` in [0, n-1]
      of Champernowne's constant, as well as their product.

    Args:
        n (int): Natural number

    Returns:
        (Tuple[List[int], int]):
            Tuple of ...
              * List of digits {d_{10^i}} for `i` in [0, n-1] of Champernowne's constant
              * Product of those digits

    Raises:
        AssertError: if incorrect args are given
    """
    assert type(n) == int and n > 0

    # Could probably cut down on number of variables, but whatever...
    digits = []  # Accumulated list of found digits
    product = 1  # Accumulated product of found digits

    next_index = 1

    num_size = 1          # Sizes of numbers in consideration (meaning their digit-count)
    num_count = 9         # Count of numbers having `digits_per_num` digits
    const_index_prev = 0                                     # Final index, in const, of numbers already considered
    const_index_range = num_count * num_size                 # Count of const's digits used by nums of `num_size`
    const_index_next = const_index_prev + const_index_range  # Final index in const of numbers currently considered

    while len(digits) < n:
        # Consider digits in const coming from numbers having `num_size` digits
        # Check if the next index we want is somewhere among those
        if const_index_prev < next_index <= const_index_next:
            # Figure out which number within this range holds the desired digit
            num_in_range, digit_of_num = (0, 0) if num_size == 1 else divmod(next_index - const_index_prev, num_size)
            num_actual = 10 ** (num_size - 1) + num_in_range

            # Extract the digit and continue
            next_digit = int(str(num_actual)[digit_of_num-1])
            digits.append(next_digit)
            product *= next_digit
            next_index *= 10
        else:
            # Desired digit not in this range
            # Step range forward to numbers having `num_size`+1 digits
            num_size += 1
            num_count *= 10
            const_index_prev = const_index_next
            const_index_range = num_count * num_size
            const_index_next = const_index_prev + const_index_range

    return digits, product


if __name__ == '__main__':
    num = int(input('Enter a natural number: '))
    champ_digits, champ_product = main(num)
    print('Digits d_1, d_10, ..., d_{10^n}:')
    print('  {}'.format(champ_digits))
    print('Product of those digits:')
    print('  {}'.format(champ_product))
