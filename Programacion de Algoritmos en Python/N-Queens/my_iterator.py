def next_number(digits, base):
    next_digits = digits.copy()

    for n in range(len(next_digits) - 1, -1, -1):

        if (next_digits[n] + 1) == base:
            next_digits[n] = 0
        else:
            next_digits[n] += 1
            break

    return next_digits


# ----------------------------------------------------------

class My_Iterator:

    def __init__(self, num_digits, base):
        self.digits_list = [0] * num_digits
        self.num_digits = num_digits
        self.base = base

    def next(self):
        next = self.digits_list
        yield next

        for i in range(1, self.base ** self.num_digits):
            next = next_number(next, self.base)
            yield next

        return