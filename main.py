import struct



# Helper functions for MD5 operations
def F(X, Y, Z):
    return (X & Y) | (~X & Z)


def G(X, Y, Z):
    return (X & Z) | (Y & ~Z)


def H(X, Y, Z):
    return X ^ Y ^ Z


def I(X, Y, Z):
    return Y ^ (X | ~Z)


# Functions for MD5 main rounds
def FF(a, b, c, d, x, s, ac):
    a = (a + F(b, c, d) + x + ac) & 0xFFFFFFFF
    a = ((a << s) | (a >> (32 - s))) & 0xFFFFFFFF
    a = (a + b) & 0xFFFFFFFF
    return a


def GG(a, b, c, d, x, s, ac):
    a = (a + G(b, c, d) + x + ac) & 0xFFFFFFFF
    a = ((a << s) | (a >> (32 - s))) & 0xFFFFFFFF
    a = (a + b) & 0xFFFFFFFF
    return a


def HH(a, b, c, d, x, s, ac):
    a = (a + H(b, c, d) + x + ac) & 0xFFFFFFFF
    a = ((a << s) | (a >> (32 - s))) & 0xFFFFFFFF
    a = (a + b) & 0xFFFFFFFF
    return a


def II(a, b, c, d, x, s, ac):
    a = (a + I(b, c, d) + x + ac) & 0xFFFFFFFF
    a = ((a << s) | (a >> (32 - s))) & 0xFFFFFFFF
    a = (a + b) & 0xFFFFFFFF
    return a



# Function to calculate MD5 hash
def calculate_md5(input_string):
    # Initialize the MD5 state
    A = 0x67452301
    B = 0xEFCDAB89
    C = 0x98BADCFE
    D = 0x10325476

    # Convert the input string to bytes
    input_bytes = input_string.encode('utf-8')

    # Calculate the length of the message in bits
    message_length_bits = len(input_bytes) * 8

    # Append padding to the message
    
    input_bytes += b'\x80'
    while len(input_bytes) % 64 != 56:
        input_bytes += b'\x00'


    # Append the length of the original message in bits
    input_bytes += struct.pack('<Q', message_length_bits)

    # Split the padded message into 512-bit blocks
    blocks = [input_bytes[i:i + 64] for i in range(0, len(input_bytes), 64)]
    # blocks = [input_bytes[i:i + 64] for i in range(0, len(input_bytes), 64)]
    for block in blocks:

        # Convert the block into a list of 32-bit words
        words = [struct.unpack('<I', block[i:i + 4])[0] for i in range(0, 64, 4)]

        # Save the current state
        AA, BB, CC, DD = A, B, C, D

        # Perform the MD5 main rounds
        # Round 1
        A = FF(A, B, C, D, words[0], 7, 0xD76AA478)
        D = FF(D, A, B, C, words[1], 12, 0xE8C7B756)
        C = FF(C, D, A, B, words[2], 17, 0x242070DB)
        B = FF(B, C, D, A, words[3], 22, 0xC1BDCEEE)
        A = FF(A, B, C, D, words[4], 7, 0xF57C0FAF)
        D = FF(D, A, B, C, words[5], 12, 0x4787C62A)
        C = FF(C, D, A, B, words[6], 17, 0xA8304613)
        B = FF(B, C, D, A, words[7], 22, 0xFD469501)
        A = FF(A, B, C, D, words[8], 7, 0x698098D8)
        D = FF(D, A, B, C, words[9], 12, 0x8B44F7AF)
        C = FF(C, D, A, B, words[10], 17, 0xFFFF5BB1)
        B = FF(B, C, D, A, words[11], 22, 0x895CD7BE)
        A = FF(A, B, C, D, words[12], 7, 0x6B901122)
        D = FF(D, A, B, C, words[13], 12, 0xFD987193)
        C = FF(C, D, A, B, words[14], 17, 0xA679438E)
        B = FF(B, C, D, A, words[15], 22, 0x49B40821)

        # Round 2
        A = GG(A, B, C, D, words[1], 5, 0xF61E2562)
        D = GG(D, A, B, C, words[6], 9, 0xC040B340)
        C = GG(C, D, A, B, words[11], 14, 0x265E5A51)
        B = GG(B, C, D, A, words[0], 20, 0xE9B6C7AA)
        A = GG(A, B, C, D, words[5], 5, 0xD62F105D)
        D = GG(D, A, B, C, words[10], 9, 0x02441453)
        C = GG(C, D, A, B, words[15], 14, 0xD8A1E681)
        B = GG(B, C, D, A, words[4], 20, 0xE7D3FBC8)
        A = GG(A, B, C, D, words[9], 5, 0x21E1CDE6)
        D = GG(D, A, B, C, words[14], 9, 0xC33707D6)
        C = GG(C, D, A, B, words[3], 14, 0xF4D50D87)
        B = GG(B, C, D, A, words[8], 20, 0x455A14ED)
        A = GG(A, B, C, D, words[13], 5, 0xA9E3E905)
        D = GG(D, A, B, C, words[2], 9, 0xFCEFA3F8)
        C = GG(C, D, A, B, words[7], 14, 0x676F02D9)
        B = GG(B, C, D, A, words[12], 20, 0x8D2A4C8A)


        # Round 3
        A = HH(A, B, C, D, words[5], 4, 0xFFFA3942)
        D = HH(D, A, B, C, words[8], 11, 0x8771F681)
        C = HH(C, D, A, B, words[11], 16, 0x6D9D6122)
        B = HH(B, C, D, A, words[14], 23, 0xFDE5380C)
        A = HH(A, B, C, D, words[1], 4, 0xA4BEEA44)
        D = HH(D, A, B, C, words[4], 11, 0x4BDECFA9)
        C = HH(C, D, A, B, words[7], 16, 0xF6BB4B60)
        B = HH(B, C, D, A, words[10], 23, 0xBEBFBC70)
        A = HH(A, B, C, D, words[13], 4, 0x289B7EC6)
        D = HH(D, A, B, C, words[0], 11, 0xEAA127FA)
        C = HH(C, D, A, B, words[3], 16, 0xD4EF3085)
        B = HH(B, C, D, A, words[6], 23, 0x04881D05)
        A = HH(A, B, C, D, words[9], 4, 0xD9D4D039)
        D = HH(D, A, B, C, words[12], 11, 0xE6DB99E5)
        C = HH(C, D, A, B, words[15], 16, 0x1FA27CF8)
        B = HH(B, C, D, A, words[2], 23, 0xC4AC5665)


        # Round 4
        A = II(A, B, C, D, words[0], 6, 0xF4292244)
        D = II(D, A, B, C, words[7], 10, 0x432AFF97)
        C = II(C, D, A, B, words[14], 15, 0xAB9423A7)
        B = II(B, C, D, A, words[5], 21, 0xFC93A039)
        A = II(A, B, C, D, words[12], 6, 0x655B59C3)
        D = II(D, A, B, C, words[3], 10, 0x8F0CCC92)
        C = II(C, D, A, B, words[10], 15, 0xFFEFF47D)
        B = II(B, C, D, A, words[1], 21, 0x85845DD1)
        A = II(A, B, C, D, words[8], 6, 0x6FA87E4F)
        D = II(D, A, B, C, words[15], 10, 0xFE2CE6E0)
        C = II(C, D, A, B, words[6], 15, 0xA3014314)
        B = II(B, C, D, A, words[13], 21, 0x4E0811A1)
        A = II(A, B, C, D, words[4], 6, 0xF7537E82)
        D = II(D, A, B, C, words[11], 10, 0xBD3AF235)
        C = II(C, D, A, B, words[2], 15, 0x2AD7D2BB)
        B = II(B, C, D, A, words[9], 21, 0xEB86D391)

    

        # Update the state with the results of this block
        A = (A + AA) & 0xFFFFFFFF
        B = (B + BB) & 0xFFFFFFFF
        C = (C + CC) & 0xFFFFFFFF
        D = (D + DD) & 0xFFFFFFFF

    # Compute the final hash
    # final_hash = struct.pack('<Q', A) + struct.pack('<Q', B) + struct.pack('<Q', C) + struct.pack('<Q', D)
    final_hash = struct.pack('<I', A) + struct.pack('<I', B) + struct.pack('<I', C) + struct.pack('<I', D)

    # Convert the final hash to a hexadecimal representation
    md5_hash = ''.join(format(byte, '02x') for byte in final_hash)
    # md5_hash = ''.join(format(byte, '02x') for byte in final_hash)
    return md5_hash
