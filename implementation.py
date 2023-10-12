import struct
import math

from helper_functions import A,B,C,D, FF
    # Define a sample message (in bytes)
# message = b"Hello, MD5!"

def impleFunction(message):

# Calculate the length of the message in bits
    message_length_bits = len(message) * 8

# Append padding to the message
    message += b'\x80'
    while len(message) % 64 != 56:
        message += b'\x00'

# Append the length of the original message in bits
    message += struct.pack('<Q', message_length_bits)

# Split the padded message into 512-bit blocks
    blocks = [message[i:i+64] for i in range(0, len(message), 64)]

    for block in blocks:
    # Convert the block into a list of 32-bit words
        words = [struct.unpack('<I', block[i:i+4])[0] for i in range(0, 64, 4)]

        # Save the current state
        AA, BB, CC, DD = A, B, C, D

        # Perform the MD5 main rounds
        A = FF(A, B, C, D, words[0], 7, 0xD76AA478)
        D = FF(D, A, B, C, words[1], 12, 0xE8C7B756)
        # ... Continue with the other rounds ...

    # Compute the final hash
    final_hash = struct.pack('<I', A) + struct.pack('<I', B) + struct.pack('<I', C) + struct.pack('<I', D)

    # Print the hexadecimal representation of the MD5 hash
    md5_hash = ''.join(format(byte, '02x') for byte in final_hash)
    print("MD5 Hash:", md5_hash)