# md5 import
from datetime import datetime
import hashlib
from bard_implementation import calculate_md5_extended
from main import calculate_md5
import matplotlib.pyplot as plt
import timeit

from string_size import calculate_hex_string_size

input_strings = [
    "Hello, world! How are all doing. This is just a sample testing Hello,"*100,
    "Good morning!, Have a nice day.Good morning!, Have a nice day.Good morning!, Have a nice day."*100,
    "Have a nice day. But I am not sure about it.Have a nice day. But I am not sure about it."*100,
    "Thank you. Have a nice day.Have a nice day. But I am not sure about it."*100,
    "Have a nice day. But I am not sure about it.Have a nice day. But I am not sure about it."*100,
]

# get sizes of input strings
input_sizes = [len(s) for s in input_strings]


# Function to calculate MD5 hash
def calculate_md5(input_string):
    return hashlib.md5(input_string.encode()).hexdigest()


def calculate_ours(input_String):
    return calculate_md5_extended(input_String)



list_md5_time = []
list_ours_time = []
for string in input_strings:
    def test_md5_speed():
        md5_hash = calculate_md5(string)
    def test_our_speed():
        md5_hash = calculate_ours(string)

    md5_execution_time = timeit.timeit(test_md5_speed, number=1000)/1000
    md5_to_string=f"{md5_execution_time:.6f}"
    ours_execution_time = timeit.timeit(test_md5_speed, number=1000)/1000
    ours_to_string=f"{ours_execution_time:.6f}"
   
    list_md5_time.append(md5_to_string)
    list_ours_time.append(ours_to_string)

# Run the test and measure the time
# Adjust the number of iterations as needed

# Calculate the average time per MD5 hash
# average_time_per_hash = execution_time / 1000  # Dividing by the number of iterations

# list_md5_hashes = []
# list_time = []
# for string in input_strings:
#     start_time = datetime.now()
#     md5_hash = calculate_md5(string)
#     end_time = datetime.now()
#     md5_time = end_time - start_time
#     list_time.append(md5_time.total_seconds() * 1000000)
#     list_md5_hashes.append(md5_hash)
#
# # implement our md5
# list_our_hashes = []
# list_our_time = []
# for string in input_strings:
#     start_time = datetime.now()
#     hashed_password = calculate_md5_extended(string)
#     end_time = datetime.now()
#     our_time = end_time - start_time
#     # time in milliseconds
#
#     list_our_time.append(our_time.total_seconds() * 1000000)
#     list_our_hashes.append(hashed_password)
# # print each input size and time taken from md5 and our implementation
print("\t-------------------------------------------------")
print("\n\tSize\t\tMD5 Time\t\tIMD5 Time")
print("\t-------------------------------------------------")
for i in range(len(input_sizes)):
    print(f"\t{input_sizes[i]}\t\t{list_md5_time[i]}\t\t{list_ours_time[i]}")
print("\t-------------------------------------------------")
# let plot both implementation on a graph
# plt.hist(list_md5_time, bins=10, label="MD5")
# plt.hist(list_ours_time, bins=10, label="IMD5")
# plt.xlabel('Time in seconds')
# plt.ylabel('Size of input string')
# plt.title('MD5 vs IMD5')
# plt.legend()
# plot a line graph for input size vs time taken for both md5 and our implementation on the same graph
# plt.plot(input_sizes, list_md5_time, label="MD5")
# plt.plot(input_sizes, list_ours_time, label="IMD5")
# plt.xlabel('Size of input string')
# plt.ylabel('Time in seconds')
# plt.title('MD5 vs IMD5')
# plot a point graph for input size vs time taken for both md5 and our implementation on the same graph
plt.scatter(input_sizes, list_md5_time, label="MD5")
plt.scatter(input_sizes, list_ours_time, label="IMD5")
plt.xlabel('Size of input string')
plt.ylabel('Time in seconds')
plt.title('MD5 vs IMD5')

plt.legend()
plt.show()

# print list of md5 hashes
