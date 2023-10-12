import base64
from email import base64mime
from cipher_layer import encrypt
from main import calculate_md5
from string_size import calculate_hex_string_size
import sys


def calculate_md5_extended(input_string):
    # Split the input string into four parts
    str_length = len(input_string)
    # Calculate the approximate length of each part
    part_length = str_length // 4

    # Calculate the actual lengths of the parts
    part_lengths = [part_length] * 4

    # Adjust the lengths if necessary to ensure they sum up to the total length
    remaining_length = str_length - (part_length * 4)
    for i in range(remaining_length):
        part_lengths[i] += 1

    # Split the string into 4 parts
    parts = []
    start = 0
    for length in part_lengths:
        end = start + length
        parts.append(input_string[start:end])
        start = end
    # loop through the parts and and encrypt each part
    parts = [encrypt(part,2) for part in parts]
    # Calculate the MD5 hash for each part
    md5_hashes = [calculate_md5(part) for part in parts]
    print("Size here= ",calculate_hex_string_size("".join(md5_hashes)))
    md5_hashes = [encrypt(str(part),2) for part in md5_hashes]
    md5_hashes = [calculate_md5(str(part)) for part in md5_hashes]
    # Combine the hashes to make a final size of 512 bits
    md5_extended = "" + md5_hashes[0] + md5_hashes[1] + md5_hashes[2] + md5_hashes[3]
    # print the size of the final hash


    return md5_extended


output = calculate_md5_extended("hello, world!")
# print size of the output
print(calculate_hex_string_size(output))
print(output)