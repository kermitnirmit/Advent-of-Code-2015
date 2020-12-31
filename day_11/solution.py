from collections import defaultdict
p_input = "cqjxjnds"

A_LOWER = ord('a')
ALPHABET_SIZE = 26

def _decompose(number):
    """Generate digits from `number` in base alphabet, least significants
    bits first.

    Since A is 1 rather than 0 in base alphabet, we are dealing with
    `number - 1` at each iteration to be able to extract the proper digits.
    """

    while number:
        number, remainder = divmod(number - 1, ALPHABET_SIZE)
        yield remainder


def base_10_to_alphabet(number):
    """Convert a decimal number to its base alphabet representation"""

    return ''.join(
            chr(A_LOWER + part)
            for part in _decompose(number)
    )[::-1]


def base_alphabet_to_10(letters):
    """Convert an alphabet number to its decimal representation"""

    return sum((ord(letter) - A_LOWER + 1) * ALPHABET_SIZE**i for i, letter in enumerate(reversed(letters)))

# Passwords must include one increasing straight of at least three letters, like abc, bcd, cde, and so on, up to xyz. They cannot skip letters; abd doesn't count.
# Passwords may not contain the letters i, o, or l, as these letters can be mistaken for other characters and are therefore confusing.
# Passwords must contain at least two different, non-overlapping pairs of letters, like aa, bb, or zz.


def evalPass(p):
    # test 3 increasing
    if any(i in p for i in "iol"):
        return False
    # print("passed iol")
    if not any(ord(a) == ord(b) - 1 == ord(c) - 2 for a, b, c in zip(p, p[1:], p[2:])):
        return False
    # print("passed abc check")
    double_indexes = []
    for i, (a,b) in enumerate(zip(p, p[1:])):
        if a == b:
            double_indexes.append(i)
    if len(double_indexes) == 0 or double_indexes[-1] - double_indexes[0] < 2:
        return False
    # print("passed aa bb ")
    return True


def get_answer(a):
    tempa = base_10_to_alphabet(base_alphabet_to_10(a) + 1)
    prog = 0
    while not evalPass(tempa):
    # print("progress")
        prog += 1
        tempa = base_10_to_alphabet(base_alphabet_to_10(tempa) + 1)
        # input(f"next: {tempa}")
        if prog % 100000 == 0:
            print(f"iteration count : {prog} testing: {tempa}")
    return tempa


nexta = get_answer(p_input)

print(f"part 1 answer: {nexta}")
print(f"part 2 answer: {get_answer(nexta)}")