#!/usr/bin/python3

def magic_calculation(a, b):
    """Bytecode matching"""
    from magic_calculation_102 import add, sub

    if a < b:
        c = add(a, b)
        for x in range(4, 6):
            c = add(c, x)
        return (c)

    else:
        return(sub(a, b))
