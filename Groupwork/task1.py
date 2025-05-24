import pandas as pd

mRNA = str(input())

# delete the space charcter
mRNA = mRNA.replace(" " , "")
        
stop_codon = ["UAA" , "UAG" , "UGA"]
start_index = mRNA.find("AUG")
codons = []
if start_index == -1:
    print("No start codon found.")
else:
    coding_region = mRNA[start_index:]
    for i in range(0 , len(coding_region) , 3):
        codon = coding_region[i : i + 3]
        if codon in stop_codon or len(codon) != 3:
            break
        # the condons are now stored in the list "codons"
        codons.append(codon)
    
    df = pd.DataFrame({"Codon" : codons}) 
    codon_counts = df["Codon"].value_counts().reset_index()
    codon_counts.index += 1
    codon_counts.columns = ["Codon" , "Count"]
    # codon_counts is a dataframe with 3 columns
    # the first column is the index
    # the second coloumn lists the codons
    # the third column is the times that each codon appears
    print(codon_counts)
    # find the most common codon
    row1 = codon_counts.loc[1]
    codon1_count = row1.loc["Count"]
    most_common_codon = codon_counts[codon_counts["Count"] == codon1_count]["Codon"].tolist()
    if len(most_common_codon) == 1:
        if codon1_count == 1:
            print(f"The most common codon is {most_common_codon} and it appears 1 time.")
        else:
            print(f"The most common codon is {most_common_codon} and it appears {codon1_count} times.")
    else:
        if codon1_count == 1:
            print(f"The most common codons are {most_common_codon} and they appear 1 time.")
        else:
            print(f"The most common codons are {most_common_codon} and they appear {codon1_count} times.")
    