#!/usr/bin/env python

def calculate(arg):

    # stack for calc
    stack = []
    # tokeniize input
    tokens = arg.split()
    # process tokens

    for token in tokens:
        try:
            value = int(token)
            stack.append(value)
        except ValueError:
            val1 = stack.pop()
            val2 = stack.pop()
            if token == '+':
                result = val1 + val2
            elif token == '-':
                result  =val1 - val2
            elif token == '*':
                result  =val1 * val2
            elif token == '/':
                result  =val1 / val2                

            stack.append(result)
            return stack[0]

def main():
    while True:
        result = calculate(input("rpn calc> "))
        print(result)

if __name__ == '__main__': # Note: that's "underscore underscore n a m e ..."
    main()
