from bitstring import BitStream, BitArray

# Initial Permutation Table 
initialPermutation = [58, 50, 42, 34, 26, 18, 10, 2,
                      60, 52, 44, 36, 28, 20, 12, 4,
                      62, 54, 46, 38, 30, 22, 14, 6,
                      64, 56, 48, 40, 32, 24, 16, 8,
                      57, 49, 41, 33, 25, 17, 9, 1,
                      59, 51, 43, 35, 27, 19, 11, 3,
                      61, 53, 45, 37, 29, 21, 13, 5,
                      63, 55, 47, 39, 31, 23, 15, 7]

# final Permutation Table 
finalPermutation = [40, 8, 48, 16, 56, 24, 64, 32,
                    39, 7, 47, 15, 55, 23, 63, 31,
                    38, 6, 46, 14, 54, 22, 62, 30,
                    37, 5, 45, 13, 53, 21, 61, 29,
                    36, 4, 44, 12, 52, 20, 60, 28,
                    35, 3, 43, 11, 51, 19, 59, 27,
                    34, 2, 42, 10, 50, 18, 58, 26,
                    33, 1, 41, 9, 49, 17, 57, 25]

# Straight Permutaion Table: input 32 – output 32
permutationTable = [16, 7, 20, 21,
                    29, 12, 28, 17,
                    1, 15, 23, 26,
                    5, 18, 31, 10,
                    2, 8, 24, 14,
                    32, 27, 3, 9,
                    19, 13, 30, 6,
                    22, 11, 4, 25]

# Permuted Choice 1 : input 64 – output 56
PC1 = [57, 49, 41, 33, 25, 17, 9
    , 1, 58, 50, 42, 34, 26, 18
    , 10, 2, 59, 51, 43, 35, 27
    , 19, 11, 3, 60, 52, 44, 36
    , 63, 55, 47, 39, 31, 23, 15
    , 7, 62, 54, 46, 38, 30, 22
    , 14, 6, 61, 53, 45, 37, 29
    , 21, 13, 5, 28, 20, 12, 4]

# Permuted Choice 2 : input 56 – output 48
PC2 = [14, 17, 11, 24, 1, 5,
       3, 28, 15, 6, 21, 10,
       23, 19, 12, 4, 26, 8,
       16, 7, 27, 20, 13, 2,
       41, 52, 31, 37, 47, 55,
       30, 40, 51, 45, 33, 48,
       44, 49, 39, 56, 34, 53,
       46, 42, 50, 36, 29, 32]

expansion_permutation = [32, 1, 2, 3, 4, 5, 4, 5,
                         6, 7, 8, 9, 8, 9, 10, 11,
                         12, 13, 12, 13, 14, 15, 16, 17,
                         16, 17, 18, 19, 20, 21, 20, 21,
                         22, 23, 24, 25, 24, 25, 26, 27,
                         28, 29, 28, 29, 30, 31, 32, 1]

# S-box Table 
SBoxTable = [[[14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7],
              [0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8],
              [4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0],
              [15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13]],

             [[15, 1, 8, 14, 6, 11, 3, 4, 9, 7, 2, 13, 12, 0, 5, 10],
              [3, 13, 4, 7, 15, 2, 8, 14, 12, 0, 1, 10, 6, 9, 11, 5],
              [0, 14, 7, 11, 10, 4, 13, 1, 5, 8, 12, 6, 9, 3, 2, 15],
              [13, 8, 10, 1, 3, 15, 4, 2, 11, 6, 7, 12, 0, 5, 14, 9]],

             [[10, 0, 9, 14, 6, 3, 15, 5, 1, 13, 12, 7, 11, 4, 2, 8],
              [13, 7, 0, 9, 3, 4, 6, 10, 2, 8, 5, 14, 12, 11, 15, 1],
              [13, 6, 4, 9, 8, 15, 3, 0, 11, 1, 2, 12, 5, 10, 14, 7],
              [1, 10, 13, 0, 6, 9, 8, 7, 4, 15, 14, 3, 11, 5, 2, 12]],

             [[7, 13, 14, 3, 0, 6, 9, 10, 1, 2, 8, 5, 11, 12, 4, 15],
              [13, 8, 11, 5, 6, 15, 0, 3, 4, 7, 2, 12, 1, 10, 14, 9],
              [10, 6, 9, 0, 12, 11, 7, 13, 15, 1, 3, 14, 5, 2, 8, 4],
              [3, 15, 0, 6, 10, 1, 13, 8, 9, 4, 5, 11, 12, 7, 2, 14]],

             [[2, 12, 4, 1, 7, 10, 11, 6, 8, 5, 3, 15, 13, 0, 14, 9],
              [14, 11, 2, 12, 4, 7, 13, 1, 5, 0, 15, 10, 3, 9, 8, 6],
              [4, 2, 1, 11, 10, 13, 7, 8, 15, 9, 12, 5, 6, 3, 0, 14],
              [11, 8, 12, 7, 1, 14, 2, 13, 6, 15, 0, 9, 10, 4, 5, 3]],

             [[12, 1, 10, 15, 9, 2, 6, 8, 0, 13, 3, 4, 14, 7, 5, 11],
              [10, 15, 4, 2, 7, 12, 9, 5, 6, 1, 13, 14, 0, 11, 3, 8],
              [9, 14, 15, 5, 2, 8, 12, 3, 7, 0, 4, 10, 1, 13, 11, 6],
              [4, 3, 2, 12, 9, 5, 15, 10, 11, 14, 1, 7, 6, 0, 8, 13]],

             [[4, 11, 2, 14, 15, 0, 8, 13, 3, 12, 9, 7, 5, 10, 6, 1],
              [13, 0, 11, 7, 4, 9, 1, 10, 14, 3, 5, 12, 2, 15, 8, 6],
              [1, 4, 11, 13, 12, 3, 7, 14, 10, 15, 6, 8, 0, 5, 9, 2],
              [6, 11, 13, 8, 1, 4, 10, 7, 9, 5, 0, 15, 14, 2, 3, 12]],

             [[13, 2, 8, 4, 6, 15, 11, 1, 10, 9, 3, 14, 5, 0, 12, 7],
              [1, 15, 13, 8, 10, 3, 7, 4, 12, 5, 6, 11, 0, 14, 9, 2],
              [7, 11, 4, 1, 9, 12, 14, 2, 0, 6, 10, 13, 15, 3, 5, 8],
              [2, 1, 14, 7, 4, 10, 8, 13, 15, 12, 9, 0, 3, 5, 6, 11]]]

# Number of bit shifts
shiftTable = [1, 1, 2, 2,
              2, 2, 2, 2,
              1, 2, 2, 2,
              2, 2, 2, 1]


# conversions
def HexToBinary(stringArr):
    mp = {'0': "0000",
          '1': "0001",
          '2': "0010",
          '3': "0011",
          '4': "0100",
          '5': "0101",
          '6': "0110",
          '7': "0111",
          '8': "1000",
          '9': "1001",
          'A': "1010",
          'B': "1011",
          'C': "1100",
          'D': "1101",
          'E': "1110",
          'F': "1111"}
    bin = ""
    for i in range(len(stringArr)):
        bin = bin + mp[stringArr[i]]
    return bin


# Binary to hexadecimal conversion 
def BinaryToHex(stringArr):
    mp = {"0000": '0',
          "0001": '1',
          "0010": '2',
          "0011": '3',
          "0100": '4',
          "0101": '5',
          "0110": '6',
          "0111": '7',
          "1000": '8',
          "1001": '9',
          "1010": 'A',
          "1011": 'B',
          "1100": 'C',
          "1101": 'D',
          "1110": 'E',
          "1111": 'F'}
    hex = ""
    for i in range(0, len(stringArr), 4):
        ch = ""
        ch = ch + stringArr[i]
        ch = ch + stringArr[i + 1]
        ch = ch + stringArr[i + 2]
        ch = ch + stringArr[i + 3]
        hex = hex + mp[ch]

    return hex


def bin2dec(binary):
    binary1 = binary
    decimal, i, n = 0, 0, 0
    while (binary != 0):
        dec = binary % 10
        decimal = decimal + dec * pow(2, i)
        binary = binary // 10
        i += 1
    return decimal


def dec2bin(num):
    res = bin(num).replace("0b", "")
    if (len(res) % 4 != 0):
        div = len(res) / 4
        div = int(div)
        counter = (4 * (div + 1)) - len(res)
        for i in range(0, counter):
            res = '0' + res
    return res


def split(word):
    return [char for char in word]


def listToString(s):
    str1 = ""
    for ele in s:
        str1 += ele
    return str1


def bitString_to_bits(bitString):
    d = BitArray(bin=bitString)
    return d.bin


#######################################################################
######################## functions for key ############################
#######################################################################
# change the key to 56 bits
def keyGeneration_before_48bit(key):
    key = makeKey56Bits(key)
    C, D = divideKeyInto_C_and_D(key)
    concate_C_D = []
    for i in range(len(C)):
        concate_C_D.append(concate_Ci_and_Di(C[i], D[i]))
    return concate_C_D


def makeKey56Bits(key):
    key = HexToBinary(key)
    key = split(key)
    print("key before: ", len(key))
    key = listToString(key)
    print(key, len(key))
    newKey = []
    for i in range(len(PC1)):
        #######################################################8alban fe -1 hna
        newKey.append(key[PC1[i] - 1])
    print("\nkey after: ", len(newKey))
    newKey = listToString(newKey)
    print(newKey, len(newKey))
    # divideKeyInto_C_and_D(newKey)
    return newKey


# divide the key  into C and D and make C(1-16) & D(1-16)
def divideKeyInto_C_and_D(key):
    length = len(key)
    C = []
    D = []
    for i in range(0, (int(length / 2))):
        C.append(key[i])
    C = listToString(C)
    C_all = C
    print("\nC:", 0)
    print(C, len(C))
    for i in range(int(length / 2), len(key)):
        D.append(key[i])
    D = listToString(D)
    D_all = D
    print("\nD:", 0)
    print(D, len(D))
    C = []
    D = []
    C.append(C_all)
    D.append(D_all)
    print("\n----------------C from 1 to 16----------------")
    for i in range(1, len(shiftTable) + 1):
        C.append(C[i - 1])
        print("C:", i)
        C[i] = shift_left(C[i - 1], shiftTable[i - 1])
        print(C[i])
    print("\n----------------D from 1 to 16----------------")
    for i in range(1, len(shiftTable) + 1):
        D.append(D[i - 1])
        print("D:", i)
        D[i] = shift_left(D[i - 1], shiftTable[i - 1])
        print(D[i])
    return C[1:17], D[1:17]


# takes C[i] and D[i] and concatinate them
def concate_Ci_and_Di(Ci, Di):
    combine_str = Ci + Di
    return combine_str


def create_16_sub_key(key):
    list_of_concates = keyGeneration_before_48bit(key)
    key = list_of_concates
    list_of_keys = []
    for i in range(len(key)):
        list_of_keys.append(returnSubKey(key[i]))
    # print(list_of_keys)
    for i in range(len(list_of_keys)):
        print("K", i + 1, list_of_keys[i], "  len: ", len(list_of_keys[i]))
    return list_of_keys


def returnSubKey(key):
    element = key
    newKey = []
    for i in range(len(PC2)):
        #######################################################8alban fe -1 hna
        newKey.append(element[PC2[i] - 1])
    # divideKeyInto_C_and_D(newKey)
    newKey = listToString(newKey)
    return newKey


def shift_left(k, nth_shifts):
    s = ""
    for i in range(nth_shifts):
        for j in range(1, len(k)):
            s = s + k[j]
        s = s + k[0]
        k = s
        s = ""
    return k


#######################################################################
#################### functions for plain text #########################
#######################################################################
def permute(k, arr, n):
    permutation = ""
    for i in range(0, n):
        permutation = permutation + k[arr[i] - 1]
    return permutation


def xor(a, b):
    ans = ""
    for i in range(len(a)):
        if a[i] == b[i]:
            ans = ans + "0"
        else:
            ans = ans + "1"
    return ans


def expand_R_to_48bits(R):
    right = permute(R, expansion_permutation, 48)
    return right


#######################################################################
####################   DES encrypt function  ##########################
#######################################################################
def DES_encrypt(plainText, key):
    list_of_keys = create_16_sub_key(key)

    print("-------------------------------plain text-------------------------------")
    plainText = HexToBinary(plainText)
    plainText = permute(plainText, initialPermutation, 64)
    print(plainText, len(plainText))
    left = plainText[0:32]
    right = plainText[32:64]
    # R_all=[]
    # l_all=[]
    for i in range(16):
        R_expaneded = expand_R_to_48bits(right)
        xor_R_Key = xor(R_expaneded, list_of_keys[i - 1])
        # R_all.append(xor(R0,list_of_keys[i-1]))

        sbox_str = ""
        for j in range(0, 8):
            row = bin2dec(int(xor_R_Key[j * 6] + xor_R_Key[j * 6 + 5]))
            col = bin2dec(
                int(xor_R_Key[j * 6 + 1] + xor_R_Key[j * 6 + 2] + xor_R_Key[j * 6 + 3] + xor_R_Key[j * 6 + 4]))
            val = SBoxTable[j][row][col]
            sbox_str = sbox_str + dec2bin(val)
        sbox_str = permute(sbox_str, permutationTable, 32)

        # XOR left and sbox_str
        result = xor(left, sbox_str)
        left = result

        # Swapper
        if (i != 15):
            left, right = right, left
        print("Round ", i + 1, " ", BinaryToHex(left), " ", BinaryToHex(right), " ", BinaryToHex(list_of_keys[i]))

        # Combination
    combine = left + right

    # Final permutaion: final rearranging of bits to get cipher text
    cipher_text = permute(combine, finalPermutation, 64)
    cipher_text = BinaryToHex(cipher_text)
    return cipher_text


#######################################################################
####################   DES decrypt function  ##########################
#######################################################################    
def DES_decrypt(plainText, key):
    list_of_keys = create_16_sub_key(key)
    list_of_keys.reverse()

    #print(list_of_keys)
    print("-------------------------------plain text-------------------------------")
    plainText = HexToBinary(plainText)
    plainText = permute(plainText, initialPermutation, 64)
    print(plainText, len(plainText))
    left = plainText[0:32]
    right = plainText[32:64]
    # R_all=[]
    # l_all=[]
    for i in range(16):
        R_expaneded = expand_R_to_48bits(right)
        xor_R_Key = xor(R_expaneded, list_of_keys[i - 1])
        # R_all.append(xor(R0,list_of_keys[i-1]))

        sbox_str = ""
        for j in range(0, 8):
            row = bin2dec(int(xor_R_Key[j * 6] + xor_R_Key[j * 6 + 5]))
            col = bin2dec(
                int(xor_R_Key[j * 6 + 1] + xor_R_Key[j * 6 + 2] + xor_R_Key[j * 6 + 3] + xor_R_Key[j * 6 + 4]))
            val = SBoxTable[j][row][col]
            sbox_str = sbox_str + dec2bin(val)
        sbox_str = permute(sbox_str, permutationTable, 32)

        # XOR left and sbox_str
        result = xor(left, sbox_str)
        left = result

        # Swapper
        if (i != 15):
            left, right = right, left
        print("Round ", i + 1, " ", BinaryToHex(left), " ", BinaryToHex(right), " ", BinaryToHex(list_of_keys[i]))

        # Combination
    combine = left + right

    # Final permutaion: final rearranging of bits to get cipher text
    cipher_text = permute(combine, finalPermutation, 64)
    cipher_text = BinaryToHex(cipher_text)
    return cipher_text


def main():
    key = input("plese enter the key: ")
    key_for_decrypt=key
    plainText = input("plese enter the plain text: ")
    plain=plainText
    no_of_times_encryption = int(input("plese enter the number of times you want to run the encryption:"))
    for i in range(no_of_times_encryption):
        plainText = DES_encrypt(plainText, key)
    cipher_text = plainText
    print("---------------------------------plain text---------------------------------")
    print("cipher text:", plain)
    print("---------------------------------cipher text---------------------------------")
    print("cipher text:", cipher_text)
    #print(reverse(key_for_decrypt))
    #key_for_decrypt = reverse(key_for_decrypt)
    want_to_decrypt=int(input("do you want to decrypt? 1 for yes ,0 for no: "))
    if(want_to_decrypt==1):
        decryption=DES_decrypt(cipher_text,key_for_decrypt)
        print("---------------------------------cipher text---------------------------------")
        print("cipher text:", cipher_text)
        print("---------------------------------plain text---------------------------------")
        print("cipher text:", decryption)
        #print(decryption)
        for i in range(1000000000):
            x=0
if __name__ == '__main__':
    main() 