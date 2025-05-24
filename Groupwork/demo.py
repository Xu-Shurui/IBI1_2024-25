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

def select_task():
    task = int(input("please select the task:"))
    codons = find_codons(mrna)
    if task == 0:
        return 0
    elif task == 1:
        from Groupwork.task1 import most_frequent_nucleotide
        most_frequent_nucleotide(codons)
        return select_task()
    elif task == 2:
        from Groupwork.task2 import nucleotide_amino
        print(nucleotide_amino(codons))
        return select_task()
    elif task == 3:
        from Groupwork.task3 import plot_amino_acid_frequency
        plot_amino_acid_frequency(codons)
        return select_task()
    elif task == 4:
        file_name = str(input("please input the file name fo the second mRNA sequence:"))
        file = open(file_name , "r").read()
        index = file.find("\n")
        mrna2 = file[index:]
        mrna2 = mrna2.replace("\n" , "")
        from Groupwork.task4 import compare_mrna
        compare_mrna(mrna, mrna2, 11)
        return select_task()
    else:
        print("please input 0, 1, 2, 3 or 4")
        return select_task()

mrna = read_mrna()       
select_task()