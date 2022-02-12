from typing import List

def permutation_cipher(full_str: str, route_list: List[List[int]], route_input: List[int]) -> str:
    result = ''
    i = 0
    j = 0
    while i != len(full_str):
        sp = list(full_str[i: i + 8])
        string_convert = []

        for j in marchroute_input:
            for crypto_key in route_list[j]:
                string_convert.append(sp[crypto_key])
            result += ''.join(string_convert)
        i += 8

    return result

#encryption routes that bypass a string
m1 = [4, 2, 5, 0, 1, 3, 6, 7]
m2 = [7, 1, 3, 6, 4, 2, 5, 0]
m3 = [3, 6, 1, 2, 4, 7, 0, 5]
m4 = [5, 0, 6, 3, 2, 1, 7, 4]
route_list = [m1, m2, m3, m4]

string_input = input("Enter the string to encrypt:")
route_input = list(map(int, input("Enter the encryption route numbers separated by commas:").split(',')))

len_string_input = len(string_input)

# if the length of the string is not a multiple of eight, then fill it with asterisks up to a length that is a multiple of eight
if len_string_input % 8 != 0:
    full_str = string_input.ljust(len_string_input + 8 - len_string_input % 8, '*')
else:
    full_str = string_input

print("Encrypted string:", permutation_cipher(full_str, route_list, route_input))
