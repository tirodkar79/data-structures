from Stack import Stack

s = Stack()


def dec_div(dec_val):
    while dec_val > 0:
        rem = dec_val % 2
        s.push(rem)
        dec_val //= 2

    binary = ""
    while not s.isEmpty():
        a = s.pop()
        binary += str(a)

    return binary


print(dec_div(242))
