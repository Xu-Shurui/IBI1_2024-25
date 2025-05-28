import numpy as np

def read_fasta(filename):
    """Reads a sequence from a FASTA file and returns the name and sequence."""
    with open(filename, 'r') as file:
        lines = file.readlines()
        name = lines[0].strip().replace(">", "")
        sequence = "".join(line.strip() for line in lines[1:])
        return name, sequence

def load_blosum62(filename):
    """Loads BLOSUM62 substitution matrix into a dictionary of dictionaries."""
    with open(filename, 'r') as file:
        lines = [line.strip().split() for line in file if not line.startswith("#") and line.strip()]
        headers = lines[0]
        matrix = {}

        for line in lines[1:]:
            row_aa = line[0]
            scores = list(map(int, line[1:]))
            matrix[row_aa] = dict(zip(headers, scores))
    return matrix

def align(seq1, seq2, blosum):
    """Performs non-gapped global alignment and returns total score and identity percentage."""
    assert len(seq1) == len(seq2), "Sequences must be of equal length"
    
    score = 0
    identity = 0

    for a1, a2 in zip(seq1, seq2):
        score += blosum.get(a1, {}).get(a2, -4)  # Use -4 as default if amino acid not found
        if a1 == a2:
            identity += 1

    percent_identity = identity / len(seq1)
    return score, percent_identity

name1, seq1 = read_fasta("P04179_human.fasta")
name2, seq2 = read_fasta("P09671_mouse.fasta")
name3, seq3 = read_fasta("random.fasta")

blosum = load_blosum62("blosum62.txt")

print(f"Comparing {name1} to {name2}")
score12, identity12 = align(seq1, seq2, blosum)
print(f"Score: {score12}, Identity: {identity12:.2f}")

print(f"Comparing {name1} to {name3}")
score13, identity13 = align(seq1, seq3, blosum)
print(f"Score: {score13}, Identity: {identity13:.2f}")

print(f"Comparing {name2} to {name3}")
score23, identity23 = align(seq2, seq3, blosum)
print(f"Score: {score23}, Identity: {identity23:.2f}")