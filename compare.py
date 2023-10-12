# md5 import 
import time
import hashlib

from bard_implementation import calculate_md5_extended

# Test passwords
sample_strings = [
    "Hello, world!",
    "Good morning!",
    "Have a nice day.",
    "Thank you.",
    "I love you.",
    "Let's go!",
    "It's a sunny day.",
    "Time flies.",
    "Life is beautiful.",
    "Stay positive.",  
]
print(f"Number of passwords: {len(sample_strings)}")
# Benchmark bcrypt
# list od5 hashes
list_md5_hashes = []
start_time = time.time()
for password in sample_strings:
    md5_hash = hashlib.md5(password.encode()).hexdigest()
    list_md5_hashes.append(md5_hash)
end_time = time.time()
md5_time = end_time - start_time

# Benchmark Argon2

# list of our hashes
list_our_hashes = []
start_time = time.time()
for password in sample_strings:
    hashed_password = calculate_md5_extended(password)
    list_our_hashes.append(hashed_password)
end_time = time.time()
our_time = end_time - start_time

print(f"Md 5 Time: {md5_time} seconds")
# print list of md5 hashes
for i in range(len(list_md5_hashes)): 
    print(list_md5_hashes[i])
    print("\n")
print(f"Our time: {our_time} seconds")
# print list of our hashes
for i in range(len(list_our_hashes)): 
    print(list_our_hashes[i])
    # break
    print("\n")
