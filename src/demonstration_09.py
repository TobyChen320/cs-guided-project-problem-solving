"""
Challenge #9:

Given a string, write a function that returns the "middle" character of the
word.

If the word has an odd length, return the single middle character. If the word
has an even length, return the middle two characters.

Examples:
- get_middle("test") -> "es"
- get_middle("testing") -> "t"
- get_middle("middle") -> "dd"
- get_middle("A") -> "A"
"""
def get_middle(input_str):
    str_len = len(input_str)
    middle_index = str_len // 2
    if str_len %2 == 0:
        return input_str[middle_index -1: middle_index + 1]
    else:
        return input_str[middle_index : middle_index  + 1]

print(get_middle("test"))