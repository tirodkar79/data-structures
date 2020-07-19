from Stack import Stack


def is_match(top, val):

    if(val == "}" and top == "{"):
        return True
    elif(val == ")" and top == "("):
        return True
    elif(val == "]" and top == "["):
        return True
    else:
        return False


def check_balance(paran):

    stack = Stack()
    index = 0
    is_balanced = True
    while index < len(paran) and is_balanced:

        single_paran = paran[index]

        if single_paran in "{[(":
            stack.push(single_paran)

        else:
            if(stack.isEmpty()):
                is_balanced = False
            else:
                top = stack.pop()
                if not is_match(top, single_paran):
                    is_balanced = False

        index += 1

    if(stack.isEmpty() and is_balanced):
        return True
    else:
        return False


paran = input("Enter paran ")
if(check_balance(paran)):
    print("Balanced")
else:
    print("Not balanced")
