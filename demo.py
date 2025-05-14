import pandas as pd
import matplotlib.pyplot as plt


def read_mrna():
    file_name = str(input("please input the file name:"))
    file = open(file_name , "r").read()
    index = file.find("\n")
    mrna = file[index:]
    mrna = mrna.replace("\n" , "")
    return mrna
    

def find_codons(mrna):
    codons = []
    stop_codon = ["UAA" , "UAG" , "UGA"]
    start_index = mrna.find("AUG")
    if start_index == -1:
        print("No start codon found.")
    else:
        coding_region = mrna[start_index:]
        for i in range(0 , len(coding_region) , 3):
            codon = coding_region[i : i + 3]
            if codon in stop_codon or len(codon) != 3:
                break
            codons.append(codon)
    return codons

mrna = read_mrna()

def select_task():
    task = int(input("please select the task:"))
    codons = find_codons(mrna)
    if task == 1:
        from task1 import abc
        abc(codons)
    elif task == 2:
        from task2 import nucleotide_amino
        print(nucleotide_amino(mrna))
    elif task == 3:  
        from task3 import plot_amino_acid_frequency
        plot_amino_acid_frequency(codons)
    elif task == 4:
        mrna2 = str(input())
        from task4 import compare_mrna
        compare_mrna(mrna , mrna2 , 11)
    else:
        print("please input 1, 2, 3 or 4")
        return select_task()
        
select_task()