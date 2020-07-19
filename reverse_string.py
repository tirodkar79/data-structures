from Stack import Stack


def reverse(string_val):

    s = Stack()
    index = 0
    while index < len(string_val):
        val = string_val[index]
        s.push(val)
        index += 1

    reverse_s = ""
    while not s.isEmpty():
        top = s.pop()
        reverse_s += top

    return reverse_s


print(reverse("Hello"))
