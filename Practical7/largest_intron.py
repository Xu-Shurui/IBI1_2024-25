seq = 'ATGCAAGTGGTGTGTCTGTTCTGAGAGGGCCTAA'

def find_largest_intron(sequence):
    max_length = 0
    n = len(sequence)
    # Iterate through the sequence to find 'GT' and 'AG' pairs
    # that indicate the start and end of an intron
    for i in range(n - 1):
        if sequence[i] == 'G' and sequence[i+1] == 'T':
            for j in range(i + 2, n - 1):
                if sequence[j] == 'A' and sequence[j+1] == 'G':
                    intron_length = j + 2 - i  
                    if intron_length > max_length:
                        max_length = intron_length
    return max_length

result = find_largest_intron(seq)
print(f"The length of the largest possible intron is: {result}")