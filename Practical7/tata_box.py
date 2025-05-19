import re
import os

def extract_tata_genes(input_file_path, output_file_name):
    # Check if the input file exists
    if not os.path.exists(input_file_path):
        raise FileNotFoundError(f"Input file '{input_file_path}' not found. Please check the path.")

    # Get the directory of the input file
    input_dir = os.path.dirname(input_file_path)
    
    # Generate the output file path in the same directory
    output_file_path = os.path.join(input_dir, output_file_name)

    with open(input_file_path, 'r') as infile, open(output_file_path, 'w') as outfile:
        gene_name = None
        sequence = []
        
        for line in infile:
            if line.startswith('>'):
                # Process the previous gene
                if gene_name is not None and sequence:
                    full_sequence = ''.join(sequence)
                    if re.search(r'TATA[AT][AT]', full_sequence):
                        outfile.write(f">{gene_name}\n{full_sequence}\n")
                # Extract new gene name
                gene_name = line.strip().split()[0][1:]  # e.g., ">YAL001C" → "YAL001C"
                sequence = []
            else:
                sequence.append(line.strip())
        
        # Process the last gene
        if gene_name is not None and sequence:
            full_sequence = ''.join(sequence)
            if re.search(r'TATA[AT][AT]', full_sequence):
                outfile.write(f">{gene_name}\n{full_sequence}\n")
    
    print(f"TATA box-containing genes saved to: {output_file_path}")

# Example usage with ABSOLUTE INPUT PATH
input_path = r'C:\Users\21507\Desktop\生物信息学\IBI1\notes\IBI_12024-2025\IBI1_2024-25\Practical7\Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa'
extract_tata_genes(
    input_file_path=input_path,
    output_file_name='tata_genes.fa'
)