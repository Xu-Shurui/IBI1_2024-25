import re
import pandas as pd
def extract_tata_genes(input_file, output_file):
    with open(input_file, 'r') as infile:
        # Read the file line by line
        lines = infile.readlines()
    df = pd.DataFrame(columns=['Gene'])
    gene_name = None
    sequence = []
    for line in lines:
        if line.startswith('>'):
            if gene_name is not None and sequence:
                # Write the previous gene's data to the DataFrame
                seq = ''.join(sequence)
                if re.search(r'TATA[AT]A[AT]', seq):
                    df = df._append({'Gene': gene_name, 'Sequence': seq}, ignore_index=True)
            gene_name = line.strip().split()[0][1:]
            sequence = []
        else:
            sequence.append(line.strip())
    if gene_name is not None and sequence:
        seq = ''.join(sequence)
        if re.search(r'TATA[AT]A[AT]', seq):
            df = df.append({'Gene': gene_name}, ignore_index=True)
    with open(output_file, 'w') as outfile:
        for _, row in df.iterrows():
            outfile.write(f">{row['Gene']}\n")
    print(f"Extracted genes with TATA box and saved to {output_file}")
extract_tata_genes('Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa', 'tata_genes.fa')