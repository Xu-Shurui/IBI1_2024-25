def find_restriction_enzyme_cut_sites(dna_sequence, enzyme_sequence):
    valid_bases = {'A', 'T', 'C', 'G'}
    # Check if the DNA sequence and enzyme sequence are valid
    if not all(base in valid_bases for base in dna_sequence):
        raise ValueError("Invalid DNA sequence. Only A, T, C, G are allowed.")
    if not all(base in valid_bases for base in enzyme_sequence):
        raise ValueError("Invalid enzyme sequence. Only A, T, C, G are allowed.")
    # Find all occurrences of the enzyme sequence in the DNA sequence
    cut_sites = []
    start = 0
    while True:
        start = dna_sequence.find(enzyme_sequence, start)
        if start == -1:
            break
        cut_sites.append(start + 1)  # +1 to convert to 1-based index
        start += 1  # Move to the next position for the next search
    return cut_sites
dna = "AGCTACTGGTACGATCGATCGATCGATCGATCGATCGATCGATCGATCGATCGATCGATCG"
enzyme = "GATC"

cut_sites = find_restriction_enzyme_cut_sites(dna, enzyme)
if cut_sites:
    print(f"Restriction enzyme cut sites found at positions: {cut_sites}")
else:
    print("No restriction enzyme cut sites found.")