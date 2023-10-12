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
def round_FF(a, b, c, d, x, s, ac):
    a = (a + F(b, c, d) + x + ac) & 0xFFFFFFFF
    a = ((a << s) | (a >> (32 - s))) & 0xFFFFFFFF
    a = (a + b) & 0xFFFFFFFF
    return a

def round_GG(a, b, c, d, x, s, ac):
    a = (a + G(b, c, d) + x + ac) & 0xFFFFFFFF
    a = ((a << s) | (a >> (32 - s))) & 0xFFFFFFFF
    a = (a + b) & 0xFFFFFFFF
    return a

def round_HH(a, b, c, d, x, s, ac):
    a = (a + H(b, c, d) + x + ac) & 0xFFFFFFFF
    a = ((a << s) | (a >> (32 - s))) & 0xFFFFFFFF
    a = (a + b) & 0xFFFFFFFF
    return a

def round_II(a, b, c, d, x, s, ac):
    a = (a + I(b, c, d) + x + ac) & 0xFFFFFFFF
    a = ((a << s) | (a >> (32 - s))) & 0xFFFFFFFF
    a = (a + b) & 0xFFFFFFFF
    return a

# Modify the padding to ensure 512-bit alignment
def add_padding(input_bytes):
    original_length_bits = len(input_bytes) * 8
    input_bytes += b'\x80'
    while (len(input_bytes) + 16 * 8) % 1024 != 0:  # Ensure 512-bit alignment
        input_bytes += b'\x00'
    input_bytes += struct.pack('<8Q', original_length_bits)
    return input_bytes

# Function to calculate MD5 hash with 512-bit output
# Function to calculate MD5 hash with 512-bit output
def calculate_md5_512(input_string):
    # Initialize the MD5 state for a 512-bit output
    A = 0x0123456789ABCDEF
    B = 0xFEDCBA9876543210
    C = 0xA1B2C3D4E5F60718
    D = 0x0123456789ABCDEF

    # Convert the input string to bytes and add padding
    input_bytes = input_string.encode('utf-8')
    input_bytes = add_padding(input_bytes)

    # Split the padded message into 512-bit blocks
    blocks = [input_bytes[i:i + 128] for i in range(0, len(input_bytes), 128)]

    for block in blocks:
        # Convert the block into a list of 64-bit words
        words = [struct.unpack('<Q', block[i:i + 8])[0] for i in range(0, 128, 8)]

        # Save the current state
        AA, BB, CC, DD = A, B, C, D

        # Perform the MD5 main rounds for 512-bit output
        for i in range(0, len(words), 16):
            for j in range(16):
                if j < 4:
                    A = round_FF(A, B, C, D, words[i + j], 7, 0xD76AA478)
                elif j < 8:
                    A = round_GG(A, B, C, D, words[i + j], 12, 0xE8C7B756)
                elif j < 12:
                    A = round_HH(A, B, C, D, words[i + j], 17, 0x242070DB)
                else:
                    A = round_II(A, B, C, D, words[i + j], 22, 0xC1BDCEEE)

            A = (A + AA) & 0xFFFFFFFFFFFFFFFF
            B = (B + BB) & 0xFFFFFFFFFFFFFFFF
            C = (C + CC) & 0xFFFFFFFFFFFFFFFF
            D = (D + DD) & 0xFFFFFFFFFFFFFFFF

    # Concatenate the final hash values as 512 bits (64 bytes)
    final_hash = struct.pack('<Q', A) + struct.pack('<Q', B) + struct.pack('<Q', C) + struct.pack('<Q', D)

    # Convert the final hash to a hexadecimal representation
    md5_hash = ''.join(format(byte, '02x') for byte in final_hash)

    return md5_hash

# Example usage
input_string = "Hello, MD5!"
md5_result = calculate_md5_512(input_string)
print("Input String:", input_string)
print("MD5 Hash:", md5_result)
