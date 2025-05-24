import re
import os

def validate_splice_combination(user_input):
    """Validate user input for splice donor/acceptor combinations"""
    allowed_combinations = {'GTAG', 'GCAG', 'ATAG'}
    user_input = user_input.strip().upper()
    if user_input not in allowed_combinations:
        raise ValueError(f"Invalid combination. Please enter one of: {', '.join(allowed_combinations)}")
    return user_input

def find_splice_sites(sequence, donor_acceptor):
    """Check if sequence contains the specified splice pattern"""
    donor = donor_acceptor[:2]  # First 2 letters (e.g., 'GT')
    acceptor = donor_acceptor[2:]  # Last 2 letters (e.g., 'AG')
    pattern = re.compile(fr'{donor}[ATCG]+{acceptor}')
    return bool(pattern.search(sequence))

def count_tata_boxes(sequence):
    """Count occurrences of TATA box pattern in sequence"""
    return len(re.findall(r'TATA[AT][AT]', sequence))

def get_script_directory():
    """Get the directory where the Python script is located"""
    return os.path.dirname(os.path.abspath(__file__))

def main():
    print("Spliced TATA Genes Finder")
    print("=" * 40)
    
    # Get current script directory
    script_dir = get_script_directory()
    
    # Define input file path (in same directory as script)
    input_filename = "Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa"
    input_path = os.path.join(script_dir, input_filename)
    
    # Verify input file exists
    if not os.path.exists(input_path):
        print(f"\nERROR: Input file not found at: {input_path}")
        print("\nPlease ensure:")
        print(f"1. The file '{input_filename}' exists in the same folder as this script")
        print("2. The filename is spelled exactly as shown above (case-sensitive)")
        print("3. The file is downloaded from:")
        print("   ftp://ftp.ensemblgenomes.org/pub/fungi/release-46/fasta/saccharomyces_cerevisiae/cdna/")
        print("\nCurrent directory contents:")
        print("\n".join(os.listdir(script_dir)))
        return
    
    # Get user input for splice combination
    while True:
        try:
            user_input = input("\nEnter splice combination (GTAG, GCAG, or ATAG): ").strip()
            donor_acceptor = validate_splice_combination(user_input)
            break
        except ValueError as e:
            print(f"Error: {e}")
    
    # Set output path (same directory as script)
    output_filename = f"{donor_acceptor}_spliced_genes.fa"
    output_path = os.path.join(script_dir, output_filename)
    
    # Process the FASTA file
    print(f"\nProcessing {input_filename}...")
    found_genes = 0
    
    with open(input_path, 'r') as infile, open(output_path, 'w') as outfile:
        gene_name = None
        sequence = []
        
        for line in infile:
            if line.startswith('>'):
                # Process previous gene if exists
                if gene_name is not None and sequence:
                    full_sequence = ''.join(sequence)
                    if find_splice_sites(full_sequence, donor_acceptor):
                        tata_count = count_tata_boxes(full_sequence)
                        if tata_count > 0:
                            outfile.write(f">{gene_name} TATA_count={tata_count}\n{full_sequence}\n")
                            found_genes += 1
                
                # Start new gene record
                gene_name = line.strip().split()[0][1:]  # Extract gene name
                sequence = []
            else:
                sequence.append(line.strip())
        
        # Process the last gene in file
        if gene_name is not None and sequence:
            full_sequence = ''.join(sequence)
            if find_splice_sites(full_sequence, donor_acceptor):
                tata_count = count_tata_boxes(full_sequence)
                if tata_count > 0:
                    outfile.write(f">{gene_name} TATA_count={tata_count}\n{full_sequence}\n")
                    found_genes += 1
    
    print(f"\nCompleted! Found {found_genes} genes with:")
    print(f"- Splice pattern: {donor_acceptor}")
    print(f"- At least one TATA box")
    print(f"\nResults saved to: {output_path}")

if __name__ == "__main__":
    main()