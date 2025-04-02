seq = 'ATGCAAGTGGTGTGTCTGTTCTGAGAGGGCCTAA'
import re
# Find largest introns in the sequence
intron = re.findall(r'GT[ATCG]+AG', seq)
print(intron)
max_length = 0
for i in intron:
    if len(i) > max_length:
        max_length = len(i)
print('The length of the largest intron is:', max_length)