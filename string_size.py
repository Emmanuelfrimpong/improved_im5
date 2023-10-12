
def calculate_hex_string_size(hex_string):
    # Check if the input is a valid hexadecimal string (even length)
    if len(hex_string) % 2 != 0:
        raise ValueError("Input string must have an even number of characters")

    # Calculate the size in bytes
    size_bytes = len(hex_string) // 2

    # Calculate the size in bits
    size_bits = size_bytes * 8

    return size_bytes, size_bits


