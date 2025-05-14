import pandas as pd
import re

def nucleotide_amino(mRNA_sequence):
   
    codon_amino = {
        'UUU': 'F', 'UUC': 'F', 'UUA': 'L', 'UUG': 'L',
        'CUU': 'L', 'CUC': 'L', 'CUA': 'L', 'CUG': 'L',
        'AUU': 'I', 'AUC': 'I', 'AUA': 'I', 'AUG': 'M',
        'GUU': 'V', 'GUC': 'V', 'GUA': 'V', 'GUG': 'V',
        'UCU': 'S', 'UCC': 'S', 'UCA': 'S', 'UCG': 'S',
        'AGU': 'S', 'AGC': 'S', 'CCU': 'P', 'CCC': 'P',
        'CCA': 'P', 'CCG': 'P', 'ACU': 'T', 'ACC': 'T',
        'ACA': 'T', 'ACG': 'T', 'GCU': 'A', 'GCC': 'A',
        'GCA': 'A', 'GCG': 'A', 'UAU': 'Y', 'UAC': 'Y',
        'CAU': 'H', 'CAC': 'H', 'CAA': 'Q', 'CAG': 'Q',
        'AAU': 'N', 'AAC': 'N', 'AAA': 'K', 'AAG': 'K',
        'GAU': 'D', 'GAC': 'D', 'GAA': 'E', 'GAG': 'E',
        'UGU': 'C', 'UGC': 'C', 'UGG': 'W', 'CGU': 'R',
        'CGC': 'R', 'CGA': 'R', 'CGG': 'R', 'AGA': 'R',
        'AGG': 'R', 'GGU': 'G', 'GGC': 'G', 'GGA': 'G',
        'GGG': 'G', 'UAA': '*', 'UAG': '*', 'UGA': '*'
    }
    

    codon_df = pd.DataFrame.from_dict(codon_amino, orient='index', columns=['Amino Acid'])

    
    if re.search(r"[^AUGC]+", mRNA_sequence):
        return "mRNA sequence contains invalid characters!"

    
    start_codons = ["AUG", "GUG", "UUG"]
    start_index = 0
    for i in range(0, len(mRNA_sequence) - 2, 3):
        if mRNA_sequence[i:i+3] in start_codons:
            start_index = i
            break

    amino_sequence = []
    for p in range(start_index, len(mRNA_sequence) - 2, 3):
        codon = mRNA_sequence[p:p+3]
        amino_acid = codon_df.loc[codon, 'Amino Acid']
        amino_sequence.append(amino_acid)
        if amino_acid == '*':  
            break

    return ''.join(amino_sequence)  
