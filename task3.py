import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from collections import Counter
from Bio.Data import CodonTable

def plot_amino_acid_frequency(codons):
    sns.set_palette("rocket")  
    plt.rcParams['font.family'] = 'DejaVu Sans'  
    rna_table = CodonTable.standard_rna_table 
    amino_acids = []
    for codon in codons:
        try:
            amino_acids.append(rna_table.forward_table[codon]) 
        except KeyError:
            pass 
    aa_counts = Counter(amino_acids)
    df = pd.DataFrame({
        'Amino Acid': aa_counts.keys(),
        'Frequency': aa_counts.values()
    }).sort_values('Frequency', ascending=False)
    fig, ax = plt.subplots(figsize=(14, 7), dpi=120)
    bars = ax.bar(
        df['Amino Acid'], 
        df['Frequency'],
        edgecolor='white',
        linewidth=1.5,
        alpha=0.9
    )
    for bar in bars:
        height = bar.get_height()
        ax.annotate(
            f"{height}",
            xy=(bar.get_x() + bar.get_width() / 2, height),
            xytext=(0, 3),
            textcoords='offset points',
            ha='center',
            va='bottom',
            fontsize=11,
            weight='bold',
            color='black'
        )
    ax.set_title(
        'mRNA AMINO ACID FREQUENCY DISTRIBUTION\n',
        fontsize=18,
        fontweight='bold',
        pad=20,
        color='#333333'
    )
    ax.set_xlabel(
        'Amino Acid',
        fontsize=14,
        labelpad=12,
        fontweight='bold'
    )
    ax.set_ylabel(
        'Frequency Count',
        fontsize=14,
        labelpad=12,
        fontweight='bold'
    )
    plt.xticks(
        rotation=45,
        fontsize=12,
        fontweight='bold'
    )
    plt.yticks(fontsize=12)
    ax.yaxis.grid(
        True,
        linestyle='--',
        alpha=0.4,
        color='gray'
    )
    from matplotlib.patches import Patch
    legend_elements = [
        Patch(facecolor='#801d37', label=f'Total Codons: {len(codons)}'),
        Patch(facecolor='#b83246', label=f'Unique AAs: {len(df)}')
    ]
    ax.legend(
        handles=legend_elements,
        loc='upper right',
        frameon=True,
        framealpha=0.9
    )
    plt.tight_layout()
    plt.savefig('aa_frequency.png', dpi=300, bbox_inches='tight')
    plt.show()
codons = ['AUG', 'UUG', 'AUC', 'CAC', 'UAC', 'UUU', 'AGU', 'UAC', 'UUG', 'GUC', 'UCG', 'GAU', 'AAU', 'CUU', 'GGU', 'CCA', 'AAA', 'AAG', 'UUA', 'AAA', 'GGU', 'CUA', 'CCU', 'UCC', 'GGU', 'GGU', 'AAC', 'GAG', 'AUA', 'ACA', 'ACG', 'AUU', 'CAC', 'CAC', 'CCU', 'GCA', 'UAC', 'GGA']
plot_amino_acid_frequency(codons)