
def encrypt_rail_fence(input, key):
    array = [[None for _ in range(len(input))] for _ in range(key)]
    dir = False
    row = 0
    output = ''
    for i in range(len(input)):
        if (row == 0) or (row == key - 1):
            dir = not dir
        array[row][i] = input[i]
        if dir:
            row = row + 1
        else:
            row = row - 1
    for i in range(key):
        for j in range(len(input)):
            if array[i][j] is not None:
                output = output + str(array[i][j])
    return output


def decrypt_rail_fence(input, key):
    array = [[None for _ in range(len(input))] for _ in range(key)]
    dir = False
    row = 0
    output = ''
    for i in range(len(input)):
        if (row == 0) or (row == key - 1):
            dir = not dir
        array[row][i] = '_'
        if dir:
            row = row + 1
        else:
            row = row - 1
    ind = 0
    for i in range(key):
        for j in range(len(input)):
            if array[i][j] == '_':
                array[i][j] = input[ind]
                ind = ind + 1
    for i in range(len(input)):
        if (row == 0) or (row == key - 1):
            dir = not dir
        output = output + str(array[row][i])
        if dir:
            row = row + 1
        else:
            row = row - 1

    return output


if __name__ == "__main__":
    m = 'POLYTECHNIC'
    n = 3
    print('Text to encode : ', m)
    print('Key : ', n)
    print('Encoded Text : ',encrypt_rail_fence(m, n))
    print('Decoded Text : ',decrypt_rail_fence(encrypt_rail_fence(m, n), n))