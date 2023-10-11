#!/usr/bin/python3
def roman_to_int(roman_string):
    """Converts a Roman numeral to an integer"""
    if type(roman_string) != str or not roman_string:
        return 0

    roman_value = {"I": 1, "V": 5, "X": 10,
