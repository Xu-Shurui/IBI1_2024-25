import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from collections import Counter
from Bio.Data import CodonTable
from mpl_toolkits.mplot3d import Axes3D

# Biochemical property dictionary (example: Kyte-Doolittle hydrophobicity)
hydrophobicity = {
    'A': 1.8, 'R': -4.5, 'N': -3.5, 'D': -3.5, 'C': 2.5,
    'Q': -3.5, 'E': -3.5, 'G': -0.4, 'H': -3.2, 'I': 4.5,
    'L': 3.8, 'K': -3.9, 'M': 1.9, 'F': 2.8, 'P': -1.6,
    'S': -0.8, 'T': -0.7, 'W': -0.9, 'Y': -1.3, 'V': 4.2
}

def plot_aa_terrain(codons):
    # 1. Translation and frequency counting
    rna_table = CodonTable.standard_rna_table
    amino_acids = [rna_table.forward_table[codon] for codon in codons 
                  if codon in rna_table.forward_table]
    aa_counts = Counter(amino_acids)
    
    # 2. Create grid for terrain
    aa_list = list(aa_counts.keys())
    x = np.arange(len(aa_list))  # Amino acid sequence
    y = np.array([hydrophobicity[aa] for aa in aa_list])  # Biochemical property
    z = np.array([aa_counts[aa] for aa in aa_list])       # Frequency
    
    # 3. Create meshgrid for surface
    X, Y = np.meshgrid(np.linspace(x.min(), x.max(), 30),
                       np.linspace(y.min(), y.max(), 30))
    Z = griddata((x, y), z, (X, Y), method='cubic')  # Interpolate
    
    # 4. Plot setup
    fig = plt.figure(figsize=(16, 10))
    ax = fig.add_subplot(111, projection='3d')
    
    # 5. Terrain surface plot
    surf = ax.plot_surface(
        X, Y, Z, cmap='terrain', alpha=0.8,
        linewidth=0, antialiased=True, rstride=1, cstride=1
    )
    
    # 6. Scatter peaks for amino acids
    ax.scatter(x, y, z+0.5, c='red', s=50, depthshade=True,
               label='Amino Acid Peaks')
    
    # 7. Labels and styling
    ax.set_xticks(x)
    ax.set_xticklabels(aa_list, rotation=45)
    ax.set_xlabel('Amino Acid', labelpad=15)
    ax.set_ylabel('Hydrophobicity', labelpad=15)  # Meaningful 3rd dimension
    ax.set_zlabel('Frequency', labelpad=15)
    ax.set_title('Amino Acid Frequency Terrain\n(Height=Frequency, Landscape=Hydrophobicity)', 
                pad=20, fontweight='bold')
    
    # 8. Colorbar and legend
    fig.colorbar(surf, ax=ax, shrink=0.5, aspect=10, label='Frequency Elevation')
    ax.legend()
    
    plt.tight_layout()
    plt.savefig('aa_terrain.png', dpi=300, bbox_inches='tight')
    plt.show()

# Example usage
codons = ['AUG', 'UUG', 'AUC', 'CAC', 'UAC', 'UUU', 'AGU', 'UAC', 'UUG', 'GUC', 'UCG', 'GAU', 'AAU', 'CUU', 'GGU', 'CCA', 'AAA', 'AAG', 'UUA', 'AAA', 'GGU', 'CUA', 'CCU', 'UCC', 'GGU', 'GGU', 'AAC', 'GAG', 'AUA', 'ACA', 'ACG', 'AUU', 'CAC', 'CAC', 'CCU', 'GCA', 'UAC', 'GGA']
plot_aa_terrain(codons)