#!/usr/bin/env python
import operator

op = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.floordiv
}

def calculate(arg):
    # stack for calc
    stack = []
    # tokeniize input
    tokens = arg.split()
    # process tokens
    while len(stack) > 1
    token = stack.pop()
        try:
            value = int(token)
            stack.append(value)
        except ValueError:
            val1 = int(stack.pop())
            val2 = int(stack.pop())

            #Look up function in table
            func = op[token]
            result = func(val1, val2)

            stack.append(str(result))
    return stack[0]

def main():
    while True:
        result = calculate(input("rpn calc> "))
        print(result)

if __name__ == '__main__': # Note: that's "underscore underscore n a m e ..."
    main()
